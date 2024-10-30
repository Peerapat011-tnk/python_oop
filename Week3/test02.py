class Studen:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def showgrade(self):
        score = self.score
        if score >= 50:
            print(f"name {self.name} pass")
        else :
            print(f"name {self.name} don't pass")

student1 = Studen("somchay",70)
student2 = Studen("somying",15)

student1.showgrade()