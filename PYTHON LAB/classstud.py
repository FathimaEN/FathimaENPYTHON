class Student:
     def __init__(self,rlno,name):
          self.rlno=rlno
          self.name=name
     def display(self):
         print("roll no:",self.rlno)
         print("name",self.name)
#main
stud1=Student(10,"athira")
stud1.display()
