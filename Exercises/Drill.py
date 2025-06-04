# Write a program that outputs all even numbers from 2 to 20
for i in range(2,21):
    if(i % 2 == 0):
        print(i)

#Write a program to find the sum of the numbers upto 50
total = 0
for i in range(51):
    total += i

print(total)

# Password Checker
inp = input("Enter your password")
while(inp != "admin123"):
    inp = input("Enter your password : ")

print("Correct Password")