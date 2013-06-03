# i variable assigned 0
i = 0
# No numbers in list
numbers = []

# i less then 6
while i < 6:
    print "At the top i is %d" % i
    
# Add onto numbers list
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
