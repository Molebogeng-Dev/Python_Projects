import sys

# class Cross_hatch:
#     #find a cell that a number can fill one block
#     @staticmethod
#     def hidden_single(numbers):
#         for num in numbers:

        
#     def naked_single(self):
#         ...

def numbers(puzzle):
    return [i.split() for i in puzzle]

def organized(numbers):
    sudoku= {'rows': [],'cols': [],'cells': []}
    #rows
    sudoku['rows']= numbers
    #columns
    num= 0
    while num != len(numbers) - 1:
        ls=[]
        for i in range(len(numbers)):
            ls.append(numbers[i][num])
        sudoku['cols'].append(ls)
        num +=1
    #cells
    r1,r2=0,3
    while r2 <= 9:
        ls=[]
        for nums in range(len(numbers)):
            for i in range(r1,r2):
                ls.append(numbers[nums][i])
            if (nums + 1) % 3 == 0:
                sudoku['cells'].append(ls)
                ls=[]
        r1+=3
        r2+=3

    return sudoku



def main():
    sudoku_numbers=''
    # if len(sys.argv) != 4:
    #     sys.exit("Incorrect arguments")
        
    with open('puzzle.txt') as puzzle:#sys.argv[1]
        sudoku_numbers= organized(numbers(puzzle))

    
    # if sys.argv[2] == '-o':
    #     #printing table with numbers (remove later).
    #     with open(sys.argv[3], 'w') as sovled_puzzle:
    #         for num in range(len(sudoku_numbers)):
    #             for d,i in enumerate(sudoku_numbers[num]):
    #                 if (d+1)%3 == 0 and d != 0:
    #                     sovled_puzzle.write(f'{i}|')
    #                 else:
    #                     sovled_puzzle.write(f'{i} ')

    #             if (num+1)%3 == 0:
    #                 sovled_puzzle.write('\n==================')

    #             sovled_puzzle.write('\n')

if __name__ == "__main__":
    main()