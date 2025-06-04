# Write a program that outputs all even numbers from 2 to 20
i = 2
while i < 21:
    if(i % 2 == 0):
        print(i)
    i += 1;

#Write a program to find the sum of the numbers upto 50
total = 0
i = 1
while i < 51:
    total += i
    i += 1

print(total)

# Password Checker
inp = input("Enter your password")
while(inp != "admin123"):
    inp = input("Enter your password : ")

print("Correct Password")


# For loop Exercises
for i in range (1,11):
    print(f'{i} * {i} = {i * i}')

MyWords = ["hello","abenezer","alemayehu","perseverance","shewa"]
for word in MyWords:
    print(len(word))

# Multiplication table exercises
for i in range(6):
    for j in range(6):
        print(f'{i} * {j} = {i * j}')