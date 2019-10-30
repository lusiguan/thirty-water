import sys
import itertools
import requests
import re
import json
import http

class inside:
    flower=0 
    num=0  
    def __init__(self,f,n):
        self.flower=f
        self.num=n

one,two,three=[],[],[]    
ans_1,ans_2,ans_3=[],[],[]  
comp_1,comp_2,comp_3=[],[],[]   
fin_1,fin_2,fin_3=[],[],[]  
f1,f2,f3=[],[],[]   
compp1,compp2,compp3,compp_z=[],[],[],[]
card=[]


for i in range(0,20):
    one.append(inside(0,0))
    two.append(inside(0, 0))
    three.append(inside(0, 0))
    ans_1.append(inside(0, 0))
    ans_2.append(inside(0, 0))
    ans_3.append(inside(0, 0))
    comp_1.append(inside(0, 0))
    comp_2.append(inside(0, 0))
    comp_3.append(inside(0, 0))
    fin_1.append(inside(0,0))
    fin_2.append(inside(0, 0))
    fin_3.append(inside(0, 0))
    f1.append(0)
    f2.append(0)
    f3.append(0)

for i in range(0,3):
    compp1.append(inside(0,0))
for i in range(0,5):
    compp2.append(inside(0,0))
for i in range(0,5):
    compp3.append(inside(0,0))
for i in range(0,14):
    compp_z.append(inside(0,0))

global ant,c1,c2,c3,end_gra,mark 
ant,c1,c2,c3=0,5,5,3
end_gra ,mark= 0.0,0.0
global g1, g2, g3
global b1, b2, b3
global take,en,en2
flag_1=0
flag_2=0
flag_3=0

def findnum(x):
    return x.num


hua,number={},{}
for i in range(0,16):
    hua[i]=0
    number[i]=0



def qian():
    global gra
    for j in range(0, 16):
        hua[j] = 0
        number[j] = 0
    

    for i in range(0,3):
        compp1[i]=ans_3[i+1]
    compp1.sort(key=findnum) 

    for i in range(1,4):
        ans_3[i]=compp1[i-1]


    for i in range(1,4):
        hua[ans_3[i].flower] +=1
        number[ans_3[i].num]+=1
    k=1
    for i in range(1,5):
        if hua[i] == 3:
            for m in range(ans_3[1].num,ans_3[1].num+3):
                if number[m] < 1:
                    flag_1=0
                else:
                    flag_1=1
            if flag_1 == 1:
                k=(9.0+0.9 / 11.0 * (ans_3[1].num - 1))
                gra += k
                return k 
    k=1
    for i in range(1,5):
        if hua[i] == 3:
            k=(6.0 +0.9/(1300+130+13)*((ans_3[3].num-1)*100+(ans_3[2].num-1)*10+(ans_3[1].num-1))*1.0 )
            gra += k
            return k 
    k=1
    for i in range(ans_3[1].num,ans_3[1].num+3):
        if number[i] < 1:
            flag_2=0
        else:
            flag_2=1
    if flag_2 == 1:
        k=(5.0  + 0.9/11.0*(ans_3[1].num-1)*1.0)
        gra += k
        return k 
    k=1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 3:
            k=(4.0+0.9/13.0*(ans_3[1].num - 1)*1.0)
            gra += k
            return k
    k=1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            k=(1.0 + 0.9/(130+13)*((ans_3[i].num - 1)*10+k-1)*1.0)
            gra += k
            return k
    
    k=0.9 / (1300.0 + 130.0 + 13.0)*((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    gra += k
    return k 

def zhong():
    global gra
    for i in range(0, 16):
        hua[i] = 0
        number[i] = 0

    for i in range(0, 5):
        compp2[i] = ans_2[i + 1]

    compp2.sort(key=findnum)  
    for i in range(1, 6):
        ans_2[i] = compp2[i - 1]


    for i in range(1,6):
        hua[ans_2[i].flower] +=1
        number[ans_2[i].num]+=1

    k=1
    for i in range(1,5):
        if hua[i] == 5:
            for m in range(ans_2[1].num,ans_2[1].num+5):
                if number[m] < 1:
                    flag_2=0
                else:
                    flag_2=1
            if flag_2 == 1:
                k= (9.0 + 0.9 / 9 * (ans_2[1].num - 1)) * 1.0
                gra += k
                return k 

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            k=(8.0+ 0.9/(130+13)*((ans_2[i].num - 1)*10))*1.0
            gra += k
            return k

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 2:
                    k=(7.0 + 0.9 / (130 + 13)*((k - 1) * 10 + ans_2[j].num - 1))*1.0
                    gra += k
                    return k
    k=1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_2[5].num-1)*10000+(ans_2[4].num - 1)*1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + (ans_2[1].num - 1)))*1.0
            gra +=k
            return k
    k=1
    for i in range(ans_2[1].num,ans_2[1].num+5):
        if number[i] < 1:
            flag_2=0
        else:
            flag_2=1
    if flag_2 == 1 :
        k=(5.0 + 0.9/9*(ans_2[1].num - 1)*1.0)
        gra += k
        return k

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 1:
                    k=(4.0 + 0.9 / (1300+130+13) * ((k-1) * 100))
                    gra += k
                    return k

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(ans_2[i].num - ans_2[j].num) == 1 :
                    k=(3.0+ 0.9 / 10 * (ans_2[j].num-1-1)) * 1.0
                    gra += k
                    return k

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 :
                    k=(2.0 +0.9 / (130+13) * ((ans_2[i].num - 1) * 10+ans_2[j].num-1)) * 1.0
                    gra += k
                    return k 

    k=1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            k=(1.0+0.9/(130+13)*((ans_2[i].num-1)*10+k-1))*1.0
            gra += k
            return k 

    k=(0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + ans_2[1].num - 1))*1.0
    gra +=k
    return k


