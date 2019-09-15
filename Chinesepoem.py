import random
#coding: utf-8
print('Please enter source file name (3 names in total, adjective, noun, verb), the files shoule be in the same derectory as the program.')
adj=input()
noun=input()
verb=input()
try:
    '''file=open(adj,'r',encoding='UTF-8')
    adj=file.read().split('\n')
    file=open(noun,'r',encoding='UTF-8')
    noun=file.read().split('\n')
    file=open(verb,'r',encoding='UTF-8')
    verb=file.read().split('\n')'''
    adj=open('adj.txt','r',encoding='UTF-8').read().split('\n')
    noun=open('noun.txt','r',encoding='UTF-8').read().split('\n')
    verb=open('verb.txt','r',encoding='UTF-8').read().split('\n')
except Exception as e:
    print(e)
try:
    output=random.choice(adj),"的",random.choice(noun),",",random.choice(adj),"地",random.choice(verb),"着",random.choice(adj),"的",random.choice(noun)
    file=open('chinesepoem.txt','w')
    i=0
    string=''
    while i<len(output):
        string+=output[i]
        i+=1
    print(string)
    file.write(string)
    file.close()
except Exception as e:
    print(e)
