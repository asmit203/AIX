import socket
import threading

def send_request():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 1234))

    # Send a simple request to the server
    request = b"Hello, server!"
    client.send(request)

    # Receive and print the response from the server
    response = client.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")

    client.close()

if __name__ == "__main__":
    # Create three threads to send requests simultaneously
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=send_request)
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()