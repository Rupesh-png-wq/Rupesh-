with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "r") as f:
    f.seek(5)
    print(f.read())

    f.seek(0)
    print(f.read())

    