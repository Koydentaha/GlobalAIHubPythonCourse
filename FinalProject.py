class employess:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.language = ["Turkish"]

    def addLanguage(self,new_lang):
        print("Adding new language")
        self.language.append(new_lang)   

    def showInfo(self):
        print("{} {} is {} years old".format(self.name,self.lastname,self.age))
        print("He can speak:")
        for i in self.language:
              print(i)

class manager(employess):
    def __init__(self,position,):
        self.position = position

manager1 = manager('Müdür')
manager1.name = 'Adem'
manager1.lastname = 'Baba'
manager1.age = 45

emp1 = employess('Taha','Köyden',21)
emp2 = employess('Celal','Çetiner',29)
emp3 = employess('Uğur','Er',22)
emp4 = employess('Berkan','Sekman',25)

emp1.addLanguage("English")
emp2.addLanguage("English")
emp2.addLanguage("German")
emp3.addLanguage("English")
emp3.addLanguage("French")
emp4.addLanguage("English")

emp = [emp1,emp2,emp3,emp4]
j = 1
print("Welcome to Company Management System")
print("-------------------------------------------------")
no = int(input("Please,enter a employee No that you would like to search :"))
if(0<no<5):
    for i in emp:
        if(j==no):
           print(i.showInfo())   
        j = j+1
else :
    print("There is no employes that has this no !!!")