numbers = []
i = 1
while i < 16:
    i += 1
    if i == 5:
        continue
    if i == 7:
        continue
    if i == 9:
        continue
    if i == 10:
        continue
    if i == 11:
        continue
    if i == 13:
        continue
    if i == 14:
        continue
    if i == 15:
        continue
    if i == 16:
         continue
    numbers.append(i)
for number in numbers:
    print (number, end="," )
    if number == 12:
        print (16, end="")