class Std:
    def __init__(self,std_name,std_id):
        self.name = std_name
        self.id = std_id
        self.grades = {}
        self.scores = {}
       
    def edit(self):
        score = int(input('ใส่คะแนน '))
        grade = self.Grades(score) 
        return grade
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
print(std1.edit())



