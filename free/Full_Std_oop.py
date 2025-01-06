class Student:
    def __init__(self):
        self.stds = [{'ชื่อ': 'โจทาโร่ คูโจ', 'อายุ': 17, 'รหัสประจำตัว': 1001},
            {'ชื่อ': 'โจเซฟ โจสตาร์', 'อายุ': 68, 'รหัสประจำตัว': 1002},
            {'ชื่อ': 'โนริอากิ คะเคียวอิน', 'อายุ': 17, 'รหัสประจำตัว': 1003},
            {'ชื่อ': 'มูฮัมหมัด อับดุล', 'อายุ': 27, 'รหัสประจำตัว': 1004},
            {'ชื่อ': 'อีกกี้', 'อายุ': 9, 'รหัสประจำตัว': 1005}]
    
    def show_std(self):
        num = 0
        for i in self.stds:
            num+=1
            print(f"{num}. ชื่อ: {i['ชื่อ']}, อายุ: {i['อายุ']} ปี, รหัสประจำตัว: {i['รหัสประจำตัว']}")
    
    def add_std(self):
        std = {}
        std['ชื่อ'] = str(input("กรอกชื่อ-นามสกุล : "))
        std['อายุ'] = int(input("กรอกอายุ : "))
        std['รหัสประจำตัว'] = int(input("กรอกรหัสประจำตัว : "))
        self.stds.append(std)
    def find_std(self):
        search = str(input("ชื่อนักเรียนที่ท่านต้องการค้นหา : "))
        check = 0
        for i in self.stds:
            if search == i['ชื่อ']:
                check += 1
                print(i)
        if check <= 0:
            print("ไม่พบ")
    
    def dlt_std(self):
        dlt = int(input("กรอกรหัสประจำตัวผู้ที่ต้องการลบ : "))
        c = 0
        for i in self.stds:
            if dlt == i['รหัสประจำตัว']:
                print(f"นักศึกษาชื่อ :  {i['ชื่อ']} ถูกลบจากระบบแล้ว ")
                self.stds.remove(i)
                c += 1
        if c <= 0:
            print("ไม่พบรหัสที่ท่านต้องการลบ")
    
    def update_std(self):
        search = str(input("ชื่อนักเรียนที่ท่านต้องการแก้ไข : "))
        check = 0
        for i in self.stds:
            if search == i['ชื่อ']:
                check += 1
                print(f"ชื่อ: {i['ชื่อ']}, อายุ: {i['อายุ']}, รหัสประจำตัว: {i['รหัสประจำตัว']}")
                selection = str(input("ท่านต้องการแก้ไขอะไร : "))
                print(selection ,":",i[selection])
                update = input("ต้องการแก้ไขเป็น : ")
                i[selection] = update
                print("แก้ไขเสร็จสิ้น")
        if check <= 0:
            print("ไม่พบ")

        

user1 = Student()
while True:
    selection = int(input("ท่านต้องดำเนินการเรื่องใด\n1:ดูชื่อนักศึกษาทั้งหมด\n2:ค้นหานักศึกษา\n3:แก้ไขข้อมูล\n4:ลบข้อมูล\n5:เพิ่มชื่อ\n6:จบการทำงาน\nเลือก : "))
    if selection == 1 :
        while True:
            user1.show_std()
            ext = int(input("ดำเนินการต่อกด 1\nกลับไปยังหน้าแรกกด 2 : "))
            if ext != 1:
                break
    elif selection == 2:
        while True:
            user1.find_std()
            ext = int(input("ดำเนินการต่อกด 1\nกลับไปยังหน้าแรกกด 2 : "))
            if ext != 1:
                break
    elif selection ==3:
        while True:
            user1.update_std()
            ext = int(input("ดำเนินการต่อกด 1\nกลับไปยังหน้าแรกกด 2 : "))
            if ext != 1:
                break
    elif selection ==4:
        while True:
            user1.dlt_std()
            ext = int(input("ดำเนินการต่อกด 1\nกลับไปยังหน้าแรกกด 2 : "))
            if ext != 1:
                break
    elif selection ==5:
        while True:
            user1.add_std()
            ext = int(input("ดำเนินการต่อกด 1\nกลับไปยังหน้าแรกกด 2 : "))
            if ext != 1:
                break
    else :
        print("จบโปรแกรม")
        break


        
