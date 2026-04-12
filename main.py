consumo_diario = []

print("Entrada de dados de consumo (30 dias):")


for i in range(30):
    
    
    print("Dia", i + 1)
    
    
    valor_digitado = input("Digite o consumo: ")
    
    
    consumo = float(valor_digitado)
    
    
    consumo_diario.append(consumo)



total = 0  

for valor in consumo_diario:
    
  
    total = total + valor



quantidade_dias = len(consumo_diario)

media = total / quantidade_dias


maior_valor = consumo_diario[0]
dia_maior = 1


for i in range(0, len(consumo_diario)):
    
    valor_atual = consumo_diario[i]
    
    
    if valor_atual > maior_valor:
       
       maior_valor = valor_atual
       dia_maior = i + 1





menor_valor = consumo_diario[0]
dia_menor = 1


for i in range(0, len(consumo_diario)):
    
    valor_atual = consumo_diario[i]
    
    
    if valor_atual < menor_valor:
        
        menor_valor = valor_atual
        dia_menor = i + 1





contador_aumento = 0


for i in range(1, len(consumo_diario)):
    
    valor_atual = consumo_diario[i]
    valor_anterior = consumo_diario[i - 1]
    
    # Verifica se aumentou
    if valor_atual > valor_anterior:
        
        contador_aumento = contador_aumento + 1



print("------------------------------")
print("RELATÓRIO FINAL")
print("------------------------------")

print("Consumo Total:", round(total, 2), "kWh")
print("Média de Consumo:", round(media, 2), "kWh")

print("Maior consumo:")
print("Valor:", round(maior_valor, 2), "kWh")
print("Dia:", dia_maior)

print("Menor consumo:")
print("Valor:", round(menor_valor, 2), "kWh")
print("Dia:", dia_menor)

print("O consumo aumentou", contador_aumento, "vezes em relação ao dia anterior")
