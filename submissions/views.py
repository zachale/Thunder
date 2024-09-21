from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
import psycopg2
from .forms import UploadFileForm
import uuid
import json
from .gptAnalyzer import extract_skills
from .vectorCreater import build_vector

#imports for extracting text from a pdf
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO




@csrf_exempt
def submit_posting(request):
    if request.method == "POST":

            id = uuid.uuid4()
 
            data = json.loads(request.body)
            skills = extract_skills(data['description'])


            build_vector(skills)

            conn = psycopg2.connect(host="localhost",dbname="postgres", user="postgres",password="1234")
            cur = conn.cursor()
            cur.execute(
                            "INSERT INTO postings (id, description, skills) VALUES (%s,%s,%s)"
                            ,(str(id), data['description'],)
                        )
            conn.commit()
            cur.close()
            conn.close()

            with open('data/postings/{}.txt'.format(id),'w') as f:
                f.write(data['description'])
            return HttpResponse(id)





@csrf_exempt
def submit_candidate(request):
    if request.method == "POST":
        
        form = UploadFileForm(request.POST, request.FILES)

        print(form.errors)
        if form.is_valid():

            id = uuid.uuid4()

            context = {
                'file':form.cleaned_data['file'],
                'id': id,
                'path': 'resumes',
                'type': 'pdf'
            }

            #converts file to text and then uses GPT to extract skills
            skills = extract_skills(extract_file(context))
            
            
            conn = psycopg2.connect(host="localhost",dbname="postgres", user="postgres",password="1234")
            cur = conn.cursor()  
            cur.execute(
                            "INSERT INTO candidates (name, email, id, skills) VALUES (%s,%s,%s,%s)"
                            ,(form.cleaned_data['name'], form.cleaned_data['email'],  str(id),skills)
                        )
            conn.commit()
            cur.close()
            conn.close()

            
            return HttpResponse(form)
        
        else:
            print('error')
            return HttpResponse(form.errors)
        

def extract_file(context):
    destination = open("data/{}/{}.{}".format(context['path'],context['id'],context['type']), "wb+") 
    for chunk in context['file'].chunks():
        destination.write(chunk)
    destination.close()
    return extract_text(context['id'])

#adapted from https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
def extract_text(id):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open('data/resumes/{}.pdf'.format(id), 'rb')
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    for page in PDFPage.get_pages(fp, None, 5):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    fp = open('data/text_resumes/{}.txt'.format(id),'w',encoding='utf-8')
    fp.write(text)
    fp.close

    return text




    