with open("Day02/input.txt", "r") as file:
    txt= file.read()
with open("Day02/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split(",")
test_data = test_txt.split(",")

data = [(x[:x.index("-")], x[x.index("-")+1:]) for x in data]
test_data = [(x[:x.index("-")], x[x.index("-")+1:]) for x in test_data]
print(int(data[1][0][:len(data[1][0])//2]))
def clean_data(array):
    temp = []
    for x in array:
        bot = x[0]
        if len(bot)%2==1:
            bot = "1"+"0"*len(bot)
        top = x[1]
        if len(top)%2==1:
            top = "9"+"9"*(len(top)-2)
        temp.append((int(bot[:len(bot)//2]), int(bot[len(bot)//2:]), int(top[:len(top)//2]), int(top[len(top)//2:])))
    return temp

data = clean_data(data)
test_data = clean_data(test_data)

doubles=[]
for dat in data:
    print(dat)
    if dat[0]>dat[2]:
        continue
    # if top half of lower range equals top half of higher range,
    #  check bottom half of higher range
    if dat[0]==dat[2]:
        if dat[0]>=dat[1] and dat[2]<=dat[3]:
            doubles.append(dat[0])
            # print(dat[0],"v")
    elif dat[0]>=dat[1]:
        doubles.append(dat[0])
        # print(dat[0],"v")
    if dat[2]<=dat[3] and dat[0]!=dat[2]:
        doubles.append(dat[2])
        # print(dat[2],"^")
    for i in range(dat[0]+1,dat[2]):
        doubles.append(i)
        # print(i)

# print(doubles)
total = sum([int(str(x)+str(x)) for x in doubles])
print(total)