# ---------------- Q111: Ticket Booking System ----------------
print("\n--- Q111: Ticket Booking System ---")

show_name = "Movie A"
total_seats = 10
booked_seats = 3
ticket_price = 150

# Calculate available seats
available_seats = total_seats - booked_seats

print("Show Name:", show_name)
print("Available Seats:", available_seats)
print("Ticket Price: Rs", ticket_price)

# Book one ticket
booked_seats = booked_seats + 1
available_seats = total_seats - booked_seats

print("\n1 Ticket Booked Successfully!")
print("Remaining Seats:", available_seats)