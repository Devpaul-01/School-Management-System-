import random 
import os 
import bcrypt
import json 
from datetime import datetime

class Quiz:
    def __init__(self):
        self.quiz_questions =  {
        "mathematics": [
        {
            "question": "What is 15 × 8?",
            "options": {"A": "110", "B": "120", "C": "130"},
            "correct_answer": "B"
        },
        {
            "question": "Solve for x: 3x + 7 = 22",
            "options": {"A": "x = 4", "B": "x = 5", "C": "x = 6"},
            "correct_answer": "B"
        },
        {
            "question": "What is the area of a circle with radius 5cm? (Use π = 3.14)",
            "options": {"A": "78.5 cm²", "B": "31.4 cm²", "C": "15.7 cm²"},
            "correct_answer": "A"
        },
        {
            "question": "What is 2³ + 4²?",
            "options": {"A": "22", "B": "24", "C": "26"},
            "correct_answer": "B"
        },
        {
            "question": "If a triangle has angles 60°, 70°, what is the third angle?",
            "options": {"A": "40°", "B": "50°", "C": "60°"},
            "correct_answer": "B"
        },
        {
            "question": "What is 144 ÷ 12?",
            "options": {"A": "11", "B": "12", "C": "13"},
            "correct_answer": "B"
        },
        {
            "question": "What is 25% of 80?",
            "options": {"A": "15", "B": "20", "C": "25"},
            "correct_answer": "B"
        },
        {
            "question": "What is the square root of 64?",
            "options": {"A": "6", "B": "8", "C": "10"},
            "correct_answer": "B"
        },
        {
            "question": "If y = 2x + 3, what is y when x = 4?",
            "options": {"A": "9", "B": "11", "C": "13"},
            "correct_answer": "B"
        },
        {
            "question": "What is the perimeter of a rectangle with length 8cm and width 5cm?",
            "options": {"A": "24cm", "B": "26cm", "C": "28cm"},
            "correct_answer": "B"
        }
    ],
    "english": [
        {
            "question": "Which word is a synonym for 'happy'?",
            "options": {"A": "Sad", "B": "Joyful", "C": "Angry"},
            "correct_answer": "B"
        },
        {
            "question": "What is the past tense of 'run'?",
            "options": {"A": "Runned", "B": "Ran", "C": "Running"},
            "correct_answer": "B"
        },
        {
            "question": "Which sentence is grammatically correct?",
            "options": {"A": "She don't like apples", "B": "She doesn't like apples", "C": "She doesn't likes apples"},
            "correct_answer": "B"
        },
        {
            "question": "What type of word is 'quickly'?",
            "options": {"A": "Noun", "B": "Adjective", "C": "Adverb"},
            "correct_answer": "C"
        },
        {
            "question": "Which is the correct spelling?",
            "options": {"A": "Recieve", "B": "Receive", "C": "Receve"},
            "correct_answer": "B"
        },
        {
            "question": "What is the plural of 'child'?",
            "options": {"A": "Childs", "B": "Children", "C": "Childrens"},
            "correct_answer": "B"
        },
        {
            "question": "Which word means the opposite of 'brave'?",
            "options": {"A": "Cowardly", "B": "Strong", "C": "Smart"},
            "correct_answer": "A"
        },
        {
            "question": "What is the comparative form of 'good'?",
            "options": {"A": "Gooder", "B": "Better", "C": "Best"},
            "correct_answer": "B"
        },
        {
            "question": "Which sentence uses correct punctuation?",
            "options": {"A": "Hello, how are you.", "B": "Hello how are you?", "C": "Hello, how are you?"},
            "correct_answer": "C"
        },
        {
            "question": "What part of speech is 'beautiful'?",
            "options": {"A": "Noun", "B": "Adjective", "C": "Verb"},
            "correct_answer": "B"
        }
    ],
    "chemistry": [
        {
            "question": "What is the chemical symbol for water?",
            "options": {"A": "H2O", "B": "CO2", "C": "NaCl"},
            "correct_answer": "A"
        },
        {
            "question": "How many protons does a carbon atom have?",
            "options": {"A": "4", "B": "6", "C": "8"},
            "correct_answer": "B"
        },
        {
            "question": "What is the pH of pure water?",
            "options": {"A": "6", "B": "7", "C": "8"},
            "correct_answer": "B"
        },
        {
            "question": "Which gas makes up about 78% of Earth's atmosphere?",
            "options": {"A": "Oxygen", "B": "Nitrogen", "C": "Carbon dioxide"},
            "correct_answer": "B"
        },
        {
            "question": "What is the chemical formula for table salt?",
            "options": {"A": "NaCl", "B": "KCl", "C": "CaCl2"},
            "correct_answer": "A"
        },
        {
            "question": "What happens to water at 100°C?",
            "options": {"A": "It freezes", "B": "It boils", "C": "It melts"},
            "correct_answer": "B"
        },
        {
            "question": "Which element has the symbol 'Fe'?",
            "options": {"A": "Fluorine", "B": "Iron", "C": "Lead"},
            "correct_answer": "B"
        },
        {
            "question": "What type of bond forms between metals and non-metals?",
            "options": {"A": "Covalent", "B": "Ionic", "C": "Metallic"},
            "correct_answer": "B"
        },
        {
            "question": "How many electrons can the first electron shell hold?",
            "options": {"A": "2", "B": "8", "C": "18"},
            "correct_answer": "A"
        },
        {
            "question": "What is the atomic number of oxygen?",
            "options": {"A": "6", "B": "8", "C": "10"},
            "correct_answer": "B"
        }
    ],
    "physics": [
        {
            "question": "What is the speed of light in vacuum?",
            "options": {"A": "3 × 10⁸ m/s", "B": "3 × 10⁶ m/s", "C": "3 × 10¹⁰ m/s"},
            "correct_answer": "A"
        },
        {
            "question": "What force keeps planets in orbit around the sun?",
            "options": {"A": "Magnetic force", "B": "Gravitational force", "C": "Electric force"},
            "correct_answer": "B"
        },
        {
            "question": "What is the unit of electric current?",
            "options": {"A": "Volt", "B": "Ampere", "C": "Watt"},
            "correct_answer": "B"
        },
        {
            "question": "Which law states 'For every action, there is an equal and opposite reaction'?",
            "options": {"A": "Newton's First Law", "B": "Newton's Second Law", "C": "Newton's Third Law"},
            "correct_answer": "C"
        },
        {
            "question": "What happens to the volume of a gas when temperature increases at constant pressure?",
            "options": {"A": "It decreases", "B": "It increases", "C": "It stays the same"},
            "correct_answer": "B"
        },
        {
            "question": "What is the formula for calculating kinetic energy?",
            "options": {"A": "KE = mgh", "B": "KE = ½mv²", "C": "KE = mc²"},
            "correct_answer": "B"
        },
        {
            "question": "What type of lens is used to correct nearsightedness?",
            "options": {"A": "Convex lens", "B": "Concave lens", "C": "Bifocal lens"},
            "correct_answer": "B"
        },
        {
            "question": "What is the acceleration due to gravity on Earth?",
            "options": {"A": "9.8 m/s²", "B": "10.8 m/s²", "C": "8.9 m/s²"},
            "correct_answer": "A"
        },
        {
            "question": "Which color of light has the longest wavelength?",
            "options": {"A": "Blue", "B": "Green", "C": "Red"},
            "correct_answer": "C"
        },
        {
            "question": "What is the unit of frequency?",
            "options": {"A": "Hertz", "B": "Joule", "C": "Newton"},
            "correct_answer": "A"
        }
    ],
    "bio": [
        {
            "question": "What is the powerhouse of the cell?",
            "options": {"A": "Nucleus", "B": "Mitochondria", "C": "Ribosome"},
            "correct_answer": "B"
        },
        {
            "question": "How many chambers does a human heart have?",
            "options": {"A": "2", "B": "3", "C": "4"},
            "correct_answer": "C"
        },
        {
            "question": "What gas do plants absorb from the atmosphere during photosynthesis?",
            "options": {"A": "Oxygen", "B": "Carbon dioxide", "C": "Nitrogen"},
            "correct_answer": "B"
        },
        {
            "question": "Which blood cells fight infections?",
            "options": {"A": "Red blood cells", "B": "White blood cells", "C": "Platelets"},
            "correct_answer": "B"
        },
        {
            "question": "What is the basic unit of heredity?",
            "options": {"A": "Cell", "B": "Gene", "C": "Chromosome"},
            "correct_answer": "B"
        },
        {
            "question": "Which organ produces insulin?",
            "options": {"A": "Liver", "B": "Pancreas", "C": "Kidney"},
            "correct_answer": "B"
        },
        {
            "question": "How many bones are there in an adult human body?",
            "options": {"A": "196", "B": "206", "C": "216"},
            "correct_answer": "B"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": {"A": "Heart", "B": "Liver", "C": "Skin"},
            "correct_answer": "C"
        },
        {
            "question": "Which part of the plant conducts photosynthesis?",
            "options": {"A": "Root", "B": "Stem", "C": "Leaf"},
            "correct_answer": "C"
        },
        {
            "question": "What type of blood vessel carries blood away from the heart?",
            "options": {"A": "Artery", "B": "Vein", "C": "Capillary"},
            "correct_answer": "A"
        }
    ]}
    #
       
    def save_questions(self):
        folder_name = "Quiz folder"
        file_name = "quiz_questions.json"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            json.dump(self.quiz_questions, file, indent=4)
  
    def validate_subject(self,subject):
        if subject in self.quiz_questions:
            print("Quiz questions found for the subject")
            return self.quiz_questions[subject]
        else:
            print("No quiz registeed for this subject")
            available = list(self.quiz_questions.keys())
            print("Here is the list of available subjects quiz:")
            print(available)
            return None
    @staticmethod
    def check_student(name, pin):
        file_name = f"{name}.json"
        folder_name = "Students folder"
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            print("You are not registered as a student yet kindly register")
            return
        with open(file_path, "r") as file:
            content = json.load(file)
            if pin == content["pin"]:
                if content["fees"]["amount_paid"] > 0:
                    print("You are qualified to to take the quiz examinations")
                    return content
                else:
                    print("You are still yet to pay school fees kindly pay up to take the quiz examinations")
            else:
                print("incorrect password kindly enter a correct password")
    @staticmethod
    def take_quiz(subject, questions, content):
        print("Welcome to the Quiz Section wishing you best of luck")
        n = len(questions)
        name = content["name"]
        level = content["level"]
        result = {"Student_Name": name,
        "Student_Level": level,
        "Quiz_Subject": subject,
        "Gotten_Questions": [],
        "Missed_Questions": []}
        score = 0
        for i in range(n):
            question = questions[i]["question"]
            option = questions[i]["options"]
            answer = questions[i]["correct_answer"]
            print(f"\nQuestion{i+1}  {question}")
            for key, value in option.items():
                print(f"{key}) {value}")
            user = input("Enter the correct option")
            if user.upper() == answer:
                score += 1
                result["Gotten_Questions"].append(question)
            else:
                result["Missed_Questions"].append(question)
        print(f"Well done! You scored {score}/{n}")
        print("Here is your quiz details:")
        result["Total_Score"] = score
        print(result)
        file_name =f"{name}.json"
        folder_name = "Quiz_results"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, "w") as file:
            json.dump(result, file, indent=4)
            print("Quiz Results saved successfully")
            print("Have a nice day")         
    @staticmethod
    def check_subject(subject, content):
        subjects_list = []
        student_subjects = content.get("subjects")
        if not student_subjects:
            print("You are not registered for any subject yet kindly register fully as a new student")
            return 
        for key, value in student_subjects.items():
            subjects_list.append(key)
        if subjects_list:
            if subject in subjects_list:
                print("Congratulations, You are qualified to take to take the quiz examinations")
                print("Best of luck❤️ ")
                return subject
            else:
                print("You are not registered for this subject kindly choose a registered subject")
                if subjects_list:
                    print("Here are the list of subjects you are registered for ")
                    for idx, sub in enumerate(subjects_list):
                        print(f"{idx}+1. {sub}")
            
                           
                           
                    
            
        
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
		pin_bytes = self.pin.encode("utf-8")
		hashed_pin = bcrypt.hashpw(pin_bytes, bcrypt.gensalt()).decode("utf-8")
		content = {
		   "name": self.name,
	       "age": self.age,                 # int or str, but be consistent
	       "pin": hashed_pin,            # NEVER store plain pins in production (hash later)
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
	           stored_hash = content["pin"].encode("utf-8")   # hashed pin from JSON
	           entered_pin = pin.encode("utf-8")
	           if bcrypt.checkpw(entered_pin, stored_hash):
	               print("Login successful")
	               return Student(
	               content["name"],
	               content["age"],
	               pin,  # keep raw pin in memory, not JSON
	               content["role"],
	               content["fees"],
	               content["subjects"],
	               content["level"],
	               content.get("grades", []),
	               content.get("history", []),
	               content.get("ID"))
	           else:
	               print("Incorrect PIN")
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
		pin_bytes = self.pin.encode("utf-8")
		hashed_pin = bcrypt.hashpw(pin_bytes, bcrypt.gensalt()).decode("utf-8")
		content = {
    "name": self.name,
    "age": self.age,
    "pin": hashed_pin,   # save hashed pin
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
    def __init__(self):
        # store only the hash, never the plain password
        self.hashed_pin = "$2b$12$oQsmWD8O7iN8F5zyQT1.xOtJNzicOTwu/W1Dpx6NggWVdLqwC5bwy"

    def check_admin(self, password):
        folder1 = "Students folder"
        folder2 = "Teachers folder"
        entered = password.encode("utf-8")
        stored = self.hashed_pin.encode("utf-8")
        if bcrypt.checkpw(entered, stored):
            print("Admin Login Succesful")
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
		  
                  			
											
																		
																	
																
																	
																
																
															
													
												
											
											
							
							
							
					
				
		
			
			
		
		
	
	
	
		
		
		
			
		
	
		


