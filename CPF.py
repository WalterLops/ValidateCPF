def validateCPF(cpf):
    
    if removeChar(cpf) != False:
        cpf = removeChar(cpf)
    else:
        return False
    
    return bildLastDigit(cpf)  
    
def removeChar (cpf):
    import re
    cnpj = re.sub(r'[^0-9]', '', cpf)
    
    return False if (cnpj == '') else cnpj

def isSequence (cpf):
    return cpf == str(cpf[0]) * len(cpf)

def bildLastDigit(cpf): 
    while True:
        
        novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
        reverso = 10                        # Contador reverso
        total = 0

        # Loop do CPF
        for index in range(19):
            if index > 8:                   # Primeiro índice vai de 0 a 9,
                index -= 9                  # São os 9 primeiros digitos do CPF

            total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

            reverso -= 1                    # Decrementa o contador reverso
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:                   # Se o digito for > que 9 o valor é 0
                    d = 0
                total = 0                   # Zera o total
                novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

        # Evita sequencias. Ex.: 11111111111, 00000000000...
        sequencia = isSequence(cpf)
        
        return True if (cpf == novo_cpf and not sequencia) else False