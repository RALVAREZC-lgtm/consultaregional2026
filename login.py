import bcrypt
usuarios={'admin':bcrypt.hashpw('123456'.encode(),bcrypt.gensalt())}

def autenticar(usuario,password):
    return usuario in usuarios and bcrypt.checkpw(password.encode(),usuarios[usuario])
