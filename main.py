
from user import Teacher 
from user import Student 
from user import Admin 
def teacher_registration():
	name = input("Enter your name")
	age = input("Enter your age")
	pin = input("Enter your pin")
	role = input("Enter your role")
	subject = input("Which subject are you teaching")
	salary = input("Enter your salary")
	teacher = Teacher(name, age, pin, role, subject, salary, [ ], [ ])
	teacher.save_teacher()
def students_registration():
	name = input("Enter your name")
	age = input("Enter your age")
	role = input("What is your role")
	pin = input("Enter your pin")
	level = input("What level are you")
	grades = [ ]
	student = Student(name, age, pin, role, level, grades, [ ], " ")
	student.register_student()
def admin_login():
	name = input("Enter your student name")
	password = input("Enter your password ")
	admin = Admin( )
	admin.view_admin(name, password)
def teachers_login():
	name = input("Enter your name")
	pin = input("Enter your pin")
	teacher = Teacher.load_teacher(name, pin)
	if not teacher:
		print("Login not successful")
		return 
	print("Login successful welcome")
	while True:
		print("Let us know how we can help you")
		print("Add salary")
		print("Record attendance")
		print("View history")
		print("Logout")
		choice = input("Enter your choice")
		if choice == 1:
			new_salary = input("Enter your new salary")
			teacher.add_salary(new_salary)
		elif choice == "2":
			student = input("Enter your name")
			status = input("Enter student status")
			teacher.take_attendance(name, status)
		elif choice == "3":
			teacher.view_history()
		elif choice == "4":
			teacher.logout_teacher()
			break
		else:
			print("Invalid option")
def students_login():
	name = input("Enter your name")
	pin = input("Enter your password")
	student = Student.login_student(name, pin)
	if not student:
		print("Incorrect details")
		return
	print("Login successful ")
	while True:
		print("Welcome to your portal")
		print ("Kindly choose from the option below")
		print("Add grades")
		print("View grades")
		print("View history")
		print("Edit details")
		print("Logout")
		
		choice = input("Enter what you want to do")
		if choice == "1":
			grade = int(input("Enter grade"))
			student.add_grades(grade)
		elif choice == "2":
			student.view_grades()
		elif choice == "3":
			student.view_history()
		elif choice == "5":
			student.logout_student()
			break
		elif choice == "4":
			name = input("Enter your name")
			pin = input("Enter your pin")
			content = student.edit_details(name, pin)
			if not content:
				print("invalid login")
				continue 
			while True :
				print("Welcome to edit section")
				print("What would you like to edit")
				print("Name")
				print("Age")
				print("Pin")
				print("grades")
				
				choice = input("What is your choice")
				if choice == "1":
					new_name = input("Enter your new name")
					student.edit_name(content, new_name)
				elif choice == "2":
					new_age = input("Enter your new age")
					student.edit_age(content, new_age)
				elif choice == "3":
					new_pin = input("Enter your new pin")
					student.edit_pin(content, new_pin)
				elif choice == "4":
					new_grades = input("Enter your new grades")
					student.edit_grades(content, new_grades)
				else:
					print("Invalid edit options")
		else:
					print("Invalid option")
	
print("Welcome to students, teacher and admin portal How can we help you")
print("Are you a student, teacher or administrator")
choice = input("Who are you")
if choice.lower() == "admin":
	admin_login()
elif choice.lower() == "teacher":
	print("Welcome to teacher section")
	print("Would you like to register or login")
	option = input("Choose from the ppti above")
	if option.lower() == "register":
		teacher_registration()
	elif option.lower() == "login":
		teachers_login()
	else:
		print("Invalid option")
elif choice.lower() == "student":
		print("Welcome to student section")
		print("How can we help you")
		print("Would you like to register or login")
		choice = input("Choose from one of the options below")
		if choice.lower() == "register":
			students_registration()
		elif choice.lower() == "login":
			students_login()
		else:
			print("Invalid option")
else:
		print("Invalid option")
		

					
					
					
				
			
		