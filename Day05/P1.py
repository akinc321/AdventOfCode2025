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

count = 0
for bite in eats:
    for range in ranges:
        if range[0] <= bite <= range[1]:
            count+=1
            break

print(count)