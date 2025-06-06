import qrcode
import random
from prettytable import PrettyTable

class Item:
    @staticmethod
    def get_name():
        name = input("Enter Name of Product: ").strip().capitalize()
        if len(name) == 0:
            raise ValueError("Name Can't Be Empty")
        
        return name
    
    @staticmethod
    def get_Price():
        price = float(input("Enter Price/KG: "))
        if price <= 0:
            raise ValueError("Price Can't Be Negative or 0")
        
        return price
    
    @staticmethod
    def get_quantity():
        quantity = float(input("Enter Quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity Can't Be Negative or 0")
        
        return quantity

ordered_items = []
total_cost = 0
    
class Cart:
    
    @staticmethod
    def add_items():
        global ordered_items
        global total_cost
        n = int(input("Enter Total Items To be Added: "))
        if n <= 0:
            raise ValueError("No of Items Can't Be Negative or 0")
        elif "." in str(n):
            raise ValueError("No of Items Can't Be Decimal")
        
        for i in range(n):
            name = Item.get_name()
            quantity = Item.get_quantity()
            price_kg = Item.get_Price()
            
            total_bill = quantity*price_kg
            
            ordered_items.append([name,quantity,total_bill])
            print(ordered_items)
            
                
            total_cost += total_bill
            
            print(f"Current Total Cost: ₹{total_cost}")
                


    
    @staticmethod
    def remove_items():
        global ordered_items
        global total_cost
        n = int(input("Enter Number Of Items To Be Removed: "))
        if n <= 0:
            raise ValueError("No of Items Can't Be Negative or 0")
        elif "." in str(n):
            raise ValueError("No of Items Can't Be Decimal")
        is_found = False
        for i in range(n):
            name_to_delete = input(f"Enter name of item {i+1}: ").strip().capitalize()
            for item in ordered_items:
                if name_to_delete == item[0]:
                    ordered_items.remove(item)
                    print(ordered_items)
                    
                    total_cost -= item[2]
                    
                    print(f"Current Total Cost is: ₹{total_cost}")
                    is_found = True
                    break
            else:
                print(f"{name_to_delete} not found")
    
    @staticmethod
    def exit_system():
        print("...EXIT...")


class User:
    
    
    @staticmethod
    def get_name():
        print("******************************\n")
        print("Welcome To The Groccery System\n")
        print("******************************\n")
        name = input("Enter Name Of User: ")
        if len(name) == 0:
            raise ValueError("Username Can't Be Empty")
        elif name.isdigit():
            raise ValueError("Name Can't Be Digits")
        
        return name
    
    
class Menu:
    @staticmethod
    def get_menu():
        my_menu = PrettyTable(["Options","Actions"])
        my_menu.add_row([1,"Add Items"])
        my_menu.add_row([2,"Remove Item"])
        my_menu.add_row([3,"Exit"])
        
        print(my_menu)
        
        choice = int(input("Enter Choice: "))
        if choice  ==  1:
            Cart.add_items()
        elif choice == 2:
            Cart.remove_items()
        elif choice == 3:
            Cart.exit_system()
        else:
            print("Invalid Choice")
            
    


class Qrcode:
    @staticmethod
    def get_qr():
        access_key = "WELCOME-0710"
        
        img = qrcode.make(access_key)
        img.save("shopping.png")
        access = input("Enter Access Key: ").strip().upper()
        if access == access_key:
            print("Access Granted")
        while True: 
                User.get_name()
                Menu.get_menu()
            
                stop = input("Press 0 to Exit and 1 to Continue: ")
                if stop == 0:
                    print("...GOODBYE...")
                    break
            
        else:
            print("Access Denied")

Qrcode.get_qr()
    
        