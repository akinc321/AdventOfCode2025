with open("Day03/input.txt", "r") as file:
    txt= file.read()
with open("Day03/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split("\n")
test_data = test_txt.split("\n")

joltage = []

for dat in data:
    dirty_dozen = []
    for i in range(len(dat)):
        dit = int(dat[i])
        if len(dirty_dozen) == 0:
            dirty_dozen.append(dit)
            continue
        # check to see if remaining numbers left make 12 in length added to dirty_dozen
        # skip sorting code to add all remaining numbers
        remaining = len(dat)-i
        if len(dirty_dozen)+remaining == 12:
            dirty_dozen.append(dit)
            continue
        # sort next number into highest spot based on size
        sorted = False
        for j in range(len(dirty_dozen)):
            current = dirty_dozen[j]
            # make sure number can be sorted without deleting needed numbers
            if remaining+j < 12:
                continue
            if dit > current:
                dirty_dozen = dirty_dozen[:j]
                dirty_dozen.append(dit)
                sorted = True
                break
            pass
        if not sorted and len(dirty_dozen) != 12:
            dirty_dozen.append(dit)
        


    joltage.append(int(''.join([str(x) for x in dirty_dozen])))

# print(joltage)
print(sum(joltage))