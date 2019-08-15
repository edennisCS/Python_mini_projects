# calculate movie discount based on the price and the number of people
movie = input("enter movie price rounded to nearest £ ")
people = input("enter number of people ")
discount = int(people) / int(movie)

percent = discount * 100
if percent > 70:
    percent = 70

print("discount is: " ,percent, "%")
