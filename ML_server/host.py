import socket
import threading

def handle_client(client_socket):
    # This function will be executed in a separate thread for each client
    response = b'30'  # Convert the response to bytes
    client_socket.send(response)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 1234))
    server.listen(5)

    print("[INFO] Server listening on port 1234...")

    while True:
        client, addr = server.accept()
        print(f"[INFO] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()