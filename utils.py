
def calcular_ritmo_medio(tempo_min, distancia_km):
    total_segundos = tempo_min * 60
    ritmo_seg_km = total_segundos / distancia_km
    minutos = int(ritmo_seg_km // 60)
    segundos = int(ritmo_seg_km % 60)
    return f"{minutos}:{segundos:02d}"

def calcular_vo2max(tempo_min):
    return round(483 / tempo_min + 3.5, 1)

def classificar_zona_vo2(vo2max):
    if vo2max < 30:
        return "Muito baixo"
    elif vo2max < 40:
        return "Baixo"
    elif vo2max < 50:
        return "Moderado"
    elif vo2max < 60:
        return "Bom"
    else:
        return "Excelente"
