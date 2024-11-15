import socket
import time

import function

ip = function.data_reader("data/server.data")[0]
port = function.data_reader("data/server.data")[1]


def client_code_poster(code_information):
    # 创建一个socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 定义服务器的IP地址和端口
    server_address = (ip, port)

    # 连接到服务器
    client.connect(server_address)

    # 发送指令到服务器
    message = bytes(f"{code_information}", 'utf-8')  # 使用bytes发送数据
    client.sendall(message)

    # 接收返回值
    try:
        # 接收数据
        data = client.recv(1024)  # Buffer size 1024 bytes
        if data:
            information = data.decode()
            print(information)
        else:
            print('No information received')
    except socket.error as socket_error:
        print(socket_error)
    client.close()


def client_normal_user(username, password):
    global ip, port

    # 创建一个socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 定义服务器的IP地址和端口
    server_address = (ip, port)

    # 连接到服务器
    client.connect(server_address)

    # 发送指令到服务器
    message = bytes(f"{username}, {password}", 'utf-8')  # 使用bytes发送数据
    client.sendall(message)

    # 接收返回值
    try:
        # 接收数据
        data = client.recv(1024)  # Buffer size 1024 bytes
        if data:
            information = data.decode()
            print(information)
        else:
            print('No information received')
    except socket.error as socket_error:
        print(socket_error)
    client.close()


def client_inside_user(username, password, usercode):
    global ip, port

    # 创建一个socket对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 定义服务器的IP地址和端口
    server_address = (ip, port)

    # 连接到服务器
    client.connect(server_address)

    # 发送指令到服务器
    message = bytes(f"{username}, {password}, {usercode}", 'utf-8')  # 使用bytes发送数据
    client.sendall(message)

    # 接收返回值
    try:
        # 接收数据
        data = client.recv(1024)  # Buffer size 1024 bytes
        if data:
            information = data.decode()
            print(information)
        else:
            print('No information received')
    except socket.error as socket_error:
        print(socket_error)
    client.close()
