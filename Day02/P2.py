with open("Day02/input.txt", "r") as file:
    txt= file.read()
with open("Day02/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split(",")
test_data = test_txt.split(",")

data = [(int(x[:x.index("-")]), int(x[x.index("-")+1:])) for x in data]
test_data = [(int(x[:x.index("-")]), int(x[x.index("-")+1:])) for x in test_data]

#need a splitting formula using a divisionary modulus

def is_repeating(num):
    snum = str(num)
    # a single digit can't repeat
    if len(snum) == 1:
        return False
    # all the same number
    if len(set(list(snum)))==1:
        return True
    for i in range(2,len(snum)//2+1):
        if len(snum)%i==0:
            #split string into even i length parts and throw into a set to check length of 1
            if len(set(list(map(''.join, zip(*[iter(snum)]*i)))))==1:
                return True

doubles=[]
for dat in data:
    for x in range(dat[0],dat[1]+1):
        if is_repeating(x):
            # print(x)
            doubles.append(x)

# print(doubles)
total = sum(doubles)
print(total)