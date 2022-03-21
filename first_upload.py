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
            if i==j:
                temp.append(1)
            else:
                temp.append(0)
        result.append(temp)
        temp = []
    return result

def createMatrix():
    x=[]
    y=[]
    s=int(input("enter the size rows matrix:"))
    p=int(input("enter the size cols matrix:"))
    for i in range(s):
        for j in range(p):
            t=int(input("enter number:"))
            y.append(t)
        x.append(y)
        y=[]
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

def ChangeMatrix(x):
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
                            x = multiplymatrix(k, x)
                            print("L is:", x)
                            z = 1
                            break
#no zero
    for i in range(len(x)):
        for j in range(len(x)):
            if i==j:
                y=unit_matrix(len(x))
                y[i][j]=(1/x[i][j])
                x=multiplymatrix(y,x)#after the change pivot is 1
                print("1 changing",x)
            else:
                y=unit_matrix(len(x))
                y[j][i]=(x[j][i]/x[i][i])*(-1)
                x=multiplymatrix(y,x)
                print("2 ->",x)
            with open("file5.txt",'a') as f:
                f.write(str(x))
                f.write("\n")












#matrix(unit_matrix(3),createMatrix())
#(arr[i][j]/arr[j][j])*(-1)


#x=createMatrix()
x=[[1,0,-5],[8,-4,-5],[-1,3,0]]
f=open("file5.txt",'w')
f.close()
ChangeMatrix(x)
