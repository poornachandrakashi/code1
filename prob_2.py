#Write a program with class emplaoyee that keeps a track of the number of employess in an organisation and store their name,destination and salary details.
class Employee():
    total=0
    def __init__(self,name,designation,salary):
        Employee.total+=1
        self.name=name
        self.designation=designation
        self.salary=salary

    def employess_count():
        print("There are %d employess"%Employee.total)

    def display():
        print("Name:",self.name,"Designation:",self.designation,"Salary",self.salary)


e1=Employee("Poornachandra","CEO",1000000000000000000000000000)
e2=Employee("Sanjay","Sr.Engineer",580000)
e2=Employee("Sadhhfc","Sjjdr.Engineer",580000)
e2=Employee("Sa","secdjfjh",580000)
e1.display()