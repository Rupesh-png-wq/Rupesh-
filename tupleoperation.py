#Tuple operation
#concatination
tuple1=(1,2,3)
tuple2=(4,5,6)
result=tuple1+tuple2
print(result)

#tuple repetation
repeated=tuple1*3
print(repeated)

#membership
print(2 in tuple1)
print(6 in tuple1)

#Slicing
print(tuple1[1:1])
print(tuple1[1:])
print(tuple1[:2])

#Immutabilitie
#tuple1.append(8)
#print(tuple1)