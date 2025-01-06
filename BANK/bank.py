class Bank:
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.balance = balance
    def Deposit(self,amount):
        if amount >= 100 :
            self.balance += amount
        else:
            print("ใส่ยอดเงิน 100 บาทขึ้นไป")
    def Drawdeposit(self,draw):
        if draw >= 100 :
            self.balance -= draw
id1 = Bank(1,"Guitar",5000)
while True:
    print("----------bank-----------")
    c = int(input("ดูยอดเงินกด1 ฝากเงินกด2 ถอนเงินกด3 เสร็จสินกด4"))
    if c == 1:
        print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
    elif c==2:
        amount = int(input("ใส่จำนวนเงิน"))
        id1.Deposit(amount)
        print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
    elif c ==3:
        draw = int(input("ใส่จำนวนเงิน"))
        id1.Drawdeposit(draw)
        print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
    else:
        break

id1.deposit(300)
print(f'เงินของ {id1.name} มีอยู่ {id1.balance} บาท')
    