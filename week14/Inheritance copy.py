class Animal:
    def __init__(self,name,age,color):
        self.__name = name
        self.__age = age
        self.__color = color
    def showinfo(self):
        return f"ชื่อ {self.__name} อายุ {self.__age} ปี สี {self.__color}"


class Dog(Animal):
    def __init__(self, name, age, color,race):
        super().__init__(name, age, color)
        self.__race = race
    def showdog(self):
        return f"หมาพันธ์ {self.__race} มี {super().showinfo()}"

dog1 = Dog("พี",12,'ขาว','ซี๊ด')
print(dog1.showdog())