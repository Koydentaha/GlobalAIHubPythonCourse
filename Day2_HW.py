## Day 2 Homework
## Q1
'''
list1 = ['İstanbul','Ankara','Balıkesir','Bitlis','Konya','Rize','Kocaeli','Aydın']

L = len(list1) # lenght of the list1
Lm = int(L/2) 
i = 0

listFH = list1[:Lm] #First Half of the list1
listSH = list1[Lm:L] #Second Half of the list1

print(listFH)
print(listSH)

while(i<Lm): ## i<4
    listSH.append(listFH[i]) ## add FH to SH
    i = i+1

listNew = listSH
print(listNew)
'''
##Q2
n = int(input('Please,enter a single digit integer :'))

for i in range(0,n):
    if(i%2==0):
        print(i)


      
 