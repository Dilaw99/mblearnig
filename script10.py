
def somme2(var) :
    s2=0
    for i in range(0,len(var)) :
        s2=s2+var[i]
    return s2

tpl=(1,2,3,4,5,6,7,8,9,10)
print(somme2(tpl))
