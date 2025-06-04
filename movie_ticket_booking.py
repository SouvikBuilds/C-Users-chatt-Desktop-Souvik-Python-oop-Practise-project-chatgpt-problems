import random
import string
from prettytable import PrettyTable


class GenerateBookingID:
    def generate_booking_id():
        prefix = "BK"
        suffix = "".join(random.choices(string.digits, k =12))
        return f"BOOKING ID: {prefix}{suffix}"

class GenerateCaptcha:
    def generate_captcha():
        a = random.randint(1,5)
        b = random.randint(2,8)
        return {
            "Question": f"What is Ans of {a} X {b}: ",
            "a": a,
            "b": b
        }

print("Welcome To Ticket Booking App ! ")
book_tickets = []
last_checked_movie = 0
last_checked_class = 0
last_checked_seat = 0
last_checked_price = 0

username = input("Enter Your Name: ").strip().capitalize()


if len(username) == 0:
    raise PermissionError("Name Section Can't Be Empty")
elif username.isdigit():
    raise ValueError("Name Can't Be Digits")
country_code = "+91"
contact = input("Enter 10 digit Mobile Number: ")
if len(contact) != 10:
    raise ValueError("Contact Can't Be more or less than 10 digits")
elif len(contact) == 0:
    raise PermissionError("Contact Section Can't Be Empty")

