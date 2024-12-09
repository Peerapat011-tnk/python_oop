class Libary:
    def __init__(self,page,price):
        self.name = []
        self.page = []
    def add_books(self):
        while True:
            in_book = str(input("ใส่ชื่อหนังสือ or esc เพื่อออก : "))
            if in_book == "esc":
                break
            else:
                self.Bname.append(in_book) 

    def show_books(self):
        i = 0
        for i in range (len(self.Bname)):
            print(self.Bname[i])
            i+=1

    def find_book(self):
        find = str(input("ใส่ชื่อหนังสือที่ต้องการค้นหา : "))
        i = 0
        for i in self.Bname:
            if find == i:
                print(i)
            


user1 = Libary()
user1.show_books()
user1.add_books()
user1.find_book()
        
    