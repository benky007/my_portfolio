def decimalToBinary(number):
    if number > 1:
        decimalToBinary(number // 2)
        print(number % 2, end='')



number = int(input("Enter any decimal number: "))

decimalToBinary(number)
