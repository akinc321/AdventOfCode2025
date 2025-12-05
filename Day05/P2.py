with open("Day05/input.txt", "r") as file:
    txt= file.read()
with open("Day05/test_input.txt", "r") as file:
    test_txt= file.read()

data = txt.split('\n')
test_data = test_txt.split('\n')

ranges = []
eats = []

for line in data:
    if '-' in line:
        split_ind = line.index('-')
        ranges.append((int(line[:split_ind]), int(line[split_ind+1:])))
    elif len(line)!=0:
        eats.append(int(line))

ranges.sort(key=lambda x: x[0])

fresh = set()
while True:
    temp = []
    
    # print(len(ranges))
    # print(ranges)

    #boolean to keep track of already compressed elements
    compressed = False
    for i in range(len(ranges)):
        if compressed:
            compressed = False
            continue
        # check if we can test the element after without going OoB
        if i+1 != len(ranges):
            ran = ranges[i]
            next = ranges[i+1]
            if ran[1]+1 >= next[0]:
                temp.append((ran[0], max(ran[1], next[1])))
                # print("comp", (ran[0], max(ran[1], next[1])))
                compressed = True
            else:
                temp.append(ran)
                # print("cont", ran)
        else:
            temp.append(ranges[i])
    # check to see if nothing compressed - if so, exit loop
    if len(ranges) == len(temp):
        break
    ranges = temp

print(sum([x[1]-x[0]+1 for x in ranges]))