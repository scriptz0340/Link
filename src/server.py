import socket
import bcrypt 
import rsa
import psutil
import threading

def ecrypt():
    pass


def kill_process_on_port(port):
    for conn in psutil.net_connections(kind="inet"):
        if conn.laddr.port == port:
            try:
                proc = psutil.Process(conn.pid)

                print(f"Terminating process on port {port}...")
                proc.terminate()

                proc.wait(timeout=3)
            except:
                proc.kill()

# read from database and compare hash to that stored with the user once i have db setup.
def check_pwd(password:str, hash:bytes) -> bool:
    return bcrypt(password.encode(), hash)
  

def exchange_keys(server_public_key):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.39", 8888))
    server.listen(1)
    print("Server is listening for public key on port 8888...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    client_public_key = conn.recv(1024).decode()
    print(f"Received public key from client: {client_public_key} ")

    
    response = f"############## CLIENT PUBLIC KEY RECEIVED! ###############\nServer Public key: {server_public_key}"
    conn.sendall(response.encode())
    print(f"Server sent response: {response}")

    conn.close()
    server.close()

def server_to_client(response_code):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.39", 9999))
    server.listen(1)
    print("Server is listening on port 9999...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    payload = conn.recv(1024).decode()
    print(f"Received payload: {payload}")

    response = "################### PAYLOAD RECEIVED! ##################"
    conn.sendall(response.encode())

    print(f"Server sent response: {response}")

    conn.close()
    server.close()
    

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# listening = True
# while listening:

try:
    exchange_keys(public_key)

    server_to_client()

except Exception as e:
    print(e)



# kill_process_on_port(9999)

