#String in loops
my_string="Rupesh"
for char in my_string:
    print(char)

#List in loops
City=['Sagar','Jabalpur','indore','Bhopal','Ujjain']
for i in City:
    print(i)

#Dictionary in loops
Marks={
    'Sidhdant': '95',
    'Rupesh':'67',
    'Yogesh':'87',
    'Durgesh':'92'
}
for key in Marks.keys():
    print(key)
for value in Marks.values():
    print(value)
for key,value in Marks.items():
    print(key,":",value)