def hou():
    global gra
    for i in range(0, 16):
        hua[i] = 0
        number[i] = 0

    for i in range(0, 5):
        compp3[i] = ans_1[i + 1]

    compp3.sort(key=findnum)  
    for i in range(1, 6):
        ans_1[i] = compp3[i - 1]

    
    for i in range(1,6):
        hua[ans_1[i].flower] +=1
        number[ans_1[i].num]+=1

    k=1
    for i in range(1,5):
        if hua[i] == 5:
            for m in range(ans_1[1].num,ans_1[1].num+5):
                if number[m] < 1:
                    flag_3=0
                else:
                    flag_3=1
            if flag_3 == 1:
                k=(9.0 + 0.9 / 9 * (ans_1[1].num - 1)) * 1.0
                gra += k
                return k 

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            k=(8.0+ 0.9/(130+13)*((ans_1[i].num - 1)*10))*1.0
            gra += k
            return k

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 2:
                    k=(7.0 + 0.9 / (130 + 13)*((k - 1) * 10 + ans_1[j].num - 1))*1.0
                    gra += k
                    return k
    k=1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_1[5].num-1)*10000+(ans_1[4].num - 1)*1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + (ans_1[1].num - 1)))*1.0
            gra +=k
            return k 

    k=1
    for i in range(ans_1[1].num,ans_1[1].num+5):
            if number[i] < 1:
                flag_3=0
            else:
                flag_3=1
    if flag_3 == 1 :
        k=(5.0 + 0.9/9*(ans_1[1].num - 1)*1.0)
        gra += k
        return k

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 1:
                    k=(4.0 + 0.9 / (1300+130+13) * ((k-1) * 100))
                    gra += k
                    return k

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1 :
                    k= (3.0+ 0.9 / 10 * (ans_1[j].num-1-1)) * 1.0
                    gra +=k
                    return k 

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 :
                    k=(2.0 +0.9 / (130+13) * ((ans_1[i].num - 1) * 10+ans_1[j].num-1)) * 1.0
                    gra += k
                    return k 

    k=1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            k=(1.0+0.9/(130+13)*((ans_1[i].num-1)*10+k-1))*1.0
            gra += k
            return k 

    k=(0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + ans_1[1].num - 1))*1.0
    gra += k
    return  k


