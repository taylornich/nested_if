# question 2 task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# question 2 task 2

extras = "audio system and projector" if attendees > 100 else "projector"
print(extras)

# question 2 task 3

food = input("Would you like vegetarian food?")
caterer = "Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(caterer)