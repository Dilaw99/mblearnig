li=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(li)) :
    for k in  range(0,len(li)) :
        if li[i]==2*k :
            print(li[i],'ce numéro est pair')
            break
        elif li[i]==2*k+1 :
            print(li[i],'ce numéro est impair')
            break