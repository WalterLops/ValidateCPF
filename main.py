import CPF

cpf = '16899535009'

cpf = input('Digite um CPF: ')

if CPF.validateCPF(cpf):
    print()
    print("CPF válido")
    print()
else:
    print()
    print("CPF inválido")
    print()