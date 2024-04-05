'''
Leia um vetor A de N elementos e escreva um vetor B de N elementos, conforme a seguinte condição:
se índice de A[índice] é par então B[índice] = 0, caso contrário B[índice] = 1.
'''
def main():
    vetor_a = [int(i) for i in input('Digite os elementos: ').split()]
    vetor_b = []

    for item in vetor_a:
        vetor_b.append(0) if item % 2 == 0 else vetor_b.append(1)
    print(vetor_b)

main()
