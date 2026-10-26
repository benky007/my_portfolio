def board(positions):
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"
    for i in range(9):
        if positions[i] == "1":
            if i == 1:
                one = "x"
            if i == 2:
                two = "x"
            if i == 3:
                three = "x"
            if i == 4:
                four = "x"
            if i == 5:
                five = "x"
            if i == 6:
                six = "x"
            if i == 7:
                seven = "x"
            if i == 8:
                eight = "x"
            if i == 9:
                nine = "x"
        if positions[i] == "2":
            if i == 1:
                one = "o"
            if i == 2:
                two = "o"
            if i == 3:
                three = "o"
            if i == 4:
                four = "o"
            if i == 5:
                five = "o"
            if i == 6:
                six = "o"
            if i == 7:
                seven = "o"
            if i == 8:
                eight = "o"
            if i == 9:
                nine = "o"
    print("-------------")
    print("")
    print(f"| {one} | {two} | {three} |")
    print("-------------")
    print(f"| {four} | {five} | {six} |")
    print("-------------")
    print(f"| {seven} | {eight} | {nine} |")
    print("")
    print("-------------")


positions = [0, 0, 0, 0, 0, 0, 0, 0, 0]
next = input("\n\nPut in the number position of which you wish to place a cross")

positions[int(next)] = 1


