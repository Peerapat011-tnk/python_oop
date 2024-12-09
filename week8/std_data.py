class Std:
    def __init__(self,std_name,std_id,std_grades={},std_scores={}):
        self.name = std_name
        self.id = std_id
        self.grades = std_grades
        self.scores = std_scores
       
    def edit(self):
        while True :
            select = str(input("เลือกวิชา : "))
            if select == "all":
                score["Math"]=int(input("ใส่คะแนนคณิตศาสตร์ : "))
                grade = self.Grades(score) 
                self.grades["Math"] = grade

                self.scores["Thai"]=int(input("ใส่คะแนนภาษาไทย : "))
                grade = self.Grades(score) 
                self.grades["Thai"] = grade

                self.scores["English"]=int(input("ใส่คะแนนอังกฤษ : "))
                grade = self.Grades(score) 
                self.grades["English"] = grade

                self.scores["Sci"]=int(input("ใส่คะแนนวิทยาศาสตร์ : "))
                grade = self.Grades(score) 
                self.grades["Sci"] = grade

                self.scores["SS"]=int(input("ใส่คะแนนสั่งคมศึกษา : "))
                grade = self.Grades(score) 
                self.grades["SS"] = grade

            elif select == "Math":
                self.scores["Math"]=int(input("ใส่คะแนนคณิตศาสตร์ : "))
                grade = self.Grades(score) 
                print(grade)
                self.grades["Math"] = grade

            elif select == "Thai":
                score = int(input("ใส่คะแนนภาษาไทย : "))
                grade = self.Grades(score) 
                self.grades["Thai"] = grade

            elif select == "English":
                self.scores["English"]=int(input("ใส่คะแนนอังกฤษ : "))
                grade = self.Grades(score) 
                self.grades["English"] = grade

            elif select == "Sci" :
                self.scores["Sci"]=int(input("ใส่คะแนนวิทยาศาสตร์ : "))
                grade = self.Grades(self.scores) 
                self.grades["Sci"] = grade

            elif select == "SS":
                self.scores["SS"]=int(input("ใส่คะแนนสั่งคมศึกษา : "))
                grade = self.Grades(self.scores) 
                self.grades["SS"] = grade

            else :
                print("สิ้นสุด")
                break

    def Grades(self,score):
        if score >= 80 :
            grade = 4
        elif score >= 70 :
            grade = 3
        elif score >= 60 :
            grade = 2
        elif score >= 50 :
            grade = 1
        elif score >= 0 :
            grade = 0
        return grade
  
std1 = Std("สมปอง",68447)
std1.edit()
print(std1.grades)



