class Students:    
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):    
        if not (0 <= code_portfolio_score <= 100):  
            raise ValueError("Code Portfolio Score must be between 0 and 100.")  
        if not (0 <= group_project_score <= 100):  
            raise ValueError("Group Project Score must be between 0 and 100.")  
        if not (0 <= exam_score <= 100):  
            raise ValueError("Exam Score must be between 0 and 100.")  
          
        self.name = name    
        self.major = major    
        self.code_portfolio_score = code_portfolio_score    
        self.group_project_score = group_project_score    
        self.exam_score = exam_score    
        
    def print_details(self):    
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, "    
              f"Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")
# Example:
student = Students("Timi", "BMI", 85, 90, 78)  
student.print_details()