import socket
import threading

def recibir_mensajes(cliente_socket):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            print(mensaje)
        except:
            print("[DESCONECTADO] El servidor cerró la conexión.")
            break

def iniciar_cliente():
    ip_servidor = input("Ingrese la IP del servidor: ")
    puerto_servidor = 12345

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip_servidor, puerto_servidor))

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    print("[CONECTADO] Escribe '/salir' para desconectarte.")

    hilo = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo.start()

    while True:
        mensaje = input()
        if mensaje == "/salir":
            cliente.send(mensaje.encode('utf-8'))
            cliente.close()
            break
        cliente.send(f"{nombre_usuario}: {mensaje}".encode('utf-8'))

if __name__ == "__main__":
    iniciar_cliente()