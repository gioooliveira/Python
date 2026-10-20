# Gerar senha segura ( letras + digitos + pontuação)
import secrets
import string
alfabeto = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(secrets.choice(alfabeto) for i in range (8))
print(f"Senha Aleatoria: {senha}")
