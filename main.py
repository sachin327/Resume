import random
from tabulate import tabulate
import numpy as np

print("Start Game")
t=random.randint(1,4)
s="map"+str(t)
print(s+" selected")

l=np.loadtxt(s+".txt",dtype=np.int32)
ll=l.tolist()
print(tabulate(ll))

pos1=1
pos2=1
r1=0
c1=0
r2=0
c2=0
def update(pos,a,p):
  global r1,r2,c1,c2
  if(pos+a > 100):
    a=0
  pos+=a
  tmp=pos
  r=(pos-1)//10
  c=(pos-1)%10
  pos=l[r][c]
  r=(pos-1)//10
  c=(pos-1)%10
  if(p==1):
    if(type(ll[r1][c1])==tuple ):
      ll[r1][c1]="P2"
    else:
      ll[r1][c1]=l[r1][c1]

    if(ll[r][c]=="P2" or type(ll[r][c])==tuple):
      ll[r][c]=("P1","P2")
    else:
      ll[r][c]="P1"
    r1=r
    c1=c
  if(p==2):
    if(type(ll[r2][c2])==tuple):
      ll[r2][c2]="P1"
    else:
      ll[r2][c2]=l[r2][c2]

    if(ll[r][c]=="P1" or type(ll[r][c])==tuple):
      ll[r][c]=("P1","P2")
    else:
      ll[r][c]="P2"
    r2=r
    c2=c
  print(tabulate(ll))
  if(tmp==pos):
    return pos,"N"
  if(tmp<pos):
    return pos,"L"
  return pos,"S"


def play(pos,p):
  a=6
  b="L"
  while(a==6 or b=="L"):
    input("Player%d's turn" %p)
    a=random.randint(1,6)
    print(a)
    pos,b=update(pos,a,p)
    if(pos==100):
      break
  return pos


while(pos1!=100 and pos2!=100):
  #Player1
  pos1=play(pos1,1)
  if(pos1==100):
    print("Player1 Win")
    break
  print("Pos1 : %d" %pos1)

  #Player2
  pos2=play(pos2,2)
  if(pos2==100):
    print("Player2 Win")
    break
  print("Pos2 : %d" %pos2)
  