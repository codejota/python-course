# Configurações do radar 1
VEL_MAX_RADAR_1 = 60  # Velocidade máxima permitida pelo radar 1
LOCAL_RADAR_1 = 100  # Localização do radar 1
DISTANCIA_DETECCAO_RADAR = 1  # Distância de detecção do radar

# Dados do veículo
velocidade_carro = 61  # Velocidade atual do carro
localizacao_carro = 100  # Localização atual do carro na estrada

# Verificações do radar 1
carro_acima_velocidade = velocidade_carro > VEL_MAX_RADAR_1
carro_na_zona_do_radar = LOCAL_RADAR_1 - DISTANCIA_DETECCAO_RADAR <= localizacao_carro <= LOCAL_RADAR_1 + DISTANCIA_DETECCAO_RADAR
carro_multado = carro_na_zona_do_radar and carro_acima_velocidade

# Resultados das verificações
if carro_acima_velocidade:
    print('Velocidade do carro acima do limite do radar 1.')

if carro_na_zona_do_radar:
    print('Carro passou pela área de detecção do radar 1.')
 
if carro_multado:
    print('Carro multado por excesso de velocidade no radar 1.')
