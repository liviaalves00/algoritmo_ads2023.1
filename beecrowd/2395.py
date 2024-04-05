def main():
    A, B, C = map(int, input().split())
    X, Y, Z = map(int, input().split())

    container = verificar_container(A, B, C, X, Y, Z)

    print(container)

def verificar_container(A, B, C, X, Y, Z):
    return int(X / A) * int(Y / B) * int(Z / C)

main()