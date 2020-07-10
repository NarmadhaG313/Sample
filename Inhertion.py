class Student:
    def __init__(self,fname,id):
        self.fname=fname
        self.id=id
        
    def display(self,ph):
        print(self.fname)
        print(self.id)
        print(self.ph)
    
class Parent(Student):
    def __init__(self,fname,id):
        super().__init__(fname,id)
        
    def display(self,ph):
        self.ph=ph
        super().display(ph)
        
P=Parent("John",1212)
P.display(6365489)
