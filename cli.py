
from helpers import (
    exit_program,
    list_trips,
    find_trip_by_name,
    find_trip_by_id,
    create_trip,
    update_trip,
    delete_trip,
    get_duration,
    get_description,
    get_destinations,
    add_destination,
    find_destination_by_name,
    find_destination_by_id,
    delete_destination,
    update_destination,
    get_accommodations,
    list_destinations
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_trips()
        elif choice == "2":
            find_trip_by_name()
        elif choice == "3":
            find_trip_by_id()
        elif choice == "4":
            get_description()
        elif choice == "5":
            get_duration()
        elif choice == "6":
            get_destinations()
        elif choice == "7":
            create_trip()
        elif choice == "8":
            update_trip()
        elif choice == "9":
            delete_trip()
        elif choice == "10":
            list_destinations()
        elif choice == "11":
            add_destination()
        elif choice == "12":
            find_destination_by_name()
        elif choice == "13":
            find_destination_by_id()
        elif choice == "14":
            get_accommodations()
        elif choice == "15":
            update_destination()
        elif choice == "16":
            delete_destination()
        else:
            print("Invalid choice")


def menu():
    print("")
    print("*Welcome to the travel itinerary organizer!*")
    print("")
    print("********Trips********")
    print("Please select an option:")
    print("0. Exit program")
    print("1. List all available trips")
    print("2. Find a trip by it's name")
    print("3. Find a trip by it's id")
    print("4: Get a trip's description")
    print("5: Get a trip's duration")
    print("6: Get a trip's all destinations")
    print("7: Create a new trip")
    print("8: Update an existing trip")
    print("9: Delete an existing trip")
    print("")
    print("*****Destinations*****")
    print("10: List all available destinations")
    print("11: Add a new destination")
    print("12. Find a destination by it's name")
    print("13. Find a destination by it's id")
    print("14: Get a destination's all accommodations")
    print("15: Update an existing destination")
    print("16: Delete an existing destination")
    
    


if __name__ == "__main__":
    main()