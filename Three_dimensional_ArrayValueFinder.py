#Millborne A. Galamiton BS-CPE 2B
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
T = int(input("Enter the number of Thickness:")) 

print()
print("Enter the values: ")

el = [[[int(input("> "))for x in range (T)] for y in range (C)] for i in range(R)] 

            
ijk = []
jik = []
print(el)
print()
for i in range(R):#Display the array in ijk order
    for y in range(C):
        for x in range (T):
            print("Index[",i,"] [",y,"]","[",x,"]:",el[i][y][x])
            ijk.append(el[i][y][x])#store in the list ijk
            
print()

for i in range(C):#Display the array in ijk order
    for y in range(R):
        for x in range (T):
            print("Index[",y,"] [",i,"]","[",x,"]:",el[y][i][x])
            jik.append(el[y][i][x])#store in the list jik
            
            
print()
print("Enter the index: ")
l1 = int(input("i >")) #ask the user an integer to locate the element (i)
l2 = int(input("j >"))#ask the user an integer to locate the element (j)
l3 = int(input("k >"))#ask the user an integer to locate the element (k)

for i in range(len(ijk)):
    if el[l1][l2][l3] == ijk[i]:#check if there is match
        print("ijk-ordering(row-major) Element found:","Index[",l1,"][",l2,"][",l3,"]:",el[l1][l2][l3],"is on the",i+1,"position")#display the located position of the element
       
    if el[l1][l2][l3] == jik[i]:#check if there is match
        print("jik-ordering(column-major)Element found:","Index[",l1,"][",l2,"][",l3,"]:",el[l1][l2][l3],"is on the",i+1,"position")#display the located position of the element
       
           
        