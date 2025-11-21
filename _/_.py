import sys

class Techniques:
    def __init__(self,sudoku_ls):
        self.sudoku_numbers=[9,8,7,6,5,4,3,2,1]
        self.sudoku_ls= sudoku_ls

    #finding a row that needs candidate/s
    def possible_nums(self,r_c,cell):
        #row
        current_row= self.sudoku_ls['rows'][r_c]
        for i in range(len(current_row)):
            try:
                #row
                if current_row[i] == 0:
                    current_row[i] =[]
                        
                    for num in self.sudoku_numbers:
                        try:
                            if num not in current_row and num not in cell:
                                current_row[i].append(num)
                        except TypeError:
                            pass
                
                    #column
                    current_column= self.sudoku_ls['cols'][i]
                    for i in range(len(current_column)):
                        try:
                            if current_column[i] == 0:
                                current_column[i]= []
                                
                                for num in self.sudoku_numbers:
                                    try:
                                        if num not in current_column and num not in cell or num in current_row[i]:
                                            current_column[i].append(num)
                                    except TypeError:
                                        pass
                                if len(current_column[i]) == 1:
                                    current_column[i]= current_column[i][0]
                                current_row[i] = current_column[i]
                                return current_column[i]
                        except TypeError:
                            pass
            except TypeError:
                pass

    #finding a cell that needs candidate/s
    def cell(self):
        #row and column changer
        row_counter=-1
        for cell in self.sudoku_ls['cells']:
            for index, num in enumerate(cell):
                if index % 3 == 0:
                    row_counter+=1
                    if row_counter == len(self.sudoku_ls['rows']):
                        row_counter=0
                if num == 0:
                    cell[index] = self.possible_nums(row_counter,cell)
        print('CELLS:\n',self.sudoku_ls['cells'],'\n==================\nROWS:\n',self.sudoku_ls['rows'],'\n==================\nCOLS:\n',self.sudoku_ls['cols'])

                    # self.col(row_i[1])
                




def numbers(puzzle):
    numbers_ls,ls=[],[]
    for nums in puzzle:
        for num in nums:
            if num.isdigit():
                ls.append(int(num))
            if len(ls) == 9:
                numbers_ls.append(ls)
                ls=[]
    return numbers_ls

def organized(numbers):
    sudoku= {'rows': [],'cols': [],'cells': []}
    #rows
    sudoku['rows']= numbers
    #columns
    num= 0
    while num != len(numbers):
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

    # print('CELLS:\n',sudoku['cells'],'\n==================\nROWS:\n',sudoku['rows'],'\n==================\nCOLS:\n',sudoku['cols'])
    return sudoku

def main():
    sudoku_crc=''
    # if len(sys.argv) != 4:
    #     sys.exit("Incorrect arguments")
        
    with open('puzzle.txt') as puzzle:#sys.argv[1]
        sudoku_crc= Techniques(organized(numbers(puzzle)))
    
    sudoku_crc.cell()


    # if sys.argv[2] == '-o':
    #     #printing table with numbers (remove later).
    #     with open(sys.argv[3], 'w') as sovled_puzzle:
    #         for num in range(len(sudoku_crc)):
    #             for d,i in enumerate(sudoku_crc[num]):
    #                 if (d+1)%3 == 0 and d != 0:
    #                     sovled_puzzle.write(f'{i}|')
    #                 else:
    #                     sovled_puzzle.write(f'{i} ')

    #             if (num+1)%3 == 0:
    #                 sovled_puzzle.write('\n==================')

    #             sovled_puzzle.write('\n')

if __name__ == "__main__":
    main()