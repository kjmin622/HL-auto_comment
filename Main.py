import random

def in_sa(name):

    hoching = name+"친구"
    
    insa = random.choice([
        "안녕하세요",
        "반가워요",
        "정말 반가워요",
        ])
    
    end = random.choice(["!","!!","~!","ㅎㅎㅎ","~~",":)","^^"])

    return random.choice([insa+' '+hoching+end,hoching+' '+insa+end])

def mid(hak_ga):

    how = random.choice(["합격","입학"])

    bu_sa = random.choice(["정말","많이","정말 많이"])

    school = random.choice(["에리카","한에리카","한양대 에리카"])

    celebrate = random.choice([
        "축하드려요",
        "축하해요",
        "축하해요! 정말 멋있어요",
        "축하드려요! 정말 수고하셨어요",
        "축하드리고 정말정말 수고하셨어요"])

    end = random.choice(["!","!!","~!","ㅎㅎㅎ","~~",":)","^^"])

    return random.choice([
        hak_ga+' '+how+' '+bu_sa+' '+celebrate+end,
        school+' '+how+' '+bu_sa+' '+celebrate+end,
        school+' '+hak_ga+' '+how+' '+bu_sa+' '+celebrate+end])

def end():
   pass 

name = input("name: ")
hak_ga = input("hak_ga: ")
print(in_sa(name)+' '+mid(hak_ga))

