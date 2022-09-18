def matematica(entrada):
    n1 = ''
    n2 = ''
    operadores = ['mais', 'menos', 'vezes', 'multiplicado por', 'dividido por', 'somado a', 'subtraído por', 'subtraido por', '+', '-', '/', ':', 'x', '*']
    for o in operadores:
        if o in entrada:
            operador = o
            for c in range(0, len(entrada)):
                if entrada[c].isnumeric():
                    n1 += entrada[c]
                elif entrada[c].isspace():
                    for c2 in range(c, len(entrada)):
                        if entrada[c2].isnumeric():
                            n2 += entrada[c2]
                    break
        else:
            continue
    n1 = int(n1)
    n2 = int(n2)
    if operador == 'mais' or operador == '+' or operador == 'somado a':
        resultado = n1 + n2 
    elif operador == 'menos' or operador == '-' or operador == 'subtraído por' or operador == 'subtraido por':
        resultado = n1 - n2
    elif operador == 'vezes' or operador == '*' or operador == 'x' or operador == 'multiplicado por':
        resultado = n1 * n2
    elif operador == 'dividido por' or operador == '/' or operador == ':':
        resultado = n1 / n2
    return f'{n1} {operador} {n2} = {resultado}'


def verificar_função(entrada, resposta):
    # Se for uma equação matemática
    if entrada[0].isnumeric() and entrada[-1].isnumeric():
        resultado = matematica(entrada)
        return resultado
    else:
        return resposta
        