
class Std :
    def __init__(self,Name,Nickname,Score):
        self.Name = Name
        self.Nickname = Nickname
        self.Score = Score
    def Test(self):
        import random
        a = random.randint(1, 10)
        self.Score += a
    def result(self):
        if self.Score > 5:
            print(f"{self.Name} : โหด!!!")
        else :
            print(f"{self.Name} : กาก!!!!")

students = [
    Std("ภีรภัทร์ รักหวาน", "ต้า", 0),
    Std("กฤษกร สินกำเนิน", "บีม", 0),
    Std("กนกพล บริพัศ", "โฟกัส", 0),
    Std("สรัลชณา จันทรสุข", "ฟ้า", 0),
    Std("กรกนก เฮ่าตระกูล", "ขิม", 0)
]


while True:
    No = int(input("เลือกนักเรียน  or 0 to stop : "))
    if No == 0 :
        break
    elif 1 <= No <= len(students):
        list_std = students[No - 1]
        Ans = str(input("เริ่มสอบมั้ย y or n : "))
        if Ans == "n" :
            break
        else :
            list_std.Test()
            print(f"ชื่อ : {list_std.Name} \n คะแนน :{list_std.Score} ")
    else :
        print("อย่าเล่นกับระบบ")
        break

for student in students:
    student.result()
    

        
