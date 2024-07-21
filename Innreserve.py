# importing modules
import json
import os
from datetime import datetime
import time

# Stores th ebookings
BOOKINGS_FILE = 'bookings.json'


ROOM_CAPACITY = {
    "Single": 10,
    "Double": 5,
    "Suite": 3
}

# Room prices information
ROOM_PRICES = {
    "Single": 300,
    "Double": 550,
    "Suite": 700
}

#charges
TAX = 33
MAINTENANCE_CHARGE = 50

#Load bookings
def load_bookings():
    if os.path.exists(BOOKINGS_FILE):
        try:
            with open(BOOKINGS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading the bookings file.")
            return {}
    return {}

#Save bookings
def save_bookings(bookings):
    try:
        with open(BOOKINGS_FILE, 'w') as file:
            json.dump(bookings, file)
    except Exception as e:
        print(f"Error saving bookings: {e}")

#Check if the required number of rooms is available
def check_room_availability(bookings, room_type, num_rooms):
    booked_rooms = sum(1 for booking in bookings.values() if booking['room_type'] == room_type)
    return booked_rooms + num_rooms <= ROOM_CAPACITY[room_type]

#Calculate total cost
def calculate_total_cost(room_type, num_rooms, check_in_date, check_out_date):
    days_stay = (check_out_date - check_in_date).days
    if days_stay <= 0:
        raise ValueError("Check-out date must be after check-in date.")
    room_price = ROOM_PRICES[room_type]
    total_room_cost = room_price * num_rooms * days_stay
    total_tax = TAX * num_rooms * days_stay
    total_cost = total_room_cost + total_tax + MAINTENANCE_CHARGE
    return total_room_cost, total_tax, MAINTENANCE_CHARGE, total_cost

# Book a room
def book_room(bookings):
    print("Room Types: 1 = Single, 2 = Double, 3 = Suite")
    time.sleep(1)

    while True:
        room_choice = input("Which room type? (1/2/3): ")
        if room_choice in ["1", "2", "3"]:
            room_types = {"1": "Single", "2": "Double", "3": "Suite"}
            room_type = room_types[room_choice]
            break
        else:
            print("Enter a valid room type")
        time.sleep(1)

    while True:
        num_rooms = input("How many rooms do you want to book? ")
        if num_rooms.isdigit() and int(num_rooms) > 0:
            num_rooms = int(num_rooms)
            if check_room_availability(bookings, room_type, num_rooms):
                break
            else:
                print(f"Sorry, we don't have enough {room_type} rooms available!")
        else:
            print("Please enter a valid number of rooms.")
        time.sleep(1)

    while True:
        aadhar = input("What's your Aadhar number? ")
        if aadhar not in bookings:
            break
        else:
            print("A room is already booked with this Aadhar number!")
        time.sleep(1)

    while True:
        name = input("What's your name? ")
        if name.isalpha():
            break
        else:
            print("Please enter a valid name (letters only).")
        time.sleep(1)

    while True:
        phone = input("What's your phone number? ")
        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Please enter a valid 10-digit phone number.")
        time.sleep(1)

    while True:
        email = input("What's your email? ")
        if "@" in email and "." in email:
            break
        else:
            print("Please enter a valid email address.")
        time.sleep(1)

    while True:
        check_in = input("Enter check-in date (YYYY-MM-DD): ")
        check_out = input("Enter check-out date (YYYY-MM-DD): ")
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            if check_out_date <= check_in_date:
                print("Check-out date must be after check-in date!")
            elif check_in_date < datetime.today():
                print("Check-in date must be today or in the future!")
            else:
                break
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
        time.sleep(1)

    while True:
        password = input("Enter a password for your booking: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Please try again.")
        time.sleep(1)

    try:
        room_cost, tax, maintenance_charge, total_cost = calculate_total_cost(room_type, num_rooms, check_in_date, check_out_date)
    except ValueError as e:
        print(e)
        return

    booking_info = {
        "name": name,
        "phone": phone,
        "email": email,
        "room_type": room_type,
        "check_in": check_in,
        "check_out": check_out,
        "num_rooms": num_rooms,
        "room_cost": room_cost,
        "tax": tax,
        "maintenance_charge": maintenance_charge,
        "total_cost": total_cost,
        "password": password
    }

    bookings[aadhar] = booking_info
    save_bookings(bookings)
    print(f"Yay! Room(s) booked successfully!")
    print(f"Room Price: {room_cost}")
    print(f"Tax: {tax}")
    print(f"Maintenance Charge: {maintenance_charge}")
    print(f"Total Cost: {total_cost}")
    time.sleep(1)

# Cancel a room booking
def leave_room(bookings):
    aadhar = input("What's your Aadhar number? ")

    if aadhar in bookings:
        stored_password = bookings[aadhar]['password']
        # Verify the password for cancellation
        while True:
            password = input("Enter your password to confirm cancellation: ")
            if password == stored_password:
                break
            else:
                print("Incorrect password. Please try again.")
        confirm = input(f"Are you sure you want to leave the room(s) booked with Aadhar {aadhar}? (yes/no): ")
        if confirm.lower() == 'yes':
            del bookings[aadhar]
            save_bookings(bookings)
            print("Room(s) left successfully!")
        else:
            print("Okay, not leaving the room(s).")
    else:
        print("No booking found with this Aadhar number.")
    time.sleep(2)

# View all bookings
def view_bookings(bookings):
    password = "Eliteinn@2024"

    Authentication = input("Enter the password to view this page: ")
    if Authentication == password:
        pass
    else:
        print("Wrong password")
        user_exit()

    if bookings:
        for aadhar, info in bookings.items():
            print(f"Debug info for Aadhar {aadhar}: {info}")
            try:
                print(
                    f"Aadhar: {aadhar}, Name: {info['name']}, Phone: {info['phone']}, Email: {info['email']}, Room: {info['room_type']}, Check-in: {info['check_in']}, Check-out: {info['check_out']}, Room Price: {info['room_cost']}, Tax: {info['tax']}, Maintenance Charge: {info['maintenance_charge']}, Total Cost: {info['total_cost']}")
            except KeyError as e:
                print(f"Missing information in booking: {e}")
    else:
        print("No bookings available.")
    time.sleep(2)

# View room prices
def view_prices(bookings):
    print("Single : 300/day")
    print("Double : 550/day")
    print("Suite  : 700/day")
    time.sleep(2)

# Exit the application
def user_exit():
    print("Thanks! Have a good day")
    exit()

# Main function to run the application
def main():
    bookings = load_bookings()
    while True:
        print("\nWelcome to SRVS Hotel")
        print("1. Book a room")
        print("2. Leave a room")
        print("3. View bookings")
        print("4. Price Details")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            book_room(bookings)
        elif choice == "2":
            leave_room(bookings)
        elif choice == "3":
            view_bookings(bookings)
        elif choice == "4":
            view_prices(bookings)
        elif choice == "5":
            user_exit()
            break
        else:
            print("Oops! Please enter a valid choice.")

if __name__ == '__main__':
    main()
