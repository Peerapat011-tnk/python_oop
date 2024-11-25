class Cat:
    def __init__(self,ชื่อ,อายุ,เพศ,สี):
        self.name = ชื่อ
        self.age = อายุ
        self.sex = เพศ
        self.color = สี
    def old(self):
        self.age +=1

cat1 = Cat("สีหมอก",2,"ผู้","ขาว")
cat2 =Cat("ส้ม",219,"ผู้","ส้ม")
cat2.name="ส้มใหญ่"
cat2.old()

print(cat2.age) 
print(cat2.name)