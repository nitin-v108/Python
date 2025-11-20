while (True):
    try:
        a = int(input("Enter first value: "))
        b = int(input("Enter second value: "))
        o = input("Enter operation (+,-,/,*) = ")
        match o:
            case "+":
                print(f"O/P = {a + b}")
            case "-":
                print(f"O/P = {a - b}")
            case "*":
                print(f"O/P = {a * b}")
            case "/":
                print(f"O/P = {a / b}")
            case default:
                print("Something wrong!!")
    except:
        print("Error, Please try again...")


