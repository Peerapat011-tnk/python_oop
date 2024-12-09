a = {'Name': 'Test', 'Page': 399},{'Name': 'Test2', 'Page': 499}

find = str(input("ใส่ชื่อหนังสือที่ต้องการค้นหา : "))
for i in a:
    if i['Name'] == find:
        print("พบหนังสือ ",i)