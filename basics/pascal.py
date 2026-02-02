def tri(num):
    ls = [['1\n']]

    for i in range(1,num+1):
        new_ls=['1']
        for j in range(i-1):
            new_ls.append(str(int(ls[i-1][j])+int(ls[i-1][j+1])))
        new_ls.append('1\n')
        ls.append(new_ls)

    return ls
        
        

print(tri(4))

    
