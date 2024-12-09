class Student:
    def __init__(self,std_name,std_id,std_age):
        self.name = std_name
        self.id = std_id
        self.age = std_age
        self.grade = {}
    def editGrade(self):
        self.grade["Math"]= int(input("ใส่เกรดคณิตศาสตร์ : "))
        self.grade["Tahi"]= int(input("ใส่เกรดภาษาไทย : "))
        self.grade["Eng"]= int(input("ใส่เกรดภาษาอังกฤษ : "))
        self.grade["Sci"]= int(input("ใส่เกรดวิทยาศาสตร์ : "))
        self.grade["SS"]= int(input("ใส่เกรดสังคม : "))
        print(self.grade)
        print(f"เกรดเฉลี่ย = {sum(self.grade.values)/len(self.grade)}")
        

std1 = Student("สมปอง","785","19")
std1.editGrade()

