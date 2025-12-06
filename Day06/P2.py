with open("Day06/input.txt", "r") as file:
    txt= file.read()
with open("Day06/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split('\n')
test_data = test_txt.split('\n')

# quick switch for test_data
# data = test_data

solutions = []

for i in range(len(data[-1])):
    operators = data[-1]

    if operators[i] == ' ':
        continue
    
    next_i = len(data[0])
    m_rem = '*' in operators[i+1:]
    p_rem = '+' in operators[i+1:]
    if m_rem and p_rem:
        next_i = min(operators[i+1:].index('*'), operators[i+1:].index('+'))+i
    elif m_rem:
        next_i = operators[i+1:].index('*')+i
    elif p_rem:
        next_i = operators[i+1:].index('+')+i
    
    nums = []
    for j in range(i, next_i):
        nums.append(int(''.join([data[x][j] for x in range(len(data)-1)])))
    
    print(nums)

    if operators[i] == '*':
        result = 1
        for x in nums: result *= x
    if operators[i] == '+':
        result = 0
        for x in nums: result += x
    solutions.append(result)

# print(solutions)
print(sum(solutions))