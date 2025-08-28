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
	def __init__(self, name, age, pin, role, id, level, fees, subjects, history=None ):
		choice = ["A", "B", "C", "D", "1", "2", "3",  "4"]
		super ( ).__init__(name, age, pin, role, history)
		self.level = level
		self.id = id or ' ' .join(random.sample(choice, k=5))
		self.fees = fees
		self.subjects = subjects
	def build_student_record(self):
	       return {
	       "name": self.name,
	       "age": self.age,                 # int or str, but be consistent
	       "pin": self.pin,                 # NEVER store plain pins in production (hash later)
	       "role": self.role,               # "student"
	       "ID": self.id,        # e.g., "SS2"
	       "level": self.level,                   # auto-generated if None
	       "fees": {
	       "total_dues": self.fees.get("total_dues", 50000),
	       "amount_paid": self.fees.get("amount_paid", 0),
	       "balance": self.fees.get("balance", 50000),
	       "payment_history": self.fees.get("payment_history", [])},
	       "subjects": self.subjects if isinstance(self.subjects, dict) else {},
	       "history": self.history if isinstance(self.history, list) else [ ]}
	       
	def register_student(self):
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		self.history.append(f"Saved on {time}")
		content = self.build_student_record()
		folder_name = "Students folder"
		file_name = f"{self.name}.json"
		if not os.path.exists(folder_name):
			os.mkdir(folder_name)
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "w") as file:
			json.dump(content, file, indent = 4)
			print("Student registered successfully")
	def make_payment(self, amount):
	   file_name = f"{self.name}.json"
	   folder_name = "Students folder"
	   file_path = os.path.join(folder_name, file_name)
	   if not os.path.exists(file_path):
	       print("Student not registered")
	       return 
	   with open(file_path, "r") as file:
	       content = json.load(file)
	       now = datetime.now()
	       time = now.strftime("%A, %d %B %Y at %I:%M %p")
	       entry = {"amount": amount, "date": time}
	       fees = content.get("fees", {})
	       total_dues = fees.get("total_dues", 50000)
	       amount_paid = fees.get("amount_paid", 0) + amount
	       balance = max(0, total_dues - amount_paid)
	       content["fees"]["amount_paid"] = amount_paid
	       content["fees"]["balance"] = balance
	       content["fees"].setdefault("payment_history", []).append(entry)
	       content.setdefault("history", []).append(f"Paid {amount} on {time}")
	       with open(file_path, "w") as file:
	           json.dump(content, file, indent=4)
	           print("Payment made successfully")
	def view_grades(self):
		folder_name = "Students folder"
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		with open(file_path, "r") as file:
		    content = json.load(file)
		    subjects = content["subjects"]
		    for subject, details in subjects.items():
		        res = "Subject not graded yet"
		        grade = details.get("grade", res)
		        print(f"{subject}: {grade}")
		    
	def add_subject(self, subject):
	     file_name = f"{self.name}.json"
	     folder_name = "Students folder"
	     file_path = os.path.join(folder_name, file_name)
	     with open(file_path, "r") as file:
	         content  = json.load(file)
	         subjects = content.get("subjects")
	         if subject in subjects:
	             print("Subject already registered")
	             return
	         subjects[subject] = {"teacher": "", "grade":None}
	         now = datetime.now().strftime("%A, %d %B %Y at %I:%M %p")
	         history = content.setdefault("history", [])
	         history.append(f"Registered for {subject} on {now}")
	         with open(file_path, "w") as file:
	             json.dump(content, file, indent=4)
	             print("Subject added successfully")
	def view_payment(self):
	    file_name = f"{self.name}.json"
	    folder_name = "Students folder"
	    file_path = os.path.join(folder_name, file_name)
	    with open(file_path, "r") as file:
	        content = json.load(file)
	        fees = content.get("fees", { })
	        if fees:
	            print("Here are your payments records")
	            print(fees)
	            return
	def view_attendance(self):
	  file_name = f"{self.name}.json"
	  folder_name = "Teachers folder"
	  if not os.path.exists(folder_name):
	          print("No teachers record yet")
	          return
	  matches = [ ]
	  files = os.listdir(folder_name)
	  for fname in files:
	          if not fname.endswith(".json"):
	              continue 
	          with open(os.path.join(folder_name, fname), "r") as file:
	              try:
	                  content = json.load(file)
	              except Exception:
	                 continue
	              for entry in content.get("attendance", []):
	                 if not isinstance(entry, dict):
	                     continue
	                 if entry.get("student") == self.name:
	                     matches.append(entry)
	  if not matches:
	      print("No attendance records for you yet")
	  else:
	       for m in matches:
	           print(f" - {m.get('time')} : {m.get('status')} (by {m.get('teacher')})")    
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
					 print(content)
					 student = Student(content["name"], content["age"], content["pin"], content["role"], content["ID"], content["level"], content["fees"], content["subjects"], content ["history"])
					 return student 
		return None
	def course_details(self):
		now = datetime.now()
		folder_name = "Students folder"
		content = self.build_student_record()
		name = self.name
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		subjects = content.get("subjects", { })
		if subjects:
		    list = [ ]
		    for entry in subjects:
		        list.append(entry)
		for a in list:
		    print(a)
		else:
		    print("No subject registered")
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
		print("Name changed successfully")
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
	def logout_student(self):
		name = self.name
		file_name = f"{name}.json"
		folder_name = "Students folder"
		file_path = os.path.join(folder_name, file_name)
		content = self.build_student_record()
		with open(file_path, "w") as file:
		  	json.dump(content, file, indent=4)
		  	print("Logging out changes saved")
		
	def view_history(self):
		folder_name = "Students folder"
		now = datetime.now()
		now = datetime.now()
		time = now.strftime("%A, %d %B %Y at %I:%M %p")
		name = self.name
		content = self.build_student_record()
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		history = content.get("history", [])
		if history:
		    for file in history:
		        print(file, end= " ")
		    content.get("history", [ ]).append(f"Viewed history on {time}")
		else:
		    print("No history records yet")
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
class Teacher(User):
	folder_name = "Teachers folder"
	def __init__(self, name, age, pin, role, subject, salary, history=None, attendance=None):
		super().__init__(name, age, pin, role, history)
		self.subject = subject 
		self.salary = salary
		self.attendance = attendance if isinstance(attendance, list) else [ ]
	def build_teacher_record(self):
	       return {
	       "name": self.name,
	       "age": self.age,
	       "pin": self.pin,
	       "role": self.role,           # "teacher"
	       "subject": self.subject,     # main subject (string)
	       "salary": self.salary,       # number
	       "attendance": self.attendance if isinstance(self.attendance, list) else [],
	       "history": self.history if isinstance(self.history, list) else []
	       }
		
	def logout_teacher(self):
		name = self.name
		folder_name = "Teachers folder"
		file_name = f"{name}.json"
		file_path = os.path.join(folder_name, file_name)
		content = self.build_teacher_record()
		with open(file_path, "w") as file:
			json.dump(content, file, indent=4)
			print("Logging out")
	@staticmethod
	def view_students():
	    folder_name = "Students folder"
	    content = os.listdir(folder_name) if os.path.exists(folder_name) else []
	    if content:
	        for i in content:
	            print("-", i)
	    else:
	        print("No student records for now")
	def remove_student(self, student_name, subject_name):
	   print(f"Teacher {self.name} is removing {student_name} from {subject_name}")
	   file_name = f"{student_name}.json"
	   folder_name = "Students folder"
	   file_path = os.path.join(folder_name, file_name)
	   with open(file_path, "r") as file:
	       content = json.load(file)
	       if subject_name in content["subjects"]:
	           del content["subjects"][subject_name]
	           content.setdefault("history", []).append(f"Subject {subject_name} removed by Teacher {self.name}")
	           with open(file_path, "w") as f:
	               json.dump(content, f, indent=4)
	               print("Student subject deleted successfully")
	       else:
	           print("Student is not registered for this subject")
	def assign_grade(self, name, subject, grade):
	    file_name = f"{name}.json"
	    folder_name = "Students folder"
	    file_path = os.path.join(folder_name, file_name)
	    with open(file_path, "r") as file:
	        content = json.load(file)
	        subjects = content["subjects"]
	        content["subjects"][subject]["grade"] = grade
	        content["subjects"][subject]["teacher"] = self.name
	        with open(file_path, "w") as file:
	            json.dump(content, file, indent=4)
	            print("Grade assigned successfully")
	   
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
		content = self.build_teacher_record()
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
		now = datetime.now().strftime("%A, %d %B %Y at %I:%M %p")
		folder_name = "Teachers folder"
		file_name = f"{self.name}.json"
		file_path = os.path.join(folder_name, file_name)
		att = {
		"student": student,
		"status": status,         # e.g., "present"/"absent"
		"time": now,            # formatted timestamp
		"teacher": self.name
		}
		with open(file_path, "r") as file:
		    content = json.load(file)
		attendance = content.get("attendance", [ ])
		attendance.append({
		"student": student,
		"status": status,         # e.g., "present"/"absent"
		"time": now,          # formatted timestamp
		"teacher": self.name
		})
		content["attendance"] = attendance
		content.setdefault("history", []).append(f"{student} was {status} on {now}")
		with open(file_path, "w") as file:
		  json.dump(content, file, indent=4)
		  print("Attendance taken successfully")

