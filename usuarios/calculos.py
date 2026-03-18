from alimentos.models import Alimentos

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

def ajustar_calorias(calorias_manutencao, objetivo, tipo_deficit):

    if objetivo == "manter":
        return calorias_manutencao
    if objetivo == "massa":
        return calorias_manutencao + 300
    if objetivo == "emagrecer":

        if tipo_deficit == "leve":
            return calorias_manutencao - 300
        
        elif tipo_deficit == "emagrecer":
            return calorias_manutencao - 500
        
        elif tipo_deficit == "agressivo":
            return calorias_manutencao - 700
        
    return calorias_manutencao

def calcular_calorias_usuario(usuario):
    tmb = calcular_tmb(usuario.peso, usuario.altura, usuario.idade)
    manutencao = tmb * fator_atividade(usuario.atividade)
    return ajustar_calorias(manutencao, usuario.objetivo, usuario.tipo_deficit)


def calcular_macros(usuario):
    calorias = calcular_calorias_usuario(usuario)

    peso = usuario.peso

    proteina = peso * 2
    gordura = peso * 0.8

    calorias_proteina = proteina * 4
    calorias_gordura = gordura * 9

    calorias_restantes = calorias - (calorias_proteina + calorias_proteina)

    carbo = calorias_restantes / 4

    return {
        'proteina': round(proteina, 1),
        'gordura': round(gordura, 1),
        'carbo': round(carbo, 1)
    }

def montar_dieta(usuario):
    calorias = calcular_calorias_usuario(usuario)
    macros = calcular_macros(usuario)

    

    dieta = []

    proteina_alimentos = Alimentos.objects.filter(categoria='proteina').first()
    carbo_alimentos = Alimentos.objects.filter(categoria='carbo').first()
    gordura_alimentos = Alimentos.objects.filter(categoria= 'gordura').first()

    if proteina_alimentos:
        qtd_proteina = macros['proteina'] / proteina_alimentos.proteina
        dieta.append({
            'nome': proteina_alimentos.nome,
            'quantidade': round(qtd_proteina * 100, 0),
            'calorias': proteina_alimentos.calorias
        })

    if carbo_alimentos:
        qtd_carbo = macros['carbo'] / carbo_alimentos.carboidrato
        dieta.append({
            'nome': carbo_alimentos.nome,
            'quantidade': round(qtd_carbo * 100, 0),
            'calorias': carbo_alimentos.calorias
        })

    if gordura_alimentos:
        qtd_gordura = macros['gordura'] / gordura_alimentos.gordura
        dieta.append({
            'nome':gordura_alimentos.nome,
            'quantidade': round(qtd_gordura * 100, 0),
            'calorias': gordura_alimentos.calorias
        })

    return dieta