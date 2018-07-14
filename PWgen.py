import random
import string

final_string = [""]

name = input("Enter a name for this file: ")
amount = int(input("Enter the amount of PW's to generate: "))

l_alphabet = []
for letter in range(97,123):
    l_alphabet.append(chr(letter))

u_alphabet = [] 
for letter in range(65, 91):
    u_alphabet.append(chr(letter))

def gen():
    parts = ["Symbol","Number","Char","Capital"]
    for i in range(4):
        choice_1 = random.choice(parts)
        parts.remove(parts[parts.index(choice_1)])
        part_1 = eval(choice_1+"()")
        print(parts)
    return final_string

def Symbol():#4
    for i in range(4):
        final_string.append(random.choice(l_alphabet))

def Capital():#4
    for i in range(4):
        final_string.append(random.choice(u_alphabet))
    
def Number():#4
    for i in range(4):
        final_string.append(random.choice(["1","2","3"]))
    
def Char():#4
    for i in range(4):
        final_string.append(random.choice(["!","?","$","-","_"]))

for i in range(amount):
    with open(name+".txt","a") as w:
        w.write("\n"*5)
        w.write("_______________________"+" "*10)
        w.write("".join(gen()))
        final_string = [""]
