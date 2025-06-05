import random
import string
from prettytable import PrettyTable
import qrcode

students = []


class Student:
    
    @staticmethod
    def gen_unique_id():
        prefix = "S"
        suffix = "".join(random.choices(string.digits, k = 7))
        return f"{prefix}{suffix}"
    
    @staticmethod
    def get_name():
        name = input("Enter Name: ").strip().capitalize()
        if len(name) == 0:
            raise ValueError("Name Can't Be Empty")
        elif name.isdigit():
            raise ValueError("Name Can't Be Digits")
        
        return name
    
    @staticmethod
    def get_scores():
        scores = {
            "Bengali": float(input("Enter Marks of Bengali: ")),
            "English": float(input("Enter Marks of English: ")),
            "Mathamatics": float(input("Enter Marks of Mathamatics: ")),
            "Physics": float(input("Enter Marks of Physics: ")),
            "Chemistry": float(input("Enter Marks of Chemistry: ")),
        }
        
        avg_score = (scores["Bengali"] + scores["English"] + scores["Mathamatics"] + scores["Physics"] + scores["Chemistry"])/5
        for subject, score in scores.items():
            if score < 0 or score > 100:
                raise ValueError(f"Invalid score in {subject}. Scores must be between 0 and 100.")
        
        if avg_score >= 90:
            grade = "A"
        elif avg_score >= 75:
            grade = "B"
        elif avg_score >= 50:
            grade = "C"
        else:
            grade = "D"

        
        my_scores = PrettyTable(["Subject","Marks","Full Marks","Average Score","Grade"])
        my_scores.add_row(["Bengali",f"{scores['Bengali']}",100,"",""])
        my_scores.add_row(["English",f"{scores['English']}",100,"",""])
        my_scores.add_row(["Mathamatics",f"{scores['Mathamatics']}",100,f"{avg_score}",f"{grade}"])
        my_scores.add_row(["Physics",f"{scores['Physics']}",100,"",""])
        my_scores.add_row(["Chemistry",f"{scores['Chemistry']}",100,"",""])
        
        return my_scores


class Management:
    @staticmethod
    def add_student():
        global students
        n = int(input("Enter No of How Many Students Will Be Added? "))
        for i in range(n):
            name = Student.get_name()
            unique_id = Student.gen_unique_id()
            scores = Student.get_scores()
            
            students.append([name,unique_id,scores])
            print(students)

    @staticmethod
    def search_student():
        global students
        is_found = False
        uniique_id_to_search = input("Enter Unique Id To Search: ").strip().upper()
        
        for student in students:
            if student[1] == uniique_id_to_search:
                print("Student Found")
                print(f"Unique ID: {student[1]}| Name: {student[0]}| Scores: {student[2]}")
                is_found = True
                break
        else:
            print(f"Student With {uniique_id_to_search} Not Found")
    
    @staticmethod
    def delete_student():
        global students
        is_found = False
        unique_id_to_delete = input("Enter Unique id To Delete: ").strip().upper()
        for student in students:
            if student[1] == unique_id_to_delete:
                students.remove(student)
                print(students)
                is_found = True
                break
        else:
            print(f"Student With Unique Id {unique_id_to_delete} not Found")
    
    @staticmethod
    def exit_system():
        print("Exit")
    
class Menu:
    @staticmethod
    def generate_menu():
        my_menu = PrettyTable(["Options","Actions"])
        my_menu.add_row([1,"Add Student"])
        my_menu.add_row([2,"Search Student"])
        my_menu.add_row([3,"Delete Student"])
        my_menu.add_row([4,"Exit"])
        
        print(my_menu)
        
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                Management.add_student()
            elif choice == 2:
                Management.search_student()
            elif choice == 3:
                Management.delete_student()
            elif choice == 4:
                Management.exit_system()
            else:
                print("Invalid Choice")
                
        except ValueError as ve:
            print(f"Error: {ve}")
        
class Qrcode:
    @staticmethod
    def gen_qr():
        access_key = "STUDENT-SCORE-MANAGEMENT-2025,./@"
        img = qrcode.make(access_key)
        img.save("Student-score-management.png")
while True:
    Qrcode.gen_qr()
    access = input("Scan QR Code to get access key: ").strip().upper()
    if access == "STUDENT-SCORE-MANAGEMENT-2025,./@":
        print("Access Granted")
        Menu.generate_menu()
    else:
        print("Access Denied")
        
