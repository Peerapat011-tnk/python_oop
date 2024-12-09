class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {}
    def Score(self):
        while True:
            selection = str(input("วิชา M T S \n เลือกวิชา:"))
            score = int(input("ใส่คะแนน : "))
            grade = self.Gradecal(score)
            if selection == "M":
                self.grades["Math"] = grade
            elif selection == "T":
                self.grades["Thai"] = grade
            elif selection == "S":
                self.grades["Sci"] = grade
            else :
                break
    def Gradecal(self,score):
        if score >= 80:
            return 4
        elif score >= 70:
            return 3
        elif score >= 60:
            return 2
        elif score >= 50:
            return 1
        else:
            return 0
    def All(self):
        print(f"ชื่อ {self.name} เลขที่ {self.id}/n{self.grades}")
    
std1 = Student("สมปอง","11")
std1.Score()
std1.All()
