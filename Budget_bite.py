import random
import string
from prettytable import PrettyTable

print("Welcome To Budget Bites! ")
print('''🎉 BIG BITES, BIGGER SAVINGS! 🎉
💰 Shop for ₹300+ and get ₹40 OFF instantly!
💸 Spend ₹500+ and grab a ₹50 DISCOUNT — NO delivery charges!
🔥 Cross ₹1000? Enjoy a FLAT 30% OFF + FREE Choco Shake on us!
👉 The more you bite, the more you save! 🍔🥤
Only at Budget Bites — Where taste meets smart spending!''')

class Generate_order:
    @staticmethod
    def order_id():
        prefix = "ORD"
        suffix = "".join(random.choices(string.digits,k = 4))
        order_id = f"#{prefix}{suffix}"
        return order_id
    @staticmethod
    def captcha():
        a = random.randint(1,5)
        b = random.randint(2,6)
        return {
            "Question": f"What is {a} X {b}: ",
            "a": a,
            "b": b
        }
user_cart = []
delivery_charges = 50
while True:
    try:    
        print("...PRICE RANGE...")
        print("\n___________________")

        opt = {
            1: "₹50",
            2: "₹100",
            3: "₹150",
            4: "₹200"
        }
        for k,v in opt.items():
            print(f"{k}:{v}")
        print("\n___________________")
        x = int(input("Enter Your Price Range: "))
        match x:
            case 1:
                print(f"ORDER ID {Generate_order.order_id()} GENERATED")
                captcha = Generate_order.captcha()
                print(f"Captcha: {captcha["Question"]}")
                userans = int(input("Enter Ans: "))
                if userans == captcha["a"]*captcha["b"]:
                    print("Enjoy Your Price Range ₹50 Meal")
                    my_list = PrettyTable(["Price₹","ID","Item_Name"])
                    
                    my_list.add_row(["20","F001","Veg Samosa(2pcs)"])
                    my_list.add_row(["30","F002","Masala Maggi"])
                    my_list.add_row(["40","F003","Egg Roll"])
                    my_list.add_row(["50","F004","Aloo Paratha + Curd"])
                    
                    print(my_list)
                    
                    user_order = input("Enter Your Food Id: ").strip().upper()
                    if user_order == "F001":
                        print("Price: ₹20| ID: F001| Item Name: Veg Samosa(2pcs)")
                        user_cart.append({
                            "ID": "F001",
                            "Name": "Veg Samosas(2pcs)",
                            "Price": 20
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F002":
                        print("Price: ₹30| ID: F002| Item Name: Masala Maggi")
                        user_cart.append({
                            "ID": "F002",
                            "Name": "Masala Maggi",
                            "Price": 30
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F003":
                        print("Price: ₹40| ID: F003| Item Name: Egg Roll")
                        user_cart.append({
                            "ID": "F003",
                            "Name": "Egg Roll",
                            "Price": 40
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F004":
                        print("Price: ₹50| ID: F004| Item Name: Aloo Paratha + Curd")
                        user_cart.append({
                            "ID": "F004",
                            "Name": "Aloo Paratha + Curd",
                            "Price": 50
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    else:
                        print(f"No Item at {user_order} available")
                    print("Enjoy Your Meal")
            case 2:
                print(f"ORDER ID {Generate_order.order_id()} GENERATED")
                captcha = Generate_order.captcha()
                print(f"Captcha: {captcha["Question"]}")
                userans = int(input("Enter Ans: "))
                if userans == captcha["a"]*captcha["b"]:
                    print("Enjoy Your Price Range ₹100 Meal")
                    my_list = PrettyTable(["Price₹","ID","Item_Name"])
                    
                    my_list.add_row(["80","F005","Chicken Egg Roll"])
                    my_list.add_row(["90","F006","Veg Grilled Sandwich"])
                    my_list.add_row(["95","F007","Paneer Kathi Roll"])
                    my_list.add_row(["100","F008","Chilli Garlic Noodles"])
                    
                    print(my_list)
                    
                    user_order = input("Enter Your Food Id: ").strip().upper()
                    if user_order == "F005":
                        print("Price: ₹80| ID: F005| Item Name: Chicken Egg Roll")
                        user_cart.append({
                            "ID": "F005",
                            "Name": "Chicken Egg Roll",
                            "Price": 80
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F006":
                        print("Price: ₹90| ID: F006| Item Name: Veg Grilled Sandwich")
                        user_cart.append({
                            "ID": "F006",
                            "Name": "Veg Grilled Sandwitch",
                            "Price": 90
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F007":
                        print("Price: ₹95| ID: F007| Item Name: Paneer Kathi Roll")
                        user_cart.append({
                            "ID": "F007",
                            "Name": "Paneer Kathi Roll",
                            "Price": 95
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F008":
                        print("Price: ₹100| ID: F008| Item Name: Chilli Garlic Noodles")
                        user_cart.append({
                            "ID": "F008",
                            "Name": "Chilli Garlic Noodles",
                            "Price": 100
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    else:
                        print(f"No Item at {user_order} available")
                    print("Enjoy Your Meal")
            
            case 3:
                print(f"ORDER ID {Generate_order.order_id()} GENERATED")
                captcha = Generate_order.captcha()
                print(f"Captcha: {captcha["Question"]}")
                userans = int(input("Enter Ans: "))
                if userans == captcha["a"]*captcha["b"]:
                    print("Enjoy Your Price Range ₹150 Meal")
                    my_list = PrettyTable(["Price₹","ID","Item_Name"])
                    
                    my_list.add_row(["130","F009","Chicken Fried Rice"])
                    my_list.add_row(["140","F010","Paneer Butter Masala + Roti"])
                    my_list.add_row(["145","F011","Veg Cheese Burger + Fries"])
                    my_list.add_row(["150","F012","Chicken Biryani (Half Plate)"])
                    
                    print(my_list)
                    
                    user_order = input("Enter Your Food Id: ").strip().upper()
                    if user_order == "F009":
                        print("Price: ₹130| ID: F009| Item Name: Chicken Fried Rice")
                        user_cart.append({
                            "ID": "F009",
                            "Name": "Chicken Fried Rice",
                            "Price": 130
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F010":
                        print("Price: ₹140| ID: F010| Item Name: Paneer Butter Masala + Roti")
                        user_cart.append({
                            "ID": "F010",
                            "Name": "Paneer Butter Masala + Roti",
                            "Price": 140
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F011":
                        print("Price: ₹145| ID: F011| Item Name: Veg Cheese Burger + Fries")
                        user_cart.append({
                            "ID": "F011",
                            "Name": "Veg Cheese Burger + Fries",
                            "Price": 145
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F012":
                        print("Price: ₹150| ID: F012| Item Name: Chicken Biryani (Half Plate)")
                        user_cart.append({
                            "ID": "F012",
                            "Name": "Chicken Biryani (Half Plate)",
                            "Price": 150
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    else:
                        print(f"No Item at {user_order} available")
                    print("Enjoy Your Meal")
            case 4:
                print(f"ORDER ID {Generate_order.order_id()} GENERATED")
                captcha = Generate_order.captcha()
                print(f"Captcha: {captcha["Question"]}")
                userans = int(input("Enter Ans: "))
                if userans == captcha["a"]*captcha["b"]:
                    print("Enjoy Your Price Range ₹200 Meal")
                    my_list = PrettyTable(["Price₹","ID","Item_Name"])
                    
                    my_list.add_row(["180","F013","Chicken Biryani + Pepsi (250ml) + Gulab Jamun"])
                    my_list.add_row(["190","F014","Veg Thali (Paneer, Dal, Rice, Roti) + Sprite + Rasgulla"])
                    my_list.add_row(["195","F015","Egg Noodles + Frooti (200ml) + Ice Cream Cup"])
                    my_list.add_row(["200","F016","Chicken Burger + Coke (250ml) + Brownie Slice"])
                    
                    print(my_list)
                    
                    user_order = input("Enter Your Food Id: ").strip().upper()
                    if user_order == "F013":
                        print("Price: ₹180| ID: F013| Item Name: Chicken Biryani + Pepsi (250ml) + Gulab Jamun")
                        user_cart.append({
                            "ID": "F013",
                            "Name": "Chicken Biryani + Pepsi (250ml) + Gulab Jamun",
                            "Price": 180
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F014":
                        print("Price: ₹190| ID: F014| Item Name: Veg Thali (Paneer, Dal, Rice, Roti) + Sprite + Rasgulla")
                        user_cart.append({
                            "ID": "F014",
                            "Name": "Veg Thali (Paneer, Dal, Rice, Roti) + Sprite + Rasgulla",
                            "Price": 190
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F015":
                        print("Price: ₹195| ID: F015| Item Name: Egg Noodles + Frooti (200ml) + Ice Cream Cup")
                        user_cart.append({
                            "ID": "F015",
                            "Name": "Egg Noodles + Frooti (200ml) + Ice Cream Cup",
                            "Price": 195
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    elif user_order == "F016":
                        print("Price: ₹200| ID: F016| Item Name: Chicken Burger + Coke (250ml) + Brownie Slice")
                        user_cart.append({
                            "ID": "F016",
                            "Name": "Chicken Burger + Coke (250ml) + Brownie Slice",
                            "Price": 200
                        })
                        total_price = sum(item["Price"] for item in user_cart)
                        print(f"Your Price is: ₹{total_price}")
                    else:
                        print(f"No Item at {user_order} available")
                    print("Enjoy Your Meal")
            case _:
                print("Invalid Choice")
                break
                
        stop = input("Do You Want To Stop (y/n): ")
        if stop.strip().lower() == "y":
            if total_price > 300 and total_price < 500:
                final_price = (total_price -40) + delivery_charges
                print(f"Amount: ₹ {final_price}")
            elif total_price > 500 and total_price < 1000:
                final_final_price = (total_price - 100)
                print(f"Amount: ₹{final_final_price} with ₹{delivery_charges} delivery charge cut")
            elif total_price > 1000:
                final_final_final_price = total_price - ((total_price*30)/100)
                print(f"Amount: ₹{final_final_final_price} and a chocolate shake 🥤 free")
            else:
                print(f"Amount: ₹{total_price}")
            break

    except ValueError as ve:
        print (f"Error: {ve}")
        break
    except Exception as e:
        print(f"Error: {e}")
        break
    finally: 
        print("Thank you for visiting Budget Bites! Have a great day!")