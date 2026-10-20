# Gerar token hexadecimal seguro (bomm para uRLS)

import secrets
import string

token = secrets.token_hex(16)
print(f"token hex:{token}")