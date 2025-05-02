from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    hash = generate_password_hash(password, salt_length=25)
    return hash