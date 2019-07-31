#!/usr/bin/env python3

import socket
import os

port = 65000        # The port used by the server


def send_task(_task):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            send = input('Enter Message: ').strip()
            s.sendall(str.encode(send))
            if send.lower() == 'exit':
                print('Programme Terminated')
                break


def client():
    global port

    try:
        send_task()
    except ConnectionRefusedError:
        port += 10
        client()
    except KeyboardInterrupt:
        print('Programme Terminated')


def main():
    global host

    os.system('clear')
    print("================== Welcome to Client Platform ===================")
    host = input('Server IP: ').strip()  # The server's hostname or IP address
    client()


if __name__ == "__main__":
    main()

