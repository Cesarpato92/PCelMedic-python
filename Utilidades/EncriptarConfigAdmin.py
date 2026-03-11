import bcrypt
import os

def hash_password(plain_password):
    # Encripta una contraseña usando bcrypt
    password_bytes = plain_password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def convertir_config():
    # Buscar el archivo .configAdmin
    ruta_actual = os.path.dirname(__file__)
    ruta_config = os.path.join(os.path.dirname(ruta_actual), '.configAdmin')
    
    # Leer el archivo actual
    try:
        with open(ruta_config, 'r') as f:
            lineas = f.readlines()
        
        usuario = None
        password = None
        
        for linea in lineas:
            if linea.startswith('USER='):
                usuario = linea.strip().split('=', 1)[1]
            elif linea.startswith('PASSWORD='):
                password = linea.strip().split('=', 1)[1]
        
        if not usuario or not password:
            print("Error: No se encontró USER o PASSWORD en el archivo")
            return
      
        print(f"Usuario: {usuario}")
        print(f"Contraseña actual (texto plano): {password}")
        
        # Encriptar la contraseña
        password_hash = hash_password(password)
        
        # Crear backup del archivo original
        backup = ruta_config + '.backup'
        os.rename(ruta_config, backup)
        print(f"Backup creado: {backup}")
        
        # Escribir nuevo archivo con contraseña encriptada
        with open(ruta_config, 'w') as f:
            f.write(f"USER={usuario}\n")
            f.write(f"PASSWORD={password_hash}\n")
        
        # Cambiar permisos (solo lectura/escritura para el usuario)
        os.chmod(ruta_config, 0o600)
        
        print("\n Archivo .configAdmin actualizado con contraseña encriptada")
        print("El archivo original se guardó como .configAdmin.backup")
        
    except FileNotFoundError:
        print(f" No se encontró el archivo .configAdmin en {ruta_config}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convertir_config()