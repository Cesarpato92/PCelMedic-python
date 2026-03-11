import bcrypt
import os

class ManejadorPassword:
    
    @staticmethod
    def hash_password(plain_password):
        # Encripta una contraseña usando bcrypt
        try:
            # Convertir a bytes y generar hash
            password_bytes = plain_password.encode('utf-8')
            salt = bcrypt.gensalt(rounds=12)
            hashed = bcrypt.hashpw(password_bytes, salt)
            return hashed.decode('utf-8')
        except Exception as e:
            print(f"Error al encriptar: {e}")
            return None
    
    @staticmethod
    def verificar_password(plain_password, hashed_password):
        # Verifica si la contraseña coincide con el hash
        try:
            password_bytes = plain_password.encode('utf-8')
            hashed_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hashed_bytes)
        except Exception as e:
            print(f"Error al verificar: {e}")
            return False
        
    @staticmethod
    def leer_config(ruta_archivo):
        #Lee el archivo de configuración y devuelve usuario y hash
        try:
            config = {}
            with open(ruta_archivo, 'r') as f:
                for linea in f:
                    if '=' in linea:
                        key, value = linea.strip().split('=', 1)
                        config[key] = value
            return config.get('USER', ''), config.get('PASSWORD', '')
        except FileNotFoundError:
            return None, None
        except Exception as e:
            print(f"Error al leer: {e}")
            return None, None