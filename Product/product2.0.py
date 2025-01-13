class Product:
    def __init__(self,name,price,stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def edit_stcock(self):
        estock = int(input("เพิ่มจำนวนสต๊อก"))
        self.__stock += estock
    def edit_price(self):
        eprice = int(input("แก้ไขราคาสินค้า"))
        self.__price += eprice
    def detail(self):
        return (f' สินค้า {self.__name} มีราคา {self.__price} บาท จำนวน {self.__stock} ชิ้น')
    
class Phone(Product):
    def __init__(self, name, price, stock,storage):
        super().__init__(name, price, stock)
        self.storage = storage
    def show_phone(self):
        return f"{super().detail()} ความจุ {self.storage} GB"
    
class Laptop(Product):
    def __init__(self, name, price, stock,spec):
        super().__init__(name, price, stock)
        self.spec = spec
    def show_laptop(self):
        return f"{super().detail()} เสปค {self.spec}"
class clothes(Product):
    def __init__(self, name, price, stock,size):
        super().__init__(name, price, stock)
        self.size = size
    def show_clothes(self):
        return f"{super().detail()} ไซส์ {self.size}"
    

P1 = Phone("i15 pro",35000,20,256)
print(P1.show_phone())
P2 = Laptop("asus 15 pro",25000,5,"i5 12th rtx8090 ")
print(P2.show_laptop())
P3 = clothes("dress",20,20,"M")
print(P3.show_clothes())

P1.edit_stcock()
P1.edit_price()
print(P1.show_phone())
