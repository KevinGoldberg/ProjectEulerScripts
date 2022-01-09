#Problem13

with open("100_fifty_digit_numbers.txt") as infile:
    sum = 0
    for line in infile:
        sum = sum + int(line)
print(sum)
