"""
total = 0。0
count = 0

filename = "score.txt"
open and read the file
for line in file
     score = float(line)
     total += score
     count += 1
     display score ,total
close file
average = total / count
display average

"""
total = 0.0
count = 0

filename = "scores.txt"
in_file = open(filename, 'r')
for line in in_file:
    score = float(line)
    total += score
    count += 1
    print(f"Score = {score:4.1f}   Total so far = {total:6.1f}")
in_file.close()
average = total / count
print(f"Average = {average:.1f}")