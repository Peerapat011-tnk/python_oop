class Cat:
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        print(self.name,"meow!!!")

mycat1 = Cat("ส้มจิ๋ว","ส้ม")
mycat2 = Cat("ส้มม่วง","สามสี")

print(mycat1.name)
print(mycat2.name)
mycat1.cry()