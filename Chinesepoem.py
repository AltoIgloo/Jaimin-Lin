import random

a="渺远"
b="人为"
c="睿智"
d="数码"
e="朦胧"
f="诡谲"
g="逻辑"
h="梦幻"
i="沉稳"
j="黯淡"
k="至高"
l="虚无"
m="浩渺"
n="无情"
o="隐形"
p="模糊"
q="终极"
adj1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]

A="苍穹"
B="寰宇"
C="圣堂"
D="祭坛"
E="高塔"
F="鲸落"
G="云霭"
H="飞星"
I="晶尘"
J="日光"
K="齿轮"
L="方碑"
M="莽野"
N="电波"
O="暗影"
noun1=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O]

aa="掩饰"
bb="吞噬"
cc="解构"
dd="幻化"
ee="关闭"
ff="播撒"
gg="击碎"
hh="跪拜"
ii="眺望"
jj="重塑"
kk="创生"
ll="沉湎"
mm="指引"
nn="消融"
oo="炙烤"
pp="灼烧"
verb1=[aa,bb,cc,dd,ee,ff,gg,hh,ii,jj,kk,ll,mm,nn,oo,pp]

con=1
while 1:
    print(random.choice(adj1),"的",random.choice(noun1),",",random.choice(adj1),"地",random.choice(verb1),"着",random.choice(adj1),"的",random.choice(noun1))
    con=con+1
    if con > 4:
        break