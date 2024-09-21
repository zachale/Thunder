from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# conn = psycopg2.connect(host="localhost",dbname="postgres", user="postgres",password="Ethiodb04pia/")
# cur = conn.cursor()
# cur.execute("""
#                 INSERT INTO candidates (name, email, id) VALUES
#                 ('jon','jon@gmail.com',1),
#                 ('jim','jim@gmail.com',2),
#                 ('cruncher69','crunchmaster@gmail.com',3),
#                 ('wowee!','waht@gmail.com',4),
#                 ('zach','zowee@gmail.com',5),
#                 ('rachel','rachel@gmail.com',6);
#                 """)
# conn.commit()
# cur.close()
# conn.close()

def say_hello(request):
    x = 1
    y = 2
    
    
    return render(request, 'hello.html', {'name': 'Mosh'})



# Create your views here.
#request handler
#takes a request and returns a response!
#some frameworks call it an action!