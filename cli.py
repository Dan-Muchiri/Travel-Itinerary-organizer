
from helpers import (
    exit_program,
    list_trips,
    find_trip_by_name,
    find_trip_by_id,
    create_trip,
    update_trip,
    delete_trip
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
            create_trip()
        elif choice == "5":
            update_trip()
        elif choice == "6":
            delete_trip()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all trips")
    print("2. Find trip by name")
    print("3. Find trip by id")
    print("4: Create trip")
    print("5: Update trip")
    print("6: Delete trip")


if __name__ == "__main__":
    main()