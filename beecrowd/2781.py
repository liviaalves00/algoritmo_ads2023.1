def main():
     L, C, lajes1, lajes2 = input().split()

    lajes1 = (L * C) + ((L - 1) * (C - 1))
    lajes2 = ((L - 1) * 2) + ((C - 1) * 2)
    print(f"%d\n", lajes1)
    print(f"%d\n", lajes2)

main()