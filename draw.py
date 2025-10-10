def draw_square(num):
    square=[]
    if num > 0:
        for i in range(num):
            for _ in range(num):
                square.append('*')
            if i != num -1:
                square.append('\n')
    else:
        raise(ValueError)
    return ''.join(square)

def draw_triangle(num):
    triangle=[]
    if num > 0:
        for i in range(num):
            for _ in range(i+1):
                triangle.append('*')
            if i != num -1:
                triangle.append('\n')
    else:
        raise(ValueError)
    return ''.join(triangle)

def draw_hollow_rectangle(col,row):
    rectangle=[]
    if col > 0 and row > 0:
        for r in range(row):
            for c in range(col):
                if r == 0 or r == row - 1:
                    rectangle.append('*')
                else:
                    if c == 0 or c == col -1:
                        rectangle.append('*')
                    else:
                        rectangle.append(' ')
            if r != row - 1:
                rectangle.append('\n')
    else:
        raise(ValueError)
    return ''.join(rectangle)



            

                
    
