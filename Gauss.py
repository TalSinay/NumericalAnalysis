def gauss(matrix,b,parameters):
    newb=[]
    e = 0.00001
    res=[0 for x in matrix]
    prev = [0 for x in matrix]
    for p in permutation(matrix):
        if(checkdiag(p)):
            indexlist = [matrix.index(x) for x in p]
            matrix = p
    for i in indexlist:
        newb.append(b[i])
    while (True):
        for i in range(len(res)):
            tmparr=[]
            for j in range(len(res)):
                if(i==j):
                    continue
                tmparr.append(res[j] * matrix[i][j])
            res[i] = (b[i][0]-sum(tmparr))/matrix[i][i]

        zipedlist = zip([abs(t) for t in res],[abs(r) for r in prev])
        comparelist = [abs(x - y) for (x, y) in zipedlist]
        for indx in range(len(res)):
            print(f" {parameters[indx]} : {res[indx]}  ",end="")
        print()
        if all(e >= v for v in comparelist):
            break
        prev = [x for x in res]


def jacobi(matrix,b,parameters):
    newb = []
    e = 0.00001
    res = [0 for x in matrix]
    prev = [0 for x in matrix]
    for p in permutation(matrix):
        if (checkdiag(p)):
            indexlist = [matrix.index(x) for x in p]
            matrix = p
    for i in indexlist:
        newb.append(b[i])
    while (True):
        for i in range(len(res)):
            tmparr = []
            for j in range(len(res)):
                if (i == j):
                    continue
                tmparr.append(prev[j] * matrix[i][j])
            res[i] = (b[i][0] - sum(tmparr)) / matrix[i][i]

        zipedlist = zip([abs(t) for t in res],[abs(r) for r in prev])
        comparelist = [abs(x - y) for (x, y) in zipedlist]
        for indx in range(len(res)):
            print(f" {parameters[indx]} : {res[indx]}  ", end="")
        print()
        if all(e >= v for v in comparelist):
            break
        prev = [x for x in res]



def checkdiag(matrixA):
    for i in range(len(matrixA)):
        if not (checkrow(matrixA[i],i)):
            return False
    return True


def checkrow(temprow,index):
    check = [abs(x)for x in temprow]
    movil = check[index]
    del check[index]
    if movil>=sum(check):
        return True
    return False


def permutation(lst):
    if len(lst) == 0:
        return []


    if len(lst) == 1:
        return [lst]



    l = []


    for i in range(len(lst)):
        m = lst[i]


        remLst = lst[:i] + lst[i + 1:]


        for p in permutation(remLst):
            l.append([m] + p)
    return l


matrixA = [[2,10,4],[4,2,0],[0,4,5]]
vectorB=[[2],[6],[5]]
parameters = ["x","y","z"]


while(True):

    chioce = input("Press 1 to solve with gauss an 0 for jacobi: \n")
    if(chioce == '1'):
        print("solution by gauss")
        gauss(matrixA,vectorB,parameters)
        break
    if (chioce == '0'):
        print("solution by Jacobi")
        jacobi(matrixA, vectorB,parameters)
        break