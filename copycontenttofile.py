with open("C:/Users/rupes/OneDrive/Desktop/pyhton/Mydata.txt","r") as src:
    with open("C:/Users/rupes/OneDrive/Desktop/pyhton/source.txt","w") as dest:
        content=src.read()
        dest.write(content)
print("content copy successfully")        

