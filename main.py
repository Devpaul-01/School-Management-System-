
from user import Teacher 
from user import Student 
from user import Admin
from user import Quiz
def take_quiz():
    quiz = Quiz()
    name = input("Enter your student name")
    pin = input("Enter your four digit pin")
    content = Quiz.check_student(name, pin)
    if not content:
        return
    subject = input("Enter the subject you would like to take the quiz")
    subject_valid = Quiz.check_subject(subject, content)
    if not subject_valid:
        return
    questions = quiz.validate_subject(subject_valid)
    if not questions:
        return
    quiz.take_quiz(subject_valid, questions, content)
    
        
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
	list_subjects = input("Enter list of subjects you are offering")
	subject_list = [(d).strip() for d in list_subjects.split(",")]
	subjects = {}
	for subject in subject_list:
	 subjects[subject] = {"teacher": "", "grade": None}
	 grades = [ ]
	 fees = {"total_dues": 50000, "amount_paid": 0, "balance": 50000, "payment_history": []}
	 student = Student(name, age, pin, role, None, level, fees, subjects, [])
	student.register_student()
def admin_login():
	password = input("Enter your password ")
	admin = Admin( )
	result = admin.check_admin(password)
	if result:
	    print("Welcome to admin section let us know how we can help you ")
	    print("Here are the list of operations you could perform as an admin")
	    print("Kindly choose from the list below")
	    print("View Student")
	    print("View Teacher")
	    print("View Teachers List")
	    print("Punish defaulters")
	    option = input("What would you like to do")
	    if option == "1":
	        student = input("Enter student name")
	        admin.view_student(student)
	    elif option == "2":
	        teacher = input("Enter teacher name")
	        admin.teacher_info(teacher)
	    elif option == "3":
	        admin.view_teachers()
	    elif option == "4":
	        print("Welcome to the punishment board")
	        print("Punishment particular student")
	        print("Punish all students")
	        choose = input("Enter your choice")
	        if choose == "1":
	            name = input("Enter student name")
	            admin.apply_subject(name)
	        elif choose == "2":
	            print("All defaulters shall be punished")
	            admin.loop_punishments()
	        else:
	            print("Invalid option kindly choose from the option above")
	    else:
	        print("Invalid option kindly choose from the option above")
	
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
		print("View Students")
		print("Remove Students")
		print("Assign Grade")
		print("View Profile")
		print("View History")
		print("Take Attendance")
		print("Logout")
		choice = input("Enter your choice")
		if choice == "1":
			new_salary = input("Enter your new salary")
			teacher.add_salary(new_salary)
		elif choice == "2":
			student = input("Enter your name")
			status = input("Enter student status")
			teacher.take_attendance(name, status)
		elif choice == "3":
			teacher.view_history()
		elif choice == "4":
		    teacher.view_students()
		elif choice == "5":
		    name = input("Enter student name")
		    subject = input("Which subject would you like to remove the student for")
		    teacher.remove_student(name, subject)
		elif choice == "6":
		    name = input("Enter student name")
		    subject = input("Enter subject name")
		    grade = input("Enter grade to assign")
		    teacher.assign_grade(name, subject, grade)
		elif choice == "7":
		    teacher.view_profile()
		elif choice == "8":
		    teacher.view_history()
		elif choice == "9":
		    student = input("Enter student name")
		    status = input("Enter student status (present/absent)")
		    teacher.take_attendance(student, status)
		elif choice == "10":
		    teacher.logout_teacher()
		    break
		else:
		    print("Invalid choice kindly choose from an option above")
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
		print("View grades")
		print("View history")
		print("Make Payments")
		print("Add Subjects")
		print("View Payment")
		print("View Attendance")
		print("Course Details")
		print("View History")
		print("Edit Details")
		print("Logout")
		choice = input("Enter what you want to do")
		if choice == "1":
			student.view_grades()
		elif choice == "2":
			student.view_history()
		elif choice == "3":
		    amount = int(input("How much would you like to pay"))
		    student.make_payment(amount)
		elif choice == "4":
		    subject = input("Which subject would you like to add")
		    student.add_subject(subject)
		elif choice == "5":
		    student.view_payment()
		elif choice == "6":
		    student.view_attendance()
		elif choice == "7":
		    student.course_details()
		elif choice == "8":
		    student.view_history()
		elif choice == "9":
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
				else:
					print("Invalid edit options")
		elif choice == "10":
			student.logout_student()
		else:
		    print("Invalid option kindly choose from the listed option above")
	
print("Welcome to students, teacher and admin portal How can we help you")
print("Are you a student, teacher, quiz contestant or administrator")
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
elif choice.lower() == "quiz":
    take_quiz()
else:
		print("Invalid option")
		

					
					
					
				
			
		