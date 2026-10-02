#test = input("what ur skill\n")
#skills = ["azure" , "java", "net" , "testing" , "sql"]
#for a in skills:
#   if a in test:
#   print("Found" , a)
#   else:
#   print("missing" , a)
#import json
#with open("skills.json" , "r") as file:
    #x = json.load(file)
#y = x["skills"]
#print(y)

#with open("skills.json" , "a") as file:
#    file.write("cobol\n")
#    file.write("plsql\n")

#try:
#    text = int(input("WHAT IS YOUR AGE\n"))
#    text1 = 10 / text
#    print(text1)

#except ValueError:
#    print("enter vaid number")

#except ZeroDivisionError:
#    print("zero division error")


import json

with open("skills.json", "r") as file:
    data = json.load(file)

x = data["skills"]

test = input("What are your skills?\n")

test = test.lower()

print("\nSkills found:")

for skill in x:
    if skill.lower() in test:
        print("Found:", skill)
    else:
        print("missing:" , skill)