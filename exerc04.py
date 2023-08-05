def verifica_senha(senha):
    conta_caract = len(senha)
    conta_num = 0
    conta_letras = 0
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pontuacoes = [',', '.', '!', ';', '?', ':']
    conta_pontuacoes = 0

    for caract in senha:
        if caract in numeros:
            conta_num += 1
        if caract.isalpha():
            conta_letras += 1
        if caract in pontuacoes:
            conta_pontuacoes += 1
    
    # return conta_caract, conta_num, conta_letras, conta_pontuacoes

    if conta_caract <= 5:
        return 'Senha Fraca'
    elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes == 0:
        return 'Senha Forte'
    elif conta_letras > 0 and conta_num > 0 and conta_pontuacoes > 0:
        return 'Senha Muito Forte'


resultado = verifica_senha('tes,te1:23')
print(resultado)