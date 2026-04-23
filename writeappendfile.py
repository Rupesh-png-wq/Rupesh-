with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "w") as f:#truncate entire the file
    f.write("This is a new line\n")

with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "r") as f:
    print(f.read())

with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "a") as f:#add at thr last of the file
   f.write("python is a very easy programming language")

with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt", "r") as f:
    print(f.read())