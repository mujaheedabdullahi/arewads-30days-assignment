
# Day 3 Assignment 

# Question 1
age = 19

# Question 2 
height = float(174)

# Question 3
c_number = complex(3, 4)

# Question 4
print("Area of the triangle:", int(input('Base: ')) * int(input('Height: ')))

# Question 5
print("Perimeter of the triangle:", int(input('a: ')) + int(input('b: ')) + int(input('c: ')))

# Question 6
length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('Area: ', length * width)
print('Perimeter: ', 2 * (length + width))

# Question 7
radius = int(input('Enter radius: '))
print('Area: ', 3.14 * radius * radius)
print('Circumference: ', 2 * 3.14 * radius)

# Question 8
print("X intercept: ", 1)
print("Y intercept: ", -2)
print("Slope: ", 2)

# Question 9
x1, x2, y1, y2 = 2, 6, 2, 10
print('Distance: ')
print('{0:.2f}'.format(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
print('Slope:')
print((y2 - y1) / (x2 - x1))

# Question 10
print(2 if 2 < (y2 - y1) / (x2 - x1) else (y2 - y1) / (x2 - x1))

# Question 11
for x in range(0, 10):
    print(x ** 2 + 6 * x + 9)
print(3, -3, "is where y is 0")

# Question 12
print(not len('python') == len('dragon'))

# Question 13
print('on' in 'python' and 'on' in 'dragon')

# Question 14
print('jargon' in "I hope this course is not full of jargon")

# Question 15
print('on' not in 'python' and 'on' in 'dragon')

# Question 16
print(str(float(len('python'))))

# Question 18
number = int(input('Enter number:'))
print("Even" if number % 2 == 0 else "Odd")

# Question 19
print(type('10') == type(10))

# Question 20
print(int('9.8') == 10)

# Question 21
hours = int(input('Enter hours:'))
rph = int(input('Enter rate per hour:'))
print("Weekly Earning:", hours * rph)

# Question 22
years = int(input('Enter years:'))
print(years * 365 * 24 * 60 * 60 * 60)

# Question 23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)