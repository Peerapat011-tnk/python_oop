class Animal:
    def __init__(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color
    def showinfo(self):
        return f"ชื่อ {self.__name} อายุ {self.__age} ปี สี {self.__color}"
animal1 = Animal('จอจี้',10,'ดำ')
print(f"สัตว์ตัวหนึ่งมี{animal1.showinfo()}")
class Dog(Animal):
    def speak(self):
        return "สุรโฮ่ง"
dog1 = Dog("สมโฮ่ง",2,"ดำ")
print(f"หมาชื่อ {dog1.showinfo()} ร้อง {dog1.speak()}")