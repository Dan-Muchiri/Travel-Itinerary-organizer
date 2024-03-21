
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
    get_destinations
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
        
        
        else:
            print("Invalid choice")


def menu():
    print("")
    print("Welcome to the trip itinerary organizer!")
    print("")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all available trips")
    print("2. Find a trip by it's name")
    print("3. Find a trip by it's id")
    print("4: Get a trip's description")
    print("5: Get a trip's duration")
    print("6: Get a trip's destinations")
    print("7: Create a new trip")
    print("8: Update an existing trip")
    print("9: Delete an existing trip")
    


if __name__ == "__main__":
    main()