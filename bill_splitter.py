class Person:
    
    @staticmethod
    def get_name():
        name = input("Enter Name: ")
        if name.isdigit():
            raise ValueError("Name Can't Be Digits")
        elif len(name) == 0:
            raise ValueError("Name Section Can't Be Empty")
        return name
    
    @staticmethod
    def get_amount_paid():
        amount_paid = float(input("Enter Amount Paid: "))
        if amount_paid <= 0:
            raise ValueError("Amount Paid Can't Be 0 or Negative")
        elif len(str(amount_paid)) == 0:
            raise ValueError("Amount Paid Section Can't Be Empty")
        return amount_paid
    
        
class Bill:
    
    @staticmethod
    def get_total_bill():
        total_bill = float(input("Enter Total Bill: "))
        if total_bill <= 0:
            raise ValueError("Total Bill Can't Be 0 or Negative")
        elif len(str(total_bill)) == 0:
            raise ValueError("Total Bill Section Can't Be Empty")
        
        return total_bill
    
    @staticmethod
    def get_tip_percentage():
        tip_percentage = float(input("Enter Tip Percentage(0 For None): "))
        
        return tip_percentage
    
    @staticmethod
    def calculate_final_bill():
        
        total_bill = Bill.get_total_bill()
        tip_percentage = Bill.get_tip_percentage()
        final_bill = total_bill + (total_bill*tip_percentage)/100
        
        print(f"Final bill With Tip: ₹{final_bill}")
        return final_bill
    
people = []
class Splitter:
    
    @staticmethod
    def add_person():
        global people
        n = int(input("Enter Total Number Of Persons: "))
        for i in range(n):
            name = Person.get_name()
            amount_paid = Person.get_amount_paid()
            
            people.append([name,amount_paid])
            
        print(f"✅ {n} people added successfully")
    
    
    @staticmethod
    def calculate_share():
        global people
        
        get_bill = Bill.calculate_final_bill()
        n = len(people)
        share = get_bill / n
        
        return share
    

    
    @staticmethod
    def show_dues():
        print("\nDue Summary: \n")
        from prettytable import PrettyTable

        my_due = PrettyTable(["Name", "Paid(₹)", "Should Pay", "Status"])

        share = Splitter.calculate_share()

        for person in people:
            name, paid = person
            due = paid - share
            status = f"Gets ₹{abs(due):.2f}" if due > 0 else f"Pays ₹{abs(due):.2f}" if due < 0 else "Settled"
            my_due.add_row([name, f"₹{paid:.2f}", f"₹{share:.2f}", status])

        print(my_due)
    
        
class Menu:
    
    @staticmethod
    def get_menu():
        opt = {
            1: "Add Person",
            2: "Enter Total Bill",
            3: "View Dues",
            4: "Exit"
        }

        print("...MENU...")
        for k,v in opt.items():
            print (f"{k}:{v}")
        
while True:     

    Menu.get_menu()
    try:        
        userchoice = int(input("Enter Choice: "))
        if userchoice == 1:
            Splitter.add_person()
        elif userchoice == 2:
            Bill.calculate_final_bill()
        elif userchoice == 3:
            Splitter.show_dues()
        elif userchoice == 4:
            print("Exit...Goodbye")
        elif userchoice == 5:
            print("Invalid Choice")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
    
    stop = int(input("Enter 0 to exit and 1 to continue: "))
    if stop == 0:
        break
    