from database import collection
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

user = {
    "name": "sahil",
    "email": "sahil@example.com",
    "hashedPassword": password_hash.hash("user123"),
    "role": "user"
}

admin = {
    "name": "admin",
    "email": "admin@example.com",
    "hashedPassword": password_hash.hash("admin123"),
    "role": "admin"
}

# collection.insert_many([user, admin])