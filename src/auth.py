import flet as ft
import bcrypt 
import socket
import rsa 
import subprocess
import threading

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

def exchange_keys(public_key):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.39", 8888))

    message = str.encode(public_key, "utf-8")

    client.sendall(message)
    print(f"Public key sent to server: {message}")
    print(f"Awaiting public key from server...")

    server_public_key = client.recv(1024).decode()
    print(f"Server public key received: {server_public_key}")

    client.close()

    return server_public_key

    


# structure and setup
def main(page: ft.Page):
    page.title = "Link"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 600
    page.window_resizeable = True
    page.padding = 20

    server_public_key = exchange_keys(public_key)


    def decrypt(private_key):
        pass

    # ecnrypt data to prepare for transport (one object) I can then decrypt and parse the object data on server and do something based on it
    def encrypt(username:bytes, password_hash:bytes, server_public_key):
        # combine user and pass bytes into one object and encrypt it then call the send data function. 
        # REFER TO VIDEO
        creds_object = username + str.encode(":", "utf-8") + password_hash
        enc_object = server_public_key.encrypt()
        pass
        

        client_to_server(enc_object)
        


    # send creds to the server to be checked.        
    def client_to_server(encrypted_object):
        try:
            
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("192.168.1.39", 9999)) # find ip of server downstairs and put the server.py script on it to lisen on 9999.
            
            message = encrypted_object

            
            client.sendall(message)
            
            print(f"payload sent to server: {message}")
            print("Awaiting response...")

            response = client.recv(1024).decode()
            print(f"Server response: {response}")

            client.close()


        except Exception as e:
            print(e)


    
    # creds handler functions
    def prepare_creds(password:str, username:str) -> bytes:
        password_hash_bytes = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
        username_bytes = str.encode(username, "utf-8")
        # print(username_bytes) # test
        # print(password_hash_bytes) # test
        encrypt(username_bytes, password_hash_bytes, server_public_key)
        

    # login and register functions
    def login(e: ft.Event[ft.FilledButton]):
        username = username_input.value
        password = password_input.value

        prepare_creds(password, username)
        

    def register(e: ft.Event[ft.FilledButton]):
        username = username_input.value
        password = password_input.value

        prepare_creds(password, username)
        
    

    # input fields for username (email) and password (these widgets are my 2 objects that i want to appear on the auth page)
    username_input = ft.TextField(
        label="Username",
        hint_text="user@example.com",
    )

    password_input = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
    )

    # buttons 
    login_button = ft.FilledButton(
        content="Login",
        icon=ft.Icons.LOGIN,
        on_click=login,
    )

    register_button = ft.FilledButton(
        content="Register",
        icon=ft.Icons.APP_REGISTRATION,
        on_click=register,
        
    )

    # create the main UI -> containers
    page.add(
        ft.Column([
            ft.Text(
                "Login or register below",
                size=28,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,              
            ),
            ft.Divider(height=20),

            username_input,
            password_input,

            ft.Row([
                login_button,
                register_button,
            ]),
            
        

        ])
    )















# run
if __name__ == '__main__':
    ft.run(main)