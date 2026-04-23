#variable assignment
a=10
b=5
print("Before Swapping:")
print("a=",a)
print("b=",b)
#without using temp variable
a,b = b,a
print("After Swapping")
print("a=",a)
print("b=",b)

#using temp variable
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)
