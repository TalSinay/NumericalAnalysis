import random
'''
def machinePrecision(f=float):
    machine=f(1)
    while f(1)+f(machine)!=f(1):
        new_machine=machine
        machine=f(machine)/f(2)
    return new_machine

print("before:",abs(3.0*(4.0/3.0-1)-1))
print("after:",abs(3.0*(4.0/3.0-1)-1)-machinePrecision())

def Rand(list):
    x=random.choice(list)
    return x
'''


def unit_matrix(n):
    result = []
    temp = []
    for i in range(n):
        for j in range(n):
            if i == j:
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
        temp = []
    return result

def createMatrix():
    x=[]
    y=[]
    rows=int(input("enter the size rows matrix:"))
    cols=int(input("enter the size cols matrix:"))
    for i in range(rows):
        for j in range(cols):
            num=int(input("enter number:"))
            y.append(num)
        x.append(y)
        y=[]
    return x

def createVector():
    x = []
    y = []
    rows = int(input("enter the size rows matrix:"))
    cols = 1
    for i in range(rows):
        for j in range(cols):
            num = int(input("enter number:"))
            y.append(num)
        x.append(y)
        y = []
    return x


def multiplymatrix(x,y):
    result = []
    temp = []
    for i in range(len(x)):
        for i in range(len(y[0])):
            temp.append(0)
        result.append(temp)
        temp = []

    # iterate through rows of X
    for i in range(len(x)):
   # iterate through columns of Y
        for j in range(len(y[0])):
       # iterate through rows of Y
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]

    return result

def ChangeMatrix(x, vectorB):
    z = 1
    while z == 1:
        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if i == j and x[i][j] == 0:
                    for y in range(len(x)):
                        if x[y][j] != 0:
                            k = unit_matrix(len(x))  # change i with y
                            k[i], k[y] = k[y], k[i]
                            old=x
                            x = multiplymatrix(k, x)
                            vectorB=multiplymatrix(k, vectorB)
                            printAsMatrix(x, vectorB, k,old)
                            z = 1
                            break
#no zero
    for i in range(len(x)):
        for j in range(len(x)):
            if i==j:
                y=unit_matrix(len(x))
                y[i][j]=(1/x[i][j])
                oldMatrix = x
                vectorB=multiplymatrix(y, vectorB)
                x=multiplymatrix(y,x)#after the change pivot is 1
                printAsMatrix(x, vectorB, y,oldMatrix)
            else:
                y=unit_matrix(len(x))
                y[j][i]=(x[j][i]/x[i][i])*(-1)
                oldMatrix=x
                vectorB = multiplymatrix(y, vectorB)
                x=multiplymatrix(y,x)
                printAsMatrix(x, vectorB, y, oldMatrix)




def printAsMatrix(x,b,k,old):
    with open("file5.txt", 'a') as f:
        for i in range(len(x)):
            print("E-->",k[i],"old-->",old[i],"= A-->",x[i],"b->",b[i])
            f.write("E-->"+ str(k[i])+ "\t\told A-->"+ str(old[i])+ "\t\t= A after the change-->"+ str(x[i])+ "\t\tthe vector b ->"+ str(b[i]))
            f.write("\n")
        f.write("----------------------------------------------------------------------------------------------------------------\n")
        print("-----------------------")

def rand():
    x=input("enter number : ")
    a=input("enter number of choices :")
    return int((x)%a)+1

x=[[1,-2,-2],[2,0,3],[1,1,3]]
b=[[-2],[4],[4]]
f=open("file5.txt",'w')
f.close()
printAsMatrix(x,b,unit_matrix(3),x)
ChangeMatrix(x,b)


