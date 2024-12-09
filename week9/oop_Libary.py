class Library:
    def __init__(self):
        self.Books = [{'Name': 'Test','Writer':'Tatata', 'Page': 399, 'Price': 299}]
    def add_books(self):
        book = {}
        book['Name'] = str(input("ใส่ชื่อหนังสือ : "))
        book['Writer'] = str(input("ใส่ชื่อผู้แต่ง : "))
        book['Page'] = int(input("ใส่จำนวนหน้า : "))
        book['Price'] = str(input("ใส่ราคา : "))
        self.Books.append(book)

    def show_books(self):
        i = 0 
        for i in self.Books:
            print(i)

    def find_book(self):
        find = str(input("ใส่ชื่อหนังสือที่ต้องการค้นหา : "))
        for i in self.Books:
            if i['Name'] == find:
                print(i)
            else :
                print("ไม่มีหนังสือที่คุณค้นหา")

user1 = Library()
while True:
    choice = int(input("ต้องการทำอะไร\n1:เพิ่มหนังสือ\n2:ดูหนังสือทั้งหมด\n3:ค้นหาหนังสือ\n4:ออก\n : "))
    if choice == 1:
        while True:
            user1.add_books()
            a = int(input("อีกครั้ง กด:1 : "))
            if a != 1:
                break
    elif choice == 2:
        user1.show_books()
        b = int(input("ดำเนินการต่อกด:1 : "))
        if b != 1:
            break
    elif choice == 3:
        while True:
            user1.find_book()
            c = int(input("ดำเนินการต่อกด:1 : "))
            if c != 1:
                break
    else : 
        break

    





