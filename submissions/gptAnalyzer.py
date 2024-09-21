from openai import OpenAI
import json
from dotenv import loadenv
client = OpenAI(api_key=loadenv('OPENAI_KEY'))

def extract_skills(content):

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {#ONLY For debugging purposes, explain what made you choose each skill with a small sentence and a reference to the original document
        #Please do not say anything else, just return the list of words, separated by commas.
        "role": "system",
        "content": "You are a text analyzer. You are given an input text, sometimes a job description and sometimes a resume. You take the input text, analyze it, and return a list of probable skills displayed in the document. for example, maybe the resume of an entry-level c programmer is input and he has some experience in working with teams. I would expect you to return a list like the one following the colon: communication, teamwork, c programming, ... etc. Please do not say anything else, just return the list of words, separated by commas. Only use the following skills. If none of the following skills are present simply respond \"none\". Communication, Customer Service, Problem-Solving, Creativity, Interpersonal, Leadership, Time Management, Organizational, Adaptability, Critical Thinking, Decision-Making, Teamwork, Attention to Detail, Self-Motivation, Work Ethic, Project Management, Customer Service, Conflict Resolution, Technical Literacy, Research, Cultural Awareness, Negotiation, Reliability, Resilience, Ethical Judgment, Emotional Intelligence. "
        },
        {
        "role": "user",
        "content": "{}".format(content)
        },
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response)

    skills = json.loads(response.model_dump_json())

    print(skills)

    return skills['choices'][0]['message']['content']