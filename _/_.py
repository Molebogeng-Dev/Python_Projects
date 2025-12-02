def pascal(num):
    ls=[[1]]
    for i in range(1,num+1):
        n_ls=[1]
        for j in range(i-1):
            n_ls.append(ls[-1][j] + ls[-1][j+1])
        n_ls.append(1)
        ls.append(n_ls)
        
    pascal=[]
    for i in ls:
        for _ in range(len(ls)-len(i)+2):
            pascal.append(' ')
        for j in i:
            pascal.append(str(j)+' ')
        pascal.append('\n')
    return ''.join(pascal)
    
            

print(pascal(5))

