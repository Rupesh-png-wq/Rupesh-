#List slicing
Numbers = [1,2,3,4,5,6,7,8,9]
print("First three element:",Numbers[:3])
print("Last three element:",Numbers[-3:])
print("Middle element:",Numbers[2:6])

#List manipulation
Numbers.append(10)
print(Numbers)
Numbers.insert(1,15)
print(Numbers)
Numbers.extend([12,14])
print(Numbers)
Numbers.sort()
print(Numbers)
Numbers.reverse()
print(Numbers)
print(Numbers.count(2))


