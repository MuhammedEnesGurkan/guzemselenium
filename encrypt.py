from cryptography.fernet import Fernet

# Anahtar oluştur
key = Fernet.generate_key()
cipher = Fernet(key)

# Şifrelenecek mesaj
username_token =cipher.encrypt(b"okul numaranız")
password_token = cipher.encrypt(b"şifreniz")
# Mesajı şifrele ve çöz
decrypted_username = cipher.decrypt(username_token)
str_decrypted_usernmae = decrypted_username.decode()
decrypted_pasword= cipher.decrypt(password_token)
str_decrypted_password = decrypted_pasword.decode()
