import socket
import time
import binascii
hostname, port = '34.243.97.41', 8510

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        client.connect((hostname, port))
    except ConnectionRefusedError:
        print("Connection refused, retryng...")
        time.sleep(1)
        continue
    except TimeoutError:
        print("Connection timeout, retryng...")
        time.sleep(1)
        continue
    except OSError:
        print("Connection timeout, retryng...")
        time.sleep(1)
        continue

    data = ''
    while True:
        try:
            client.sendall(b'\xDE\xAD\xFA\xCE' * 3000000)
            print("SENT!")
            time.sleep(1)
        except ConnectionResetError:
            print("Connection reset, retryng...")
            time.sleep(1)
            break
        except TimeoutError:
            print("Connection timeout, retryng...")
            time.sleep(1)
            continue
        except ConnectionRefusedError:
            print("Connection refused after connect, retryng...")
            time.sleep(1)
            break
        except ConnectionAbortedError:
            print("Connection aborted, retryng connection")
            time.sleep(1)
            break
