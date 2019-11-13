def main(l):
    p,q=0,0
    flag =0
    
    for i in range(len(l)):
        
        if isinstance(l[i],int):
            q = i
            if p ==0 and flag == 0:
                temp = 0
                flag = 1
            else:
                temp = l[p]
            for j in range(p,q+1):
                l[j] = (temp+l[q])/(q-p+1)
                
            p= q
            
        else:
            pass
    if l[-1] == '_':
        temp = l[p]
        for j in range(p,len(l)):
            l[j] = temp/(len(l)-p)
        
    
    return l

 

print(main(l))
