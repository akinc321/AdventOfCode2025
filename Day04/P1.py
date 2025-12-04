with open("Day04/input.txt", "r") as file:
    txt= file.read()
with open("Day04/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split('\n')
test_data = test_txt.split('\n')

def adjacent_rolls(arr, y, x):
    adj = 0
    for i in range(-1,2):
        t=''
        for j in range(-1,2):
            if y+i >= 0 and y+i < len(arr) and x+j >= 0 and x+j < len(arr[i]):
                if i == 0 and j == 0:
                    t+='X'
                    continue
                
                t+= arr[y+i][x+j]
                if arr[y+i][x+j] == "@":
                    adj+=1
        # print(t)
    # print("adj",adj)
    return adj
                     
            
count = 0
# test data quick swap code V
# data = test_data
for i in range(len(data)):
    dat = data[i]
    for j in range(len(dat)):
        d = dat[j]
        if adjacent_rolls(data, i, j) < 4 and data[i][j] == '@':
            count+=1
            

print(count)