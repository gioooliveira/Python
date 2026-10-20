import secrets

# Gera um numero seguro entre 0 e 99

numero_seguro = secrets.randbelow(100)
print(f" Número Seguro (0-99):{numero_seguro}")