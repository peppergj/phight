with open ("level.txt", "r") as data:
    lines = [x.strip("\n") for x in data.readlines()]

for line in lines: 
    numbers =  line.split(" ")
    array = []
    for numb in numbers:
        n = int(numb)
        print(n + 1)
        array.append(n)
    print(array)