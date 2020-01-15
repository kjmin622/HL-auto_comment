import random

def in_sa(name):

    hoching = name+"친구"
    
    insa = random.choice([
        "안녕하세요",
        "반가워요",
        "정말 반가워요",
        "정말정말 반가워요",
        "반가워용"
        ])
    
    end = random.choice(["!","!!","~!","ㅎㅎㅎ","~~",":)","^^"])

    return random.choice([insa+' '+hoching+end,hoching+' '+insa+end])

def mid(hak_ga):

    how = random.choice(["합격","입학"])

    bu_sa = random.choice(["정말","많이","정말 많이"])

    school = random.choice(["에리카","한양대 에리카"])

    celebrate = random.choice([
        "축하드려요",
        "축하해요",
        "축하드려요! 정말 수고 하셨어요",
        "축하드리고 정말정말 수고하셨어요"])

    end = random.choice(["!","!!","~!","ㅎㅎㅎ","~~",":)","^^"])

    return random.choice([
        hak_ga+' '+how+' '+bu_sa+' '+celebrate+end,
        school+' '+how+' '+bu_sa+' '+celebrate+end,
        school+' '+hak_ga+' '+how+' '+bu_sa+' '+celebrate+end])

def end():
    one = random.choice([
        "학교에 대해 궁금한 점 있으시면",
        "궁금한 점 있으시면",
        "학교 생활에 대해 궁금하신 거 있으시면",
        "대학 생활에 대해 궁금한게 있으시면",
        "궁금한 것은"])

    two = random.choice([
        "뭐든지 물어봐 주시고",
        "무엇이든지 휴라 질문 게시판이나 오픈채팅에 물어봐주시고",
        "뭐든지 질문해주시길 바라구",
        "뭐든지 질문해주시길 바라고",
        "무엇이든 휴아라이프에게 편하게 질문해주시고",
        "언제든지 휴라에게 맡겨주시고"])


    three = random.choice([
        "휴라와 함께 많은 친구들과 선배 알아가시길 바라요",
        "휴라와 함께 더 즐거운 캠퍼스 생활 준비하시길 바라요",
        "더 즐거운 캠퍼스 생활 휴라와 함께 준비합시다",
        "즐거운 대학생활, 저희와 함께 준비해 나가요",
        "휴라에서 많은 사람들과 친해지시길 바라요"])

    end = random.choice(["!","~~!!","~~~~","ㅎㅎ!!",":)","*^^*","!!!!","~~","😀"])

    return one+' '+two+' '+three+end


def create(name,hakga):
    str = in_sa(name)+' '+mid(hakga)+' '+end()
    return str
