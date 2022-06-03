def Linear_interpolation(points, find_point):
    for row in range(len(points) - 1):
        if find_point > points[row][0] and find_point < points[row + 1][0]:
            x1 = points[row][0]
            x2 = points[row + 1][0]
            y1 = points[row][1]
            y2 = points[row + 1][1]
            return (((y1 - y2) / (x1 - x2)) * find_point) + ((y2 * x1 - y1 * x2) / (x1 - x2))

def Lagrange_interpolation(points,find_point):
    sum = 0
    for i in range(len(points)):
        mul = 1
        for j in range(len(points)):
            if i == j:
                continue
            mul = mul * ((find_point-points[j][0]) / (points[i][0] - points[j][0]))
        sum =sum+mul*points[i][1]
    return sum




def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('N must be equals to M')
    new_matrix = []
    while len(new_matrix) < rowsA:
        new_matrix.append([])
        while len(new_matrix[-1]) < colsB:
            new_matrix[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            sum = 0
            for k in range(colsA):
                sum += A[i][k] * B[k][j]
            new_matrix[i][j] = sum
    return new_matrix


def matrix_multiply(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('N must be equals to M')
    new_matrix = []
    while len(new_matrix) < rowsA:
        new_matrix.append([])
        while len(new_matrix[-1]) < colsB:
            new_matrix[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            sum = 0
            for k in range(colsA):
                sum += A[i][k] * B[k][j]
            new_matrix[i][j] = sum
    return new_matrix

def UnitMatrix(matrix):
    Unit = list(range(len(matrix)))
    for i in range(len(Unit)):
        Unit[i] = list(range(len(Unit)))

    for i in range(len(Unit)):
        for j in range(len(Unit[i])):
            Unit[i][j] = 0.0

    for i in range(len(Unit)):
        Unit[i][i] = 1.0
    return Unit


def inverse(matrix):
    new_matrix = UnitMatrix(matrix)
    count = 0
    check = False  # flag
    while count <= len(matrix) and check == False:
        if matrix[count][0] != 0:
            check = True
        count = count + 1
    if check == False:
        print("error please try again")
    else:
        helper = matrix[count - 1]
        matrix[count - 1] = matrix[0]
        matrix[0] = helper
        helper = new_matrix[count - 1]
        new_matrix[count - 1] = new_matrix[0]
        new_matrix[0] = helper

        for x in range(len(matrix)):
            division = matrix[x][x]
            if division==0:
                division=1
            for i in range(len(matrix)):
                matrix[x][i] = matrix[x][i] / division
                new_matrix[x][i] = new_matrix[x][i] / division
            for row in range(len(matrix)):
                if row != x:
                    division = matrix[row][x]
                    for i in range(len(matrix)):
                        matrix[row][i] = matrix[row][i] - division * matrix[x][i]
                        new_matrix[row][i] = new_matrix[row][i] - division * new_matrix[x][i]
    return new_matrix



def Polynomial_interpolation(points,find_point):
    matrix = list(range(len(points)))
    for i in range(len(matrix)):
        matrix[i] = list(range(len(matrix)))
    for row in range(len(points)):
        matrix[row][0] = 1
    for row in range(len(points)):
        for col in range(1, len(points)):
            matrix[row][col] = pow(points[row][0], col)
    new_matrix = list(range(len(points)))
    for i in range(len(new_matrix)):
        new_matrix[i] = list(range(1))
    for row in range(len(new_matrix)):
        new_matrix[row][0]=points[row][1]
    vector= matrix_multiply(inverse(matrix), new_matrix)
    sum = 0
    for i in range(len(vector)):
        if i == 0:
            sum = vector[i][0]
        else:
            sum +=vector[i][0]*find_point ** i

    return sum

def HelpNeville(m, n, points, find_point):
    if m==n:
        return points[m][1]
    new= ((find_point-points[m][0]) * HelpNeville(m + 1, n, points, find_point) - (find_point - points[n][0]) * HelpNeville(m, n - 1, points, find_point)) / (points[n][0] - points[m][0])
    return new


def Neville_interpolation(points,find_point):
    new_matrix = list(range(len(points)))
    for k in range(len(points)):
        new_matrix[k] = list(range(len(points)))

    for i in range(len(points)):
        for j in range(i,len(points)):
            new_matrix[i][j]=HelpNeville(i, j, points, find_point)
    return new_matrix[0][len(points)-1]


def main():
    points=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9589],[6,-0.2794]]
    find_point=2.5
    choice=int(input("in which interpolation do you calculate?\n1-Linear\n2-polynomial\n3-Lagrange\n4-Neville\n"))
    if choice == 1:
        print("======================Linear_interpolation===========================\n")
        print(Linear_interpolation(points,find_point))
    elif choice == 2:
        print("======================Polynomial_interpolation===========================\n")
        print(Polynomial_interpolation(points,find_point))
    elif choice == 3:
        print("======================Lagrange_interpolation===========================\n")
        print(Lagrange_interpolation(points,find_point))
    elif choice == 4:
        print("======================Neville_interpolation===========================\n")
        print(Neville_interpolation(points,find_point))
    else:
        choice = int(input("illegal choice! please try again\n "))




