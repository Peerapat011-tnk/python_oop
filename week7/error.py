while True:
    try :
        a = 5 
        b = int(input("ใส่เลขครับอ้าย : "))
        if b < 0:
            raise Exception
        
        c = a/b
        print(c)

    except ValueError:
        print("ใส่เฉพาะเลข")
    except ZeroDivisionError:
        print("ห้ามใส่0")
    except:
        print("อื่นๆ")
