import bcrypt

# Definir las contraseñas a hashear
passwords = [
    "password1",
    "password2"
]

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

for password in passwords:
    hashed_password = hash_password(password)
    print(f"Original: {password} -> Hashed: {hashed_password}")
