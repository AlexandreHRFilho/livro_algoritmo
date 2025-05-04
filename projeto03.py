#sequencia de collatz
#O problema de Collatz é um problema matemático que envolve uma sequência de números inteiros. A sequência começa com um número inteiro positivo n e segue as seguintes regras:
#1. Se n é par, o próximo número na sequência é n / 2.
#2. Se n é ímpar, o próximo número na sequência é 3n + 1.
#3. A sequência termina quando n se torna 1.
#A conjectura de Collatz afirma que, independentemente do número inicial n, a sequência sempre acabará chegando ao número 1. Embora tenha sido testada para muitos números, ainda não foi provada para todos os inteiros positivos.
#A sequência de Collatz é um exemplo clássico de um problema que é fácil de entender, mas difícil de resolver matematicamente. Ela é frequentemente usada como um exemplo em teoria dos números e em estudos de algoritmos.

def collatz(n):
    if n <= 0:
        raise ValueError("O número deve ser um inteiro positivo.")
    sequencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        sequencia.append(n)
    return sequencia

testes = [-1,0,2, 3, 4, 10, 25, 40, 32, 100, 1000, -5, 0]  # Incluí valores inválidos para teste

for t in testes:
    try:
        print(f"Sequência de Collatz para {t}: {collatz(t)}")
    except ValueError as e:
        print(f"Erro ao calcular a sequência de Collatz para {t}: {e}")