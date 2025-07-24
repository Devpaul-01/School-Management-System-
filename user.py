import random 
import os 
import json 
from datetime import datetime 
class User:
	def __init__(self, name, age, pin, role, history = None):
		self.name = name
		self.age = age
		self.pin = pin
		self.role = role
		self.history = history if isinstance(history,  list) else [ ]
class Student(User):
	folder_name = "Students folder"
	def __init__(self, name, age, pin, role, level, grades=None, history=None, id=None):
		choice = ["A", "B", "C", "D", "1", "2", "3",  "4"]
		super ( ).__init__(name, age, pin, role, history)
		self.grades = grades if isinstance(grades,  list) else [ ]
		self.level = level
		self.id = id or ' ' . join(random.sample(choice, k=5))
	def register_student(self):
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		self.history.append(f"Saved on {time}")
		details = {"name": self.name, "age": self.age,  "pin": self.pin, "role": self.role, "level": self.level, "grades": self.grades, "history": self.history, "ID": self.id}
		folder_name = "Students folder"
		file_name = f"{self.name}.json"
		if not os.path.exists(folder_name):
			os.mkdir(folder_name)
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "w") as file:
			json.dump(details, file, indent = 4)
			print("Student registered successfully")
	@staticmethod
	def login_student(name, pin):
		folder_name = "Students folder"
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		if os.path.exists(file_path):
			with open(file_path, "r") as file:
				content = json.load(file)
				saved_pass = content["pin"]
				history = content.get("history", [ ] )
				grades = content.get("grades", [ ] )
				if pin == content.get("pin"):
					 student = Student (content["name"], content["age"], content["pin"], content["role"], content["level"], grades, history, content.get("ID") )
					 return student 
		return None
	def add_grades(self, grade):
		folder_name = "Students folder"
		self.grades.append(grade)
		name = self.name
		file_name = f"{name}.json"
		now = datetime.now().strftime("%A, %d %B %Y %I : %M %p")
		real = f"Student grade added on {now}"
		self.history.append(real)
		file_path = os.path.join(folder_name, file_name)
		content = {
    "name": self.name,
    "age": self.age,
    "ID": self.id,
    "pin": self.pin,
    "role": self.role,
    "level": self.level,
    "grades": self.grades,
    "history": self.history
}
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
		print("Student grade added succesfully")
	def view_grades(self):
		now = datetime.now()
		folder_name = "Students folder"
		content = {
    "name": self.name,
    "age": self.age,
    "ID": self.id,
    "pin": self.pin,
    "role": self.role,
    "level": self.level,
    "grades": self.grades,
    "history": self.history
}
		name = self.name
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		grades = self.grades
		if not grades:
			print("No grades")
		else:
			print("Grades")
			print(grades)
		self.history.append(f"View grades on {time}")
		with open(file_path, "w") as file:
			json.dump(content, file, indent = 4)
	@staticmethod				
	def edit_details(name, pin):
		folder_name = "Students folder"
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		if os.path.exists(file_path):
			with open(file_path, "r") as file:
				content = json.load(file)
				sav_pass = content.get("pin")
				if pin == sav_pass:
					print("Login succesful")
					return content
		return None	
	def edit_name(self, content, new_name):
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		folder_name = "Students folder"
		old_name = content["name"]
		old_file = f"{old_name}.json"
		old_path = os.path.join(folder_name, old_file)
		if os.path.exists(old_path):
			os.remove(old_path)
		content["name"] = new_name
		file_name = f"{new_name}.json"
		new_path = os.path.join(folder_name, file_name)
		self.history.append(f"Changed name to {new_name} on {time}")
		with open(new_path, "w") as file:
			json.dump(content, file, indent=4)
			
	def edit_age(self, content, new_age):
		folder_name = "Students folder"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		old_age = content["age"]
		name = content["name"]
		content["age"] = new_age
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		self.history.append(f"Changed age to {new_age} on {time}")
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
			print("New age updated ")
	def edit_pin(self, content, new_pin):
		folder_name = "Students folder"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		old_pin = content["pin"]
		name = content["name"]
		content["pin"] = new_pin
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "w") as file:
			self.history.append(f"Changed login pin to {new_pin} on {time}")
			json.dump(content, file, indent=4)
			print("Pin reset successfully")
	def edit_grades(self, content, new_grades):
		folder_name = "Students folder"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		grades = content["grades"]
		name = content["name"]
		cleaned_grades = [ int(grade.strip()) 
		for grade in new_grades.split()]
		content["grades"] = cleaned_grades
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		self.history.append(f"Changed grades to {new_grades} on {time}")
		with open(file_path, "w") as file:
			json.dump(content, file, indent= 4)
			date = datetime.now()
			print("Grades updated successfully")
	def logout_student(self):
		name = self.name
		file_name = f"{name}.json"
		folder_name = "Students folder"
		file_path = os.path.join(folder_name, file_name)
		content = {"name": self.name, "age": self.age, "ID": self.id, "pin": self.pin, "role": self.role, "level": self.level, "grades": self.grades, "history": self.history}
		with open(file_path, "w") as file:
		  	json.dump(content, file, indent=4)
		  	print("Logging out changes saved")
		
	def view_history(self):
		folder_name = "Students folder"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		name = self.name
		file_name = f"{name}.json"
		self.history.append(f"Viewed history on {time}")
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "r") as file:
			content = json.load(file)
			histories = content.get("history", [ ])
			if not histories:
				print("No records")
			else:
						for history in histories:
							print("-", history)
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
class Teacher(User):
	folder_name = "Teachers folder"
	def __init__(self, name, age, pin, role, subject, salary, history=None, attendance=None):
		super().__init__(name, age, pin, role, history)
		self.subject = subject 
		self.salary = salary
		self.attendance = attendance if isinstance(history, list) else [ ]
		
	def logout_teacher(self):
		name = self.name
		folder_name = "Teachers folder"
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		content = {
    "name": self.name,
    "age": self.age,
    "pin": self.pin,
    "role": self.role,
    "subject": self.subject,
    "salary": self.salary,
    "attendance": self.attendance,
    "history": self.history
}
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
			print("Logging out")
	@staticmethod
	def load_teacher(name, pin):
		folder_name = "Teachers folder"
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		if os.path.exists(file_path):
			with open(file_path, "r") as file:
				content = json.load(file)
				history = content.get("history", [ ])
				attendance = content.get("attendance", [ ])
				if pin == content["pin"]:
					print("Login successfully ")
					teacher = Teacher(content["name"], content["age"], content["pin"], content["role"], content["subject"], content["salary"], history, attendance)
					return teacher 
		return None 
						
	def save_teacher(self):
		folder_name = "Teachers folder"
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		content = {
    "name": self.name,
    "age": self.age,
    "pin": self.pin,
    "role": self.role,
    "subject": self.subject,
    "salary": self.salary,
    "attendance": self.attendance,
    "history": self.history
}
		if not os.path.exists(folder_name):
			os.mkdir(folder_name)
		with open(file_path, "w") as file:
				json.dump(content, file, indent = 4)
				print("Teacher registered successfully")
	def add_salary(self, new_salary):
		folder_name = "Teachers folder"
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		with open (file_path, "r") as file:
				content = json.load(file)
				salary = content["salary"]
				content["salary"] = new_salary
				self.history.append(f"Changed salary to {new_salary}")
				with open(file_path, "w") as file:
					json.dump(content, file, indent=4)
					print("Salary added successfully")
	def view_profile(self):
		folder_name = "Teachers folder"
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		if os.path.exists(file_path):
			with open(file_path, "r") as file:
				content = json.load(file)
				print("Login succesful")
				print(content)
		else:
			print("User not found")
	def view_history(self):
		folder_name = "Teachers folder"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "r") as file:
					content = json.load(file)
					histories = content.get("history", [ ])
					if not histories:
						print("History not found")
					else:
					 for history in histories:
					 	print("-", history)
	def take_attendance(self, student, status):
		folder_name = "Teachers folder"
		file_name = f"{self.name}.json"
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		entry = f"Student {student} was {status} on {time}"
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "r") as file:
			content = json.load(file)
			attendance = content["attendance"]
			attendance.append(entry)
			with open(file_path, "w") as file:
				self.history.append(f"Took attendance on {now}")
				json.dump(content, file, indent = 4)
				print("Attendance taken successfully")

class Admin:
	def __init__(self, pin="admin"):
		self.pin = pin
	def view_admin(self, name, password):
		folder_name = "Students folder"
		file_name = f"{name}.json"
		if password == self.pin:
			file_path = os.path.join(folder_name, file_name)
			if os.path.exists(file_path):
				with open(file_path, "r") as file:
					content = json.load(file)
					print("Login successful")
					print(content)
			else:
					print("Student not found")
		else:
														print("Incorrect password ")
														
															
														
														
												
											
																		
																	
																	
																	
																
																
															
													
												
											
											
							
							
							
					
				
		
			
			
		
		
	
	
	
		
		
		
			
		
	
		


