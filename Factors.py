while True:
    n = int(input("Number: "))
    List = []

    for i in range(n):
        if n % (i+1) == 0:
            List.append((i+1))

    print("Factors: ", end="")
    print(List)
    input("Press Enter...")
    print("")