class Admin:
    def __init__(self, pin="admin"):
        self.pin = pin

    def check_admin(self, password):
        folder1 = "Students folder"
        folder2 = "Teachers folder"
        if password == self.pin:
            print("Correct password login successful")
            data1 = os.listdir(folder1)
            data2 = os.listdir(folder2)
            if data1:
                for data in data1:
                    print(data)
            else:
                print("No student record at the moment")
            if data2:
                for data in data2:
                    print(data)
            else:
                print("No teacher record at the moment")
            return True
        else:
            print("Incorrect password enter correct admin password")
            return False
    @staticmethod
    def view_student(name):
        folder_name = "Students folder"
        file_name = f"{name}.json"
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = json.load(file)
                print("Login successful")
                print(content)
        else:
            print("Student not found")
    @staticmethod
    def loop_punishments():
        folder_name = "Students folder"
        student_files = os.listdir(folder_name) if os.path.exists(folder_name) else []
        if student_files:
            for file in student_files:
                if not file.endswith(".json"):
                    continue
                folder_name = "Students folder"
                file_path = os.path.join(folder_name, file)
                try:
                    with open(file_path, "r") as f:
                        content = json.load(f)
                        fees = content.get("fees", {})
                        amount_paid = fees.get("amount_paid", 0)
                        if amount_paid == 0:
                            print("Student is still yet to make any payments")
                            os.remove(file_path)
                            print("Punishment applied \n. Student removed from student list")
                        elif 0 < amount_paid < 50000:
                            print("Student made partial payment therefore the right pumi would be applied")
                            content["subjects"] = {}
                            print("Students subjects deleted successfully")
                            with open(file_path, "w") as f_out:
                                json.dump(content, f_out, indent=4)
                except Exception as e:
                    print(f"Error while processing file {file}")

    def apply_subject(self, name):
        file_name = f"{name}.json"
        folder_name = "Students folder"
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "r") as file:
            content = json.load(file)
            fees = content.get("fees", {})
            amount_paid = fees.get("amount_paid", 0)
            if amount_paid == 0:
                print("Student hasn't made any payments yet therefore he woi be removed as a student......")
                os.remove(file_path)
                print("Student removed successfully")
            elif 0 < amount_paid < 50000:
                print(f"Student paid {amount_paid} naira which is not full payment therefore we delete all his registered subjects....")
                content["subjects"] = {}
                with open(file_path, "w") as f:
                    json.dump(content, f, indent=4)
            else:
                print(f"Invalid amount: {amount_paid}")
            

    @staticmethod  
    def view_teachers():
        folder_name = "Teachers folder"
        teachers_details = os.listdir(folder_name) if os.path.exists(folder_name) else[]
        if teachers_details:
            for teacher in teachers_details:
                print(teacher)
        else:
                print("No teacher record at the moment")
                
    @staticmethod
    def teacher_info(name):
        file_name = f"{name}.json"
        folder_name = "Teachers folder"
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = json.load(file)
                print("Here is the teacher info:")
                print(content)
		  
                  			
											
																		
																	
																
																	
																
																
															
													
												
											
											
							
							
							
					
				
		
			
			
		
		
	
	
	
		
		
		
			
		
	
		


