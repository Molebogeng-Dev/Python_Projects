import sys,random 
'''$ python dice_simulator.py --dice 2 --faces 6 --rolls 1000 --weights 1,1,1,1,2,2 --bins 10'''

def frequency():
    added_nums=[]
    for _ in range(int(sys.argv[6])):
        added_nums.append(sum(random.choices([int(num) for num in range(1,int(sys.argv[4]) + 1)],weights=[int(num) for num in sys.argv[8].split(',')],k=int(sys.argv[2]))))
    counted_nums= {num: added_nums.count(num) for num in range(2,(int(sys.argv[4])*2)+1)}
    return counted_nums

def mean(values):
    mean= round(float(sum(values)/len(values)),1)
    return mean
    
def median(values):
    sort=sorted(values)
    if len(sort) % 2 != 0:
        return sort[(len(sort)-1)//2]
    else:
        return sum[sort[(len(sort)-1)//2],sort[((len(sort)-1)//2)+1]]

def mode(values):
    counted= {} 
    value=[]
    for num in values:
        counted[num]=values.count(num)
    m= max([counted[value] for value in counted.keys()])
    for num in counted:
        if counted[num] == m and num not in value:
            value.append(str(num))
    if len(value) != 1:
        return ','.join(value)
    else:
        return value[0]

def variance(values):
    sums= {}
    for num in values:
        sums[num]= sum(values) - num
    print(sums) 


print(f'Number of Dice: {sys.argv[2]}\nNumber of Rolls: {sys.argv[6]}\nDice Faces: {sys.argv[4]}\nWeights: [{sys.argv[8]}]\n')
print('Frequency Distribution:')
print('Outcome  Frequency')
for i in frequency():
    if frequency()[i] > 0:
        print(str(i)+'        '+str(frequency()[i]))

print("Histogram:")
for i in frequency():
    if frequency()[i] > 0:
        print(str(i)+':  '+'*'*(frequency()[i]//5))

numbers_ls= [frequency()[value] for value in frequency()]
print('Summary Statistics:')
print(f'Mean: {mean(numbers_ls)}')
print(f'Median: {median(numbers_ls)}')
print(f'Mode: {mode(numbers_ls)}')
# print(f'Variance: {variance(numbers_ls)}')



