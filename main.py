from functions import *

print("What would you like to do?")
print("1 -- Search all films")
print("2 -- Search all people")
print("3 -- Search all vehicles")
user_input = input("Enter Option Number ")
if user_input.isalpha():
    print("not a valid option.")
else:
    if int(user_input) == 1:
        print("All the films: ")
        choosen_results(film_url, 'title', 26)
        filter_by_film()
    elif int(user_input) == 2:
        print("All the characters: ")
        choosen_results(people_url, 'name', 27)
        filter_by_person()
    elif int(user_input) == 3:
        print("All the vehicles: ")
        choosen_results(vehicles_url, 'name', 29)
        filter_by_vehicle()
    else:
        print("not a valid option.")
