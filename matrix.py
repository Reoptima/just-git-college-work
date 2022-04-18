def Matrix():
    try:
        a = int(input("Кол-во столбцов в матрице: "))
        b = int(input("Кол-во строк в матрице: "))
        c = int(input("Начальное число: "))
        d = int(input("Шаг: "))
        matrix = []
        for i in range(b):
            matrix.append([])
            for j in range(a):
                matrix[i].append(c)
                c += d
        for i in range(b):
            for j in range(a):
                print(matrix[i][j], end = " ")
            print("")
    except Exception:
        print("Ошибка ввода данных")