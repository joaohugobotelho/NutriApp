def calcular_tmb(peso, altura, idade):
    return(10 * peso) + (0.25 * altura) - (5 * idade) + 5

#def calcular_manutencao(tmb, fator_atividade):
    return tmb * fator_atividade


#def calorias_objetivo(calorias_manutencao, objetivo):
    if objetivo == "emagrecer":
        return calcular_manutencao - 300
    
    elif objetivo == "massa":
        return calorias_manutencao + 300
    
    else:
        return calorias_manutencao

def fator_atividade(nivel):
    fatores = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'intenso': 1.725
    }
    return fatores.get(nivel,1.2)

def ajustar_calorias(calorias_manutencap, objetivo, tipo_deficit):

    if objetivo == "manter":
        return calorias_manutencap
    if objetivo == "massa":
        return calorias_manutencap + 300
    if objetivo == "emagrecer":

        if tipo_deficit == "leve":
            return calorias_manutencap - 300
        
        elif tipo_deficit == "emagrecer":
            return calorias_manutencap - 500
        
        elif tipo_deficit == "agressivo":
            return calorias_manutencap - 700
        
    return calorias_manutencap

def calcular_calorias_usuario(usuario):
    tmb = calcular_tmb(usuario.peso, usuario.altura, usuario.idade)
    manutencao = tmb * fator_atividade(usuario.atividade)
    return ajustar_calorias(manutencao, usuario.onjetivo, usuario.tipo_deficit)