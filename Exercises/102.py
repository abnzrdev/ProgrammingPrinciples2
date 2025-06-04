#List Exercises
#  Finding the sum and the max of the numbers in the list
num = [20,45,34,53,9]
sum = 0
max = num[0]
for i in num:
    sum += i
    if i > max:
        max = i
print(sum)
print(max)

# Strings list
places = ["Italy", "Kazakhstan", "Ireland", "Finland", "Ethiopia"]
places[1] = "Updated"
for place in places:
    print(place)

names = ["Abenezer", "Alemayehu", "Lemma"]
for name in names:
    if name[0] == "A":
        print(name)


