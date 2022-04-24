# Jacobi and Guass methods eliminations

# A function that attempts to make a matrix a dominant diagonal by switching rows if necessary
# params: matrix
def make_dominant(m):
    for i in range(len(m)):
        sum1 = sum(map(abs, m[i]))
        for j in range(len(m)):
            if abs(m[i][j]) > sum1 - abs(m[i][j]):
                t = m[j]
                m[j] = m[i]
                m[i] = t
    sum2 = 0
    countA = 0
    countB = 0
    for i in m:
        for j in i:
            if (countA != countB):
                sum2 = sum2 + abs(j)
            countB = countB + 1
        countB = 0
        if (abs(m[countA][countB] < sum2)):
            print("The matrix has no dominant diagonal")
            return False
        countA += 1
        return True


# jacobi method
# params: matrix,vector
def jacobi_method(m, v):
    eps = 0.00001  # Accuracy with epsilon
    x_i = 0
    y_i = 0
    z_i = 0
    if (make_dominant(m)):
        print("#####Jecobi iterations#####")
        x_i_j = x_i + 1
        prev_x = x_i
        while (abs(x_i_j - prev_x) > eps):
            x_i_j = (v[0] - y_i * m[0][1] - z_i * m[0][2]) / m[0][0]  # Isolation of variable X
            y_i_j = (v[1] - x_i * m[1][0] - z_i * m[1][2]) / m[1][1]  # Isolation of variable Y
            z_i_j = (v[2] - x_i * m[2][0] - y_i * m[2][1]) / m[2][2]  # Isolation of variable Z
            prev_x = x_i
            x_i = x_i_j
            y_i = y_i_j
            z_i = z_i_j
            print("##x##y##z")
            print(x_i_j, y_i_j, z_i_j)
    else:
        print("The matrix has no dominant diagonal, we will try to perform 10 iterations")
        x_i = 0
        y_i = 0
        z_i = 0
        x_i_j = x_i + 1
        prev_x = x_i
        for i in range(10):
            x_i_j = (v[0] - y_i * m[0][1] - z_i * m[0][2]) / m[0][0]  # Isolation of variable X
            y_i_j = (v[1] - x_i * m[1][0] - z_i * m[1][2]) / m[1][1]  # Isolation of variable Y
            z_i_j = (v[2] - x_i * m[2][0] - y_i * m[2][1]) / m[2][2]  # Isolation of variable Z
            k = x_i
            x_i = x_i_j
            y_i = y_i_j
            z_i = z_i_j
            print("##x##y##z")
            print(x_i_j, y_i_j, z_i_j)


# gauss seidal method
# params: matrix,vector
def GuassSeidal_method(m, v):
    eps = 0.00001  # Accuracy with epsilon
    x_i = 0
    y_i = 0
    z_i = 0
    if (make_dominant(m)):
        print("#####Guass iterations#####")
        x_i_j = x_i + 1
        prev_x = x_i
        y_i_j = 0
        z_i_j = 0
        while (abs(x_i_j - prev_x) > eps):
            prev_x = x_i_j
            x_i_j = (v[0] - y_i_j * m[0][1] - z_i_j * m[0][2]) / m[0][0]  # Isolation of variable X
            y_i_j = (v[1] - x_i_j * m[1][0] - z_i_j * m[1][2]) / m[1][1]  # Isolation of variable Y
            z_i_j = (v[2] - x_i_j * m[2][0] - y_i_j * m[2][1]) / m[2][2]  # Isolation of variable Z
            print("##x##y##z")
            print(x_i_j, y_i_j, z_i_j)
    else:
        print("The matrix has no dominant diagonal, we will try to perform 10 iterations")
        x_i_j = x_i + 1
        prev_x = x_i
        y_i_j = 0
        z_i_j = 0
        for i in range(10):
            prev_x = x_i_j
            x_i_j = (v[0] - y_i_j * m[0][1] - z_i_j * m[0][2]) / m[0][0]  # Isolation of variable X
            y_i_j = (v[1] - x_i_j * m[1][0] - z_i_j * m[1][2]) / m[1][1]  # Isolation of variable Y
            z_i_j = (v[2] - x_i_j * m[2][0] - y_i_j * m[2][1]) / m[2][2]  # Isolation of variable Z
            print("##x##y##z")
            print(x_i_j, y_i_j, z_i_j)


# Main
def program(m, v):
    print("choose your option\nfor Jacobi press 1\nfor Gauss press 2")
    flag = input()
    if (flag == "1"):
        jacobi_method(m, v)
        print("To continue the program press 1\nfor EXIT press any button")
        flag2 = input()
        if (flag2 == "1"):
            program(m, v)
        else:
            print("Gooodbay")
            exit()
    elif (flag == "2"):
        GuassSeidal_method(m, v)
        print("To continue the program press 1\nfor EXIT press any button")
        flag2 = input()
        if (flag2 == "1"):
            program(m, v)
        else:
            print("Gooodbay")
            exit()
    else:
        print("wrong input,try again")
        program(m, v)



matrixA = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
vectorB = [2, 6, 5]


program(matrixA, vectorB)
