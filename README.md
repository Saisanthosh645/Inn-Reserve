# Inn-Reserve
The "SRVS" project is a Python-based hotel management system designed to facilitate room bookings, cancellations, and viewing of room details and prices. The system uses a JSON file to store booking information and handles various user interactions through a command-line interface.

Technologies and Libraries Used
Python: The programming language used to develop the application.
JSON: Used for storing and managing booking data in a file (bookings.json).
Datetime: For handling date operations such as check-in and check-out dates.
OS: To check the existence of the bookings file and handle file operations.
Time: To add delays and make user interactions more manageable.
Key Features
Room Booking: Users can book rooms by selecting room type (Single, Double, Suite), specifying the number of rooms, and providing personal details. The system checks for room availability and calculates the total cost, including room charges, tax, and maintenance fees.

Room Cancellation: Users can cancel their bookings by providing their Aadhar number and password. The system verifies the password before proceeding with the cancellation.

View Bookings: Authorized users can view all bookings by entering a password. This feature displays detailed information about each booking.

View Prices: Users can view the prices for different room types.

File Management: Bookings are stored in a JSON file, allowing for easy data management and retrieval.
