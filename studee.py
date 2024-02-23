#A program to build a simple student management system using python that can do the following:
#Accept, Display,Delete, Update

class Students():
    def __init__(self):
        self.students = ["Mark", "Shiundu", "Sam", "Kelop","Precious", "Lihavi", "Caleb", "Mosi", "Milicent", "Omanga", "Arnold", "Mutwiri", "Grace", "Kendi"] 
        self.form4a = ["milan", "Carl", "Mike", "Arnold"]
        global milan, carl, mike, arnold
        milan = "Name : Milan \nAge : 17 \nadmno : 1341 \nGrade :"
        carl = "\n\nName : Carl \nAge : 19 \nadmno : 1342 \nGrade :"
        mike = "\n\nName : Mike \nAge : 16 \nadmno : 1343 \nGrade :"
        arnold = "\n\nName : Arnold \nAge : 18 \nadmno : 1345 \nGrade :"
    def prompt(self):
        option = int(input("Enter option number[1.Display info, 2.Enter amrks] : "))   
        if option == 1:
            student1.displayinfo()
        elif option == 2:
            student1.modify()        
    def displayinfo(self):    
        self.info = int(input("Enter admno of student to display[1341,1342,1343,1345] ; "))
        if self.info == 1341:
            print(milan)
        elif self.info == 1342:
            print(carl)
        elif self.info == 1343:
            print(mike)
        elif self.info == 1345:
            print(arnold)                
    def modify(self):
        self.info = int(input("Enter admno of student to modify[1341, 1342, 1343, 1345] ; "))
        if self.info == 1341:
            student1.milano()
        elif self.info == 1342:
            studens1.carlo()
        elif self.info == 1343:
            student1.mikeo()
        elif self.info == 1345:
            student1.arnoldo()       
    def milano(self):        
        milan = "Name : Milan \nAge : 17 \nadmno : 1341 \nGrade :"
        newgrade = float(input("Enter marks(milan) : "))
        if newgrade  < 50:
            milan +='F'
        elif newgrade  < 60:
            milan +='D'
        elif newgrade  < 70:
            milan +='C'
        elif newgrade < 80:
            milan +='B'
        else:
            milan +='A' 
        print(milan)        
    def carlo(self):  
        carl = "\n\nName : Carl \nAge : 19 \nadmno : 1342 \nGrade :"
        newgrade = float(input("Enter marks(carl): "))
        if newgrade  < 50:
            carl +='F'
        elif newgrade  < 60:
            carl +='D'
        elif newgrade  < 70:
            carl +='C'
        elif newgrade < 80:
            carl +='B'
        else:
            carl +='A'  
        print(carl) 
    def mikeo(self):
        mike = "\n\nName : Mike \nAge : 16 \nadmno : 1343 \nGrade :"
        newgrade = float(input("Enter marks(mike) : "))
        if newgrade  < 50:
            mike +='F'
        elif newgrade  < 60:
            mike +='D'
        elif newgrade  < 70:
            mike +='C'
        elif newgrade < 80:
            mike +='B'
        else:
            mike +='A'  
        print(mike)
    def arnoldo(self):
        arnold = "\n\nName : Arnold \nAge : 18 \nadmno : 1345 \nGrade :"
        newgrade = float(input("Enter marks(arnold) : "))
        if newgrade  < 50:
            arnold +='F'
        elif newgrade  < 60:
            arnold +='D'
        elif newgrade  < 70:
            arnold +='C'
        elif newgrade < 80:
            arnold +='B'
        else:
            arnld += 'A'
        print(arnold)    


student1 = Students()   
student1.prompt()     
