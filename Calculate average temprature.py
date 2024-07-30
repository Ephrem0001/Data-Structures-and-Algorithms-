days = int(input("How many day's temperature? "))
temp = []
for i in range(days):
    temp.append(int(input(f"day {i}'s high temp: ")))
average = sum(temp)/days
print(f"Average = {average}")
j = 0
for i in range(days):
    if temp[i] > average:
        j = +1
print(f"{j} day(s) above average")
