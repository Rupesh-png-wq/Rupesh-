with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "r") as f:
    data = f.read()
   # print(data)

with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line=f.readlines()

    print(line1)
    print(line2)
    print(line)
