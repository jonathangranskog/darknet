import socket
import os
import struct

HOST = 'localhost'
PORT = 8007
image_folder = "../Downloads/yolo_semi_large_test_set_v3/images/"
images = os.listdir(image_folder)
images = [image_folder + image for image in images]

def send_image(image, s):
    with open(image, 'rb') as f:
        bytez = f.read()
        size = len(bytez)
        print(size);
        s.sendall(str(size).encode())
        answer = s.recv(4096)
        print('Answer =', answer.decode())

        if answer.decode().startswith("Got it"):
            s.sendall(bytez)
            answer = s.recv(4096)
            print('Answer =', answer.decode())
            if answer.decode().startswith("Got image"):
                print(image, "successfully sent")
                answer = s.recv(12)
                print('Answer =', answer.decode())
                if answer.decode().startswith("Predictions"):
                    i = 0
                    while True:
                        answer = s.recv(64)
                        i += 1
                        prediction = answer.decode().split('\n')[0]
                        print(prediction)
                        if prediction.startswith("NO MORE"):
                            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for image in images:
        send_image(image, s)
    
    s.sendall(str.encode("STOP"));

    s.close()
