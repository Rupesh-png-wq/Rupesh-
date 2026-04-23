#Continue
i = 1
while i <= 5:
    if i % 2 == 0:
        i += 1
        continue  # skip even numbers
    print(i)
    i += 1

#Break
i=1
while i<=10:
    if(i==3):
        i+=1
        break # stop
    print(i)
    i+=1   

#pass
for i in range(5):
    if(i==3):
        pass # Do nothing
    else:
        print(i)
