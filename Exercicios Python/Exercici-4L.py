def analisar_margem(faturamento, custo):
    margem = (faturamento - custo) / faturamento
    if margem >= 0.30:
        return "Margem Saudavel"
    else:
        return "Margem Baixa "

print(analisar_margem(1000, 6000))