print(f"Contact Details: {country_code}{contact}")
captcha = GenerateCaptcha.generate_captcha()
print(captcha["Question"])
userans = int(input("Enter Ans: "))
if userans == captcha["a"]*captcha["b"]:
    print("You Are Human")
    while True:
        try:
            opt = {
                1: "View Now Showing Movies",
                2: "View Seat Layout & Availability & Prices",
                3: "Book a Ticket & Cancel Booking",
                4: "View My Bookings",
                5: "Apply Discount/Coupon Code",
                6: "Make Payment",
                7: "Exit"
            }
            print("\n**************************************")
            print("...MOVIE TICKET BOOKING MENU...")
            print("\n**************************************")

            for k,v in opt.items():
                print(f"{k}.{v}")


            print("\n_______________________________________")

            x =  int(input("Enter Choices(1-7): "))
            match x:
                case 1:
                    my_table = PrettyTable(["Sl.","Movie Name","Language","Genre","Duration","Certification"])
                    
                    my_table.add_row(["1","Avengers: Endgame","English","Action,sci-fi","3h 2m","U/A"])
                    my_table.add_row(["2","Pushpa: The Rule","Telegu","Action,Drama","2h 45m","A"])
                    my_table.add_row(["3","Jawaan","Hindi","Action,Thriller","2h 30m","U/A"])
                    my_table.add_row(["4","Spiderman: No-way-Home","English","SuperHero","2h 28m","U"])
                    
                    print(my_table)
                    print("\n____________")
                    user_choice = int(input("Enter (1-4) To View Showtime...."))
                    if user_choice == 1:
                        print("1. Avengers: Endgame")
                        print("\n_____________")
                        print("Theatre: INOX South City,Kolkata")
                        print('''Screen 1
                        - 10:00 AM
                        - 01:30 PM
                        - 06:30 PM
                        - 09:45 PM''')
                        print("\n")
                        print("Theatre: PVR Bengal Plaza, Kolkata")
                        print('''Screen 3:
                        - 11:15 AM
                        - 03:45 PM
                        - 07:00 PM''')
                    elif user_choice == 2:
                        print("\n_________________")
                        print("2. Pushpa: The Rule")
                        print("\n_________________")
                        print("Theatre: Cinepolis Acropolis, Kolkata")
                        print('''Screen 2
                        - 9:30 AM
                        - 12:45 PM
                        - 5:00 PM
                        - 8:30 PM''')
                        print("\n")
                        print("Theatre: INOX South City, Kolkata")
                        print('''Screen 3:
                        - 10:15 AM
                        - 2:00 PM
                        - 6:00 PM
                        - 9:15 PM''')
                    elif user_choice == 3:
                        print("\n_________________")
                        print("3. Jawaan")
                        print("\n_________________")
                        print("Theatre: INOX South City, Kolkata")
                        print(''' Screen 2:
                        - 10:30 AM
                        - 1:45 PM
                        - 5:30 PM
                        - 8:45 PM''')
                        print("Theatre: Cinepolis Acropolis, Kolkata")
                        print(''' Screen 4:
                        - 10:45 AM
                        - 3:15 PM
                        - 6:45 PM''')
                    elif user_choice == 4:
                        print("\n___________________")
                        print('4. Spiderman: No Way Home')
                        print("\n___________________")
                        print("Theatre: PVR Bengal Plaza, Kolkata")
                        print(''' Screen 1:
                        - 11:00 AM
                        - 2:30 PM
                        - 7:15 PM''')
                        print("Theatre: Cinepolis Acropolis, Kolkata")
                        print(''' Screen 3:
                        - 10:45 AM
                        - 3:15 PM
                        - 6:45 PM''')
                    else:
                        print("Invalid Choice")
                    print("\n__________________________")
                    print("Select showtime for booking.")
                    movie_number = int(input("Enter Movie Number: "))
                    showtime = input("Enter ShowTime (AM/PM): ").upper()
                    if movie_number == 1:
                        last_checked_movie = "Avengers: Endgame"
                        if showtime == "10:00 AM" or showtime == "01:30 PM" or showtime == "06:30 PM" or showtime == "09:45 PM":
                            print("Theatre: INOX South City,Kolkata| Screen: 1")
                        else:
                            print("Theatre: PVR Bengal Plaza, Kolkata| Screen: 3")
                    elif movie_number == 2:
                        last_checked_movie = "Pushpa: The Rule"
                        if showtime == "09:30 AM" or showtime == "12:45 PM" or showtime == "05:00 PM" or showtime == "08:30 PM":
                            print ("Theatre: Cinepolis Acropolis, Kolkata| Screen: 2")
                        else:
                            print("Theatre: INOX South City, Kolkata| Screen: 4")
                    elif movie_number == 3:
                        last_checked_movie = "Jawan"
                        if showtime == "10:30 AM" or showtime == "01:45 PM" or showtime == "05:30 PM" or showtime == "08:45 PM":
                            print("Theatre: INOX South City, Kolkata| Screen: 2")
                        else:
                            print("Theatre: Cinepolis Acropolis, Kolkata| Screen: 4")
                    elif movie_number == 4:
                        last_checked_movie = "Spiderman No Way Home"
                        if showtime == "11:00 AM" or showtime == "02:30 PM" or showtime == "07:15 PM":
                            print("Theatre: PVR Bengal Plaza, Kolkata| Screen: 1")
                        else:
                            print("Theatre: Cinepolis Acropolis, Kolkata| Screen: 3")
                    else:
                        print("Invalid Choice")
                case 2:
                    my_seats = PrettyTable(["Seat Category","Description","Price Range(₹)"])
                    
                    my_seats.add_row(["Classic","Basic seat, middle or back row","₹120 - ₹180"])
                    my_seats.add_row(["Premium","Better view, center location, soft cushion","₹200 - ₹300"])
                    my_seats.add_row(["Couple","Sofa-style double seat for couples","₹500 - ₹800"])
                    my_seats.add_row(["Gold","Ultra-premium experience (PVR Gold, etc.)","₹900 - ₹1500"])
                        
                        
                    print(my_seats)
                    user_class = input("Enter Class Of Seat: ").strip().capitalize()
                    if user_class == "Classic":
                        my_seats_seats = PrettyTable(["Seat ID","Seat No","Price"])
                        my_seats_seats.add_row(["C1","A1","₹150"])
                        my_seats_seats.add_row(["C2","A2","₹150"])
                        my_seats_seats.add_row(["C3","A3","₹150"])
                        
                        print(my_seats_seats)
                        user_seat_no = input("Enter Seat Number: ").strip().upper()
                        if user_seat_no == "A1":
                            last_checked_seat = "A1"
                            last_checked_class = "Classic"
                            last_checked_price = "₹150"
                            print("Seat ID: C1|Seat No: A1| Price: ₹150")
                        elif user_seat_no == "A2":
                            last_checked_seat = "A2"
                            last_checked_class = "Classic"
                            last_checked_price = "₹150"
                            print("Seat ID: C2|Seat No: A2| Price: ₹150")
                        elif user_seat_no == "A3":
                            last_checked_seat = "A3"
                            last_checked_class = "Classic"
                            last_checked_price = "₹150"
                            print("Seat ID: C3|Seat No: A3| Price: ₹150")
                        else:
                            print("Invalid Choice")
                            
                    elif user_class == "Premium":
                        my_seats_seats = PrettyTable(["Seat ID", "Seat No", "Price"])
                        my_seats_seats.add_row(["P1", "B1", "₹250"])
                        my_seats_seats.add_row(["P2", "B2", "₹250"])
                        my_seats_seats.add_row(["P3", "B3", "₹250"])
                        print(my_seats_seats)

                        user_seat_no = input("Enter Seat Number: ").strip().upper()
                        if user_seat_no == "B1":
                            last_checked_seat = "B1"
                            last_checked_class = "Premium"
                            last_checked_price = "₹250"
                            print("Seat ID: P1 | Seat No: B1 | Price: ₹250")
                        elif user_seat_no == "B2":
                            last_checked_seat = "B2"
                            last_checked_class = "Premium"
                            last_checked_price = "₹250"
                            print("Seat ID: P2 | Seat No: B2 | Price: ₹250")
                        elif user_seat_no == "B3":
                            last_checked_seat = "B3"
                            last_checked_class = "Premium"
                            last_checked_price = "₹250"
                            print("Seat ID: P3 | Seat No: B3 | Price: ₹250")
                        else:
                            print("Invalid Choice")

                    elif user_class == "Couple":
                        my_seats_seats = PrettyTable(["Seat ID", "Seat No", "Price"])
                        my_seats_seats.add_row(["CO1", "C1-C2", "₹500"])
                        my_seats_seats.add_row(["CO2", "C3-C4", "₹500"])
                        my_seats_seats.add_row(["CO3", "C5-C6", "₹500"])
                        print(my_seats_seats)

                        user_seat_no = input("Enter Seat Number (like C1-C2): ").strip().upper()
                        if user_seat_no == "C1-C2":
                            last_checked_seat = "C01"
                            last_checked_class = "Couple"
                            last_checked_price = "₹500"
                            print("Seat ID: CO1 | Seat No: C1-C2 | Price: ₹500")
                        elif user_seat_no == "C3-C4":
                            last_checked_seat = "C02"
                            last_checked_class = "Couple"
                            last_checked_price = "₹500"
                            print("Seat ID: CO2 | Seat No: C3-C4 | Price: ₹500")
                        elif user_seat_no == "C5-C6":
                            last_checked_seat = "C03"
                            last_checked_class = "Couple"
                            last_checked_price = "₹500"
                            print("Seat ID: CO3 | Seat No: C5-C6 | Price: ₹500")
                        else:
                            print("Invalid Choice")


                    elif user_class == "Gold":
                        my_seats_seats = PrettyTable(["Seat ID", "Seat No", "Price"])
                        my_seats_seats.add_row(["G1", "D1", "₹350"])
                        my_seats_seats.add_row(["G2", "D2", "₹350"])
                        my_seats_seats.add_row(["G3", "D3", "₹350"])
                        print(my_seats_seats)

                        user_seat_no = input("Enter Seat Number: ").strip().upper()
                        if user_seat_no == "D1":
                            last_checked_seat = "G1"
                            last_checked_class = "Gold"
                            last_checked_price = "₹350"
                            print("Seat ID: G1 | Seat No: D1 | Price: ₹350")
                        elif user_seat_no == "D2":
                            last_checked_seat = "G1"
                            last_checked_class = "Gold"
                            last_checked_price = "₹350"
                            print("Seat ID: G2 | Seat No: D2 | Price: ₹350")
                        elif user_seat_no == "D3":
                            last_checked_seat = "G1"
                            last_checked_class = "Gold"
                            last_checked_price = "₹350"
                            print("Seat ID: G3 | Seat No: D3 | Price: ₹350")
                        else:
                            print("Invalid Choice")

                    else:
                        print("Invalid Class")
                case 3:
                    choice = int(input("Enter 1 For Booking And 2 For Cancel Booking."))
                    if choice == 1:
                        if last_checked_movie and last_checked_class and last_checked_seat and last_checked_price:
                            ticket = {
                                "Booking-ID": GenerateBookingID.generate_booking_id(),
                                "Name": username,
                                "Contact": contact,
                                "Movie": last_checked_movie,
                                "Class": last_checked_class,
                                "Seat": last_checked_seat,
                                "Price": last_checked_price
                            }
                            book_tickets.append(ticket)
                        else:
                            print("Please check seat availability first before booking.")
                    elif choice == 2:
                        to_cancel = input("Enter Seat No or Booking ID to cancel: ").strip().upper()
                        found = False
                        for ticket in book_tickets:
                            if ticket["SeatNo"] == to_cancel or ticket["BookingID"] == to_cancel:
                                book_tickets.remove(ticket)
                                print("Booking Cancelled.")
                                found = True
                                break
                        if not found:
                            print("No matching booking found.")

                case 4:
                    if not book_tickets:
                        print("❌ No bookings found.")
                    else:
                        print("\n✅ Your Booked Tickets:")
                        view_bookings = PrettyTable(["Movie", "Class", "Seat ID", "Seat No", "Price"])
                        for ticket in book_tickets:
                            view_bookings.add_row(ticket)
                        print(view_bookings)


                case 5:
                    if not book_tickets:
                        print("❌ You must book at least one ticket to apply a discount.")
                    else:
                        coupon = input("🎟️ Enter Coupon Code (e.g., SAVE20): ").strip().upper()
                        valid_coupons = {"SAVE20": 0.20, "FLAT50": 50}  # flat or percentage
                        if coupon in valid_coupons:
                            if isinstance(valid_coupons[coupon], float):
                                discount_percent = valid_coupons[coupon]
                                total = sum(int(ticket[4][1:]) for ticket in book_tickets)
                                discount_amount = total * discount_percent
                                total -= discount_amount
                                print(f"✅ {int(discount_percent*100)}% Discount Applied. New Total: ₹{int(total)}")
                            else:
                                discount_flat = valid_coupons[coupon]
                                total = sum(int(ticket[4][1:]) for ticket in book_tickets)
                                total -= discount_flat
                                print(f"✅ ₹{discount_flat} Discount Applied. New Total: ₹{int(total)}")
                        else:
                            print("❌ Invalid Coupon Code.")


                case 6:
                    if not book_tickets:
                        print("❌ No tickets booked to make a payment.")
                    else:
                        total_amount = sum(int(ticket[4][1:]) for ticket in book_tickets)
                        print(f"💰 Total Amount Due: ₹{total_amount}")
                        confirm = input("Proceed to Payment? (yes/no): ").strip().lower()
                        if confirm == "yes":
                            print("✅ Payment Successful! Enjoy your movie 🎬🍿")
                            book_tickets.clear()  
                        else:
                            print("❌ Payment Cancelled.")

                case 7:
                    print("👋 Thank you for using Movie Booking System. See you again!")
                    break
                    
                case _:
                    print("Invald Choice")
            
            stop = input("Do You Want to Stop (y/n): ").strip().lower()
            if stop == "y":
                break


                    
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Welcome")
else:
    print("ACCESS BLOCKED")