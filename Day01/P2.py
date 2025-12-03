with open("Day01/input.txt", "r") as file:
    txt= file.read()
with open("Day01/test_input.txt", "r") as file:
    test_txt= file.read()

txt=txt.replace("R","").replace("L","-")
data=[int(x) for x in txt.split("\n")]

test_txt=test_txt.replace("R", "").replace("L","-")
test_data=[int(x) for x in test_txt.split("\n")]

zed_count = 0
dial = 50
# print(abs(-1023)//100)
# print(abs(-1023)%100)
# print(-53%100)
# print(abs(110)//100)
# print(110%100)
# print(abs(-110)//100)
# print(-110%100)

# if -111 x=-11 z+=1
# if 111 x=11 z+=1
# f=-111
# print(abs(f)//100)
# print(f%100-100 if f<0 else f%100)

for x in data:
    # print(dial,x)
    #clean x to be within abs(100) range
    # and add the number of dial passes
    zed_count += abs(x)//100
    x = x%100-100 if x<0 else x%100
    if (dial + x <= 0 or dial + x >= 100) and dial != 0:
        zed_count += 1
        # print(dial+x, dial, x)
        # print(zed_count)
    dial += x
    dial %= 100
print(zed_count)