with open("Day03/input.txt", "r") as file:
    txt= file.read()
with open("Day03/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split("\n")
test_data = test_txt.split("\n")

joltage = []

for dat in data:
    first = 0
    second = 0
    highest = 0
    for i in range(len(dat)):
        dit = int(dat[i])
        swap = False
        if dit > first and i != len(dat)-1:
            first = dit
            second = 0
            swap = True
        if dit > second and not swap:
            second = dit

    joltage.append(int(str(first)+str(second)))

print(joltage)
print(sum(joltage))