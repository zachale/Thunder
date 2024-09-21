

skills = [
    "Communication", 
    "Problem-Solving", 
    "Creativity",
    "Interpersonal",
    "Leadership",
    "Time Management",
    "Organizational",
    "Adaptability",
    "Critical Thinking",
    "Decision-Making",
    "Teamwork",
    "Attention to Detail",
    "Self-Motivation",
    "Work Ethic",
    "Project Management",
    "Customer Service",
    "Conflict Resolution",
    "Technical Literacy",
    "Research",
    "Cultural Awareness",
    "Negotiation",
    "Reliability",
    "Resilience",
    "Ethical Judgment",
    "Emotional Intelligence"
]




def build_vector(input):
    vector = ""
    found = False
    seperated = input.split(', ')
    for skill in skills:
        for x in seperated:
            if x == skill.lower():
                vector += '1'
                found = True
                break
        if not found:
            vector += '0'  
        found = False      
    return vector

# returns how closely the candidate matches the posting via a percentage  
def vector_compare(posting,candidate):

    indexes = []
    num = 0
    
    for i in range(0,len(posting)):
        if posting[i] == '0':
            indexes.append(i)

    for i in range(0,len(indexes)):
        posting = delete_char(posting,indexes[i]-i)
        candidate = delete_char(candidate,indexes[i]-i)
    
    length = len(candidate)

    for i in range(0,length):
        if candidate[i] == '1':
            num += 1

    result = num / length

    print(posting)
    print(candidate)

    print(result * 100)


#adapted from https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/
def delete_char(string,index):
    byte = bytearray(string, 'utf-8')
    del byte[index]
    return byte.decode()

# print(build_vector("communication, leadership, teamwork, problem-solving, adaptability"))
# candidate = "11001001001"
# posting = "10101001001"
# print(candidate)

# print(posting)

# vector_compare(posting, candidate)