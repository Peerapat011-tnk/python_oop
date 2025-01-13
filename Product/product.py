class Product:
    def __init__(self):
        self.__Product = [{'ชื่อสินค้า': 'พัดลม', 'ราคา': 250, 'สต๊อก': 105},
            {'ชื่อสินค้า': 'ปากกา3d', 'ราคา': 450, 'สต๊อก': 99},
            {'ชื่อสินค้า': 'พาวเวอร์แบงค์', 'ราคา': 2250, 'สต๊อก': 50}]
        
    def Add_Product(self):
        product = {}
        product['ชื่อสินค้า'] = str(input("กรอกชื่อสินค้า : "))
        product['ราคา'] = int(input("กรอกราคา : "))
        product['สต๊อก'] = int(input("กรอกจำนวนที่เหลือ : "))
        self.__Product.append(product)
    
    def ShowProduct(self):
        num = 0
        for i in self.__Product:
            num+=1
            print(f"{num}. ชื่อ: {i['ชื่อสินค้า']}, ราคา: {i['ราคา']} บาท, จำนวนที่เหลือ: {i['สต๊อก']} ชิ้น")
    
    def Edit_Product(self):
        search = str(input("ชื่อสินค้าที่ท่านต้องการแก้ไข : "))
        check = 0
        for i in self.__Product:
            if search == i['ชื่อสินค้า']:
                check += 1
                print(f"ชื่อ: {i['ชื่อสินค้า']}, ราคา: {i['ราคา']} บาท, จำนวนที่เหลือ: {i['สต๊อก']} ชิ้น")
                selection = str(input("ท่านต้องการแก้ไขอะไร : "))
                print(selection ,":",i[selection])
                update = input("ต้องการแก้ไขเป็น : ")
                i[selection] = update
                print(f"ชื่อ: {i['ชื่อสินค้า']}, ราคา: {i['ราคา']} บาท, จำนวนที่เหลือ: {i['สต๊อก']} ชิ้น")
                print("แก้ไขเสร็จสิ้น")
        if check <= 0:
            print("ไม่พบ")


U = Product()
while True:
    selection = int(input(" ดูสินค้า กด1\nแก้ไขข้อมูล กด 2 \nเพิ่มสินค้า กด3"))
    if selection == 1:
        U.ShowProduct()
    elif selection == 2:
        U.Edit_Product()
    elif selection ==3:
        U.Add_Product()
    else:
        break