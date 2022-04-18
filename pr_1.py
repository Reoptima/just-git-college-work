from logging import exception
import math

def Calculator():
    try:
        operations = ["+", "-", "/", "*", "//", "**", "%", "comb", "Copysign", "ldexp", "Hypot", "PPar", "SPar"]
        a, b = (float(input("Введите число: ")) for i in range(2))
        print("Список операций:")
        for i in range(len(operations)):
            print(operations[i], end=" ")
        operation = input("\nВведите операцию: ")
        match operation:
            case "+":
                print("a + b = ", a + b)
            case "-":
                print("a - b = ", a - b)
            case "/":   
                print("a / b = ", a / b)
            case "*":
                print("a * b = ", a * b)
            case "//":
                print("a // b = ", a // b)
            case "**":
                print("a ** b = ", a ** b)
            case "%":
                print(f"a % b", a % b)
            case "comb":
                print("a comb b = ", math.comb(int(a), int(b)))
            case "Copysign":
                print("a Copysign b = ", math.copysign(a, b))
            case "ldexp":
                print("ldexp(a,b) = ", math.ldexp(int(a), int(b)))
            case "Hypot":
                print("Fabs(a,b) = ", math.hypot(a, b))
            case "PPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: (a + b + d) * 4
                print("PPar(a,b,c) = ", f(a, b, d))
            case "SPar":
                d = float(input("Введите дополнительное значение: "))
                f = lambda a, b, d: ((a * b) + (a * d) + (d * b)) * 2
                print("SPar(a,b,d) = ", f(a, b, d))
    except Exception:
        print("Ошибка ввода данных")

def StrCounter():
    try:
        str = input("Введите строку: ")
        space = str.count(" ")
        comma = str.count(",")
        strlen = len(str)
        print("Количество символов: ", strlen)
        print("Количество пробелов: ", space)
        print("Количество запятых: ", comma)
    except Exception:
        print("Ошибка ввода данных")

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

def main():
    while True:
        try:
            a = int(input("Введите номер задания(1-3), 0 - Выход \n"))
            match a:
                case 1:
                    Calculator()
                case 2:
                    StrCounter()
                case 3:
                    Matrix()
                case 0:
                    break
        except Exception:
            print("Ошибка ввода данных")

if __name__ == "__main__":
    main()