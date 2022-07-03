alto = int(input("Alto: "))

for a in range(alto):
    for b in range(alto):
        if b <= a:
            print("*", end="")
        if b == a:
            print("")