def charge() :
    global gra,end_gra,ant
    global g1, g2, g3
    global b1, b2, b3
    for i in range(1,4): 
        ans_3[i] = comp_3[i]
    for i in range(1,6): 
        ans_2[i] = comp_2[i]
    for i in range(1,6): 
        ans_1[i] = comp_1[i]
    gra = 0.0
    j1 = qian()
    g1 = gra
    j2 = zhong()
    g2 = gra - g1
    j3 = hou()
    g3 = gra - (g1 + g2)
    if j1 > j2 or j2 > j3 or j1 > j3 :
        gra = 0
    if gra>end_gra :
        end_ans = gra
        a1 = g1; a2 = g2; a3 = g3
        for i in range(1,4):
            fin_3[i] = ans_3[i]
        for i in range(1,6):
            fin_2[i] = ans_2[i]
        for i in range(1,6): 
            fin_1[i] = ans_1[i]
    ant+=1



def ser2(d,index_2) :
    for i in range(d,9):
        comp_2[index_2] = two[i]
        f2[i] = 1
        if index_2 == c2 :
            index_3 = 0
            for j in range(1,8+1):
                if f2[j] == 0 :
                    index_3+=1
                    comp_3[index_3] = two[j]
            charge()
        else :
            ser2(i + 1, index_2 + 1)
        f2[i] = 0


def ser1(d, index_1): 
    for i in range(d,13+1):
        f1[i] = 1
        comp_1[index_1] = one[i]
        if index_1 == c1 :
            index = 0
            for j in range(1,14):
                if f1[j] == 0:
                    index+=1
                    two[index] = one[j]
            ser2(1, 1)
        else:
            ser1(i + 1, index_1 + 1)
        f1[i] = 0




def number_to_hua(x):
    if x == 1:
        return "&"
    if x == 2:
        return "$"
    if x == 3:
        return "#"
    if x == 4:
        return "*"


def hua_to_number(x):
    if x == "&":
        return 1
    if x == "$":
        return 2
    if x == "#":
        return 3
    if x == "*":
        return 4

def change(x):
    if x==10:
        return "10"
    if x==11:
        return "J"
    if x==12:
        return "Q"
    if x==13:
        return "K"
    if x==14:
        return "A"
    return str(x)

def begingame(str0):
    frc = 0
    str1 = str0.replace("10", "M")
    for i in range(0,39,3):
        if str1[i + 1] == "M":
            x = inside(hua_to_number(str1[i]), 10)
        else:
            if str1[i + 1] == "J":
                x = inside(hua_to_number(str1[i]), 11)
            else:
                if str1[i + 1] == "Q":
                    x = inside(hua_to_number(str1[i]), 12)
                else:
                    if str1[i + 1] == "K":
                        x = inside(hua_to_number(str1[i]), 13)
                    else:
                        if str1[i + 1] == "A":
                            x = inside(hua_to_number(str1[i]), 14)
                        else:
                            x = inside(hua_to_number(str1[i]), int(str1[i + 1]))
        frc+=1
        one[frc]=x
        
def p_ans():
    sub_ans=[]
    s=""
    for i in range(1, 4):  
        if i!=3:
            s+=number_to_hua(fin_3[i].flower)+change(fin_3[i].num)+" "
        else:
            s+=number_to_hua(fin_3[i].flower)+change(fin_3[i].num)

    sub_ans.append(s)
    s=""
    for i in range(1, 6):  
        if i != 5:
            s += number_to_hua(fin_2[i].flower) + change(fin_2[i].num) + " "
        else:
            s += number_to_hua(fin_2[i].flower) + change(fin_2[i].num)
    sub_ans.append(s)
    s = ""
    for i in range(1, 6):
        if i != 5:
            s += number_to_hua(fin_1[i].flower) + change(fin_1[i].num) + " "
        else:
            s += number_to_hua(fin_1[i].flower) + change(fin_1[i].num)
    sub_ans.append(s)
    print(sub_ans)
    return sub_ans

def AI_split_cards(card):
    begingame(card)
    ser1(1, 1)
    sub_ans=p_ans()
    return sub_ans

if __name__ == "__main__":
    data = AI_split_cards("&4 #J &J *5 &2 &A $4 *J $5 &10 $7 *4 &5")


    
