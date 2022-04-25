def gauss(matrix,b,parameters):
    newb=[]
    maxiter = 100
    existdiagonal = False
    e = 0.00001
    res=[0 for x in matrix]
    prev = [0 for x in matrix]
    for p in permutation(matrix):
        if(checkdiag(p)):
            indexlist = [matrix.index(x) for x in p]
            matrix = p
            existdiagonal = True
            break
    if existdiagonal:
        for i in indexlist:
            newb.append(b[i])
    else:
        print("No dominant diagonal")
    iternum = 1
    for itr in range(maxiter):
        for i in range(len(res)):
            tmparr=[]
            for j in range(len(res)):
                if(i==j):
                    continue
                tmparr.append(res[j] * matrix[i][j])
            res[i] = (b[i][0]-sum(tmparr))/matrix[i][i]

        zipedlist = zip([abs(t) for t in res],[abs(r) for r in prev])
        comparelist = [abs(x - y) for (x, y) in zipedlist]
        print(f"{iternum} ) ", end="")
        for indx in range(len(res)):
            print(f" {parameters[indx]} : {res[indx]}  ",end="")
        print()
        iternum += 1
        if all(e >= v for v in comparelist):
            return
        prev = [x for x in res]

    print("The system of equations does not converge")


def jacobi(matrix,b,parameters):
    newb = []
    maxiter = 100
    existdiagonal = False
    e = 0.00001
    res = [0 for x in matrix]
    prev = [0 for x in matrix]
    for p in permutation(matrix):
        if (checkdiag(p)):
            indexlist = [matrix.index(x) for x in p]
            matrix = p
            existdiagonal = True
            break
    if existdiagonal:
        for i in indexlist:
            newb.append(b[i])
    else:
        print("No dominant diagonal")

    iternum = 1
    for itr in range(maxiter):
        for i in range(len(res)):
            tmparr = []
            for j in range(len(res)):
                if (i == j):
                    continue
                tmparr.append(prev[j] * matrix[i][j])
            res[i] = (b[i][0] - sum(tmparr)) / matrix[i][i]

        zipedlist = zip([abs(t) for t in res],[abs(r) for r in prev])
        comparelist = [abs(x - y) for (x, y) in zipedlist]
        print(f"{iternum} ) ", end="")
        for indx in range(len(res)):
            print(f" {parameters[indx]} : {res[indx]}  ", end="")
        print()
        iternum+=1
        if all(e >= v for v in comparelist):
            return
        prev = [x for x in res]

    print("The system of equations does not converge")



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


matrixA = [[4,2,0],[2,10,4],[0,4,5]]
vectorB=[[2],[6],[5]]
parameters = ["x","y","z"]

while(True):
    # parameters = input("Enter the parameters :\n for example XYZ if the first parameter is X the second is Y...\n")
    # parameters = list(parameters)
    # print(parameters)
    chioce = input("Press 0 to solve with gauss an 1 for jacobi: \n")
    if(chioce == '0'):
        print("solution by gauss")
        gauss(matrixA,vectorB,parameters)
        break
    if (chioce == '1'):
        print("solution by Jacobi")
        jacobi(matrixA, vectorB,parameters)
        break
