class animals:
    def __init__(self,genus,leg,habitat):
        self.genus = genus
        self.leg = leg
        self.habitat = habitat

class dogs(animals):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def showInfo(self):
        print("It's name is {} and {} years old.".format(self.name,self.age))
        print("It's genus is {}.It has {} legs and lives on the {}.".format(self.genus,self.leg,self.habitat))

class cats(animals):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def showInfo(self):
        print("It's name is {} and {} years old.".format(self.name,self.age))
        print("It's genus is {}.It has {} legs and lives on the {}.".format(self.genus,self.leg,self.habitat))


dog1 = dogs("Mex",3)
dog1.genus = "Canis"
dog1.leg = "4"
dog1.habitat = "land"

dog2 = dogs("Karabaş",1)
dog2.genus = "Canis"
dog2.leg = "4"
dog2.habitat = "land"

dog3 = dogs("Akkurt",5)
dog3.genus = "Canis"
dog3.leg = "4"
dog3.habitat = "land"

cat1 = cats("Pamuk",2)
cat1.genus = "Felis"
cat1.leg = "4"
cat1.habitat = "land"

cat2 = cats("Haydar",2)
cat2.genus = "Felis"
cat2.leg = "4"
cat2.habitat = "land"

cat3 = cats("Kara",4)
cat3.genus = "Felis"
cat3.leg = "4"
cat3.habitat = "land"

dogs = [dog1,dog2,dog3]
cats = [cat1,cat2,cat3]

j = 1
k = 1

print("Welcome to our website")
print("-------------------------------")
slct = int(input("Enter a number\nFor Dogs : 1\nFor Cats : 2\n"))

if(slct==1):
    print("Mex : 1\nKarabaş : 2\nAkkurt : 3")
    d = int(input("Which dog would you like to know about :"))
    for i in dogs:
        if(j==d):
            print(i.showInfo())
        j = j+1    
        if(d<1 and d>3):
            print("There is no dog that you are looking on our website")

elif(slct==2):
    print("Pamuk : 1\nHaydar : 2\nKara : 3")
    c = int(input("Which cat would you like to know about :"))
    for i in cats:
        if(k==c):
            print(i.showInfo())
        k = k+1    
        if(c<1 and c>3):
            print("There is no cat that you are looking on our website")
else:
    print("Wrong Number !!!")            