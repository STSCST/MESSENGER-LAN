import socket
import threading

def manejar_cliente(cliente_socket, clientes):
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode('utf-8')
            if mensaje == "/salir":
                print("[DESCONECTADO] Un cliente se desconectó.")
                clientes.remove(cliente_socket)
                cliente_socket.close()
                break
            print(f"[MENSAJE RECIBIDO]: {mensaje}")
            for cliente in clientes:
                if cliente != cliente_socket:
                    cliente.send(mensaje.encode('utf-8'))
        except:
            clientes.remove(cliente_socket)
            cliente_socket.close()
            break

def iniciar_servidor():
    ip_servidor = "0.0.0.0"
    puerto_servidor = 12345
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip_servidor, puerto_servidor))
    servidor.listen(5)

    print(f"[SERVIDOR] Escuchando en {ip_servidor}:{puerto_servidor}")
    clientes = []

    while True:
        cliente_socket, direccion = servidor.accept()
        print(f"[NUEVO CLIENTE] {direccion} conectado.")
        clientes.append(cliente_socket)
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, clientes))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()