def main():
    while True:
        try:
            a = abs(int(input("Введите номер задания(1-3), 0 - Выход \n")))
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
