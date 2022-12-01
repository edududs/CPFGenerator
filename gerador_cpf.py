from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10
total = 0
for i in range(19):
    if i > 8:
        i -= 9

    total += int(novo_cpf[i]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

digi = novo_cpf[9:11]


def fatiador_cpf(string):
    temporario = [string[i:i + 3] for i in range(0, 9, 3)]
    base = '.'.join(temporario)
    digito = string[-(len(string) % 3):]
    return base + '-' + digito


# cpf_format = ''
#
# for iii, iter in enumerate(novo_cpf):
#     cpf_format += iter
#     if iii == 2 or iii == 5:
#         cpf_format += '.'
#     if iii == 8:
#         cpf_format += '-'

print(novo_cpf)
print(fatiador_cpf(novo_cpf))
