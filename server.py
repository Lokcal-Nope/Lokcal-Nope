import sys
import time
import socket
import asyncio
import function


def socket_server():
    key_psw = 1093
    # 处理缓存
    temp_data = ""
    for i in function.data_reader("data/information.data"):
        i = int(i) - key_psw
        temp_data += chr(i)

    # 创建一个socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定socket到ip和端口
    ip = function.data_reader("data/server.data")[0]
    port = function.data_reader("data/server.data")[1]
    server_socket.bind((ip, port))

    # 设置最大连接数
    server_socket.listen(10)

    # 储存数据
    user_normal = {"TestUser": "000000"}
    user_inside = {"Lokcal-Nope": "lokcal794613"}
    code_inside = {"Lokcal-Nope": "v#0001dxc"}

    print("\n【Socket Server】【2.1v】")
    print(f"Server is running on 【IP {ip}】【Port {port}】\n")
    print("TEMP DATA:")

    # 加载缓存
    temp = ""
    for i in temp_data:
        if i == "\n":
            temp += "$"
        else:
            temp += i
        print(temp)
    print("\n")

    while True:
        # 接受一个新的连接
        client_socket, client_address = server_socket.accept()

        # 接收客户端发送的数据
        received_data = client_socket.recv(1024).decode()

        #  假设数据是 str, str 格式，分解并分析
        try:
            key, value = received_data.split(", ")
            user_normal[str(key)] = str(value)
            client_socket.sendall(bytes(f"Newly built", 'utf-8'))
            print("We get a command -> New User{normal}")
        except ValueError:
            try:
                key, value, code = received_data.split(", ")
                user_inside[str(key)] = str(value)
                code_inside[str(key)] = str(code)
                client_socket.sendall(bytes(f"Newly built", 'utf-8'))
                print("We get a command -> New User{inside}")
            except ValueError:
                if received_data == "save":
                    data_n = data_i = ""
                    print("We get a command -> Save")
                    data_file = open(r"data/information.data", "w")
                    key_n = user_normal.keys()
                    key_i = user_inside.keys()
                    for i in key_n:
                        value = user_normal[i]
                        data_n += f"{i}, {value}\n"
                    for i in key_i:
                        value = user_inside[i]
                        code = user_inside[i]
                        data_i += f"{i}, {value}, {code}\n"
                    data = f"{data_n}\n{data_i}"
                    list_psw = []
                    for i in data:
                        i = ord(i)
                        list_psw.append((int(i) + key_psw))
                    data_psw = ""
                    for i in list_psw:
                        data_psw += f"{i}\n"
                    data_file.write(data_psw)
                    data_file.close()
                    time.sleep(3)
                    client_socket.sendall(bytes(f"Saved", 'utf-8'))
                    client_socket.close()
                elif received_data == "exit":
                    data_n = data_i = ""
                    print("We get a command -> Exit")
                    print("Save and break")
                    data_file = open(r"data/information.data", "w")
                    key_n = user_normal.keys()
                    key_i = user_inside.keys()
                    for i in key_n:
                        value = user_normal[i]
                        data_n += f"{i}, {value}"
                    for i in key_i:
                        value = user_inside[i]
                        code = user_inside[i]
                        data_i += f"{i}, {value}, {code}"
                    data = f"{data_n}\n{data_i}"
                    list_psw = []
                    for i in data:
                        i = ord(i)
                        list_psw.append((int(i) + key_psw))
                    data_psw = ""
                    for i in list_psw:
                        data_psw += f"{i}\n"
                    data_file.write(data_psw)
                    data_file.close()
                    time.sleep(3)
                    client_socket.sendall(bytes(f"Withdrawn", 'utf-8'))
                    client_socket.close()
                    sys.exit()
                elif received_data == "exit*":
                    print("We get a command -> Forced Closing")
                    print("Exit in three seconds")
                    time.sleep(3)
                    client_socket.sendall(bytes(f"Withdrawn", 'utf-8'))
                    client_socket.close()
                    sys.exit()
                elif received_data == "get information":
                    num = 0
                    data = ""
                    key = user_normal.keys()
                    for i in key:
                        value = user_normal[i]
                        num += 1
                        data += f" ---- {num} {i} {value} \n"
                    client_socket.sendall(bytes(f" -- Normal Users Information: \n{data}", 'utf-8'))
                    print("We get a command -> Information Getting{normal}")
                    # 关闭与客户端的连接
                    client_socket.close()
                elif received_data == "get information*":
                    num = 0
                    data = ""
                    key = user_inside.keys()
                    for i in key:
                        value = user_inside[i]
                        code = code_inside[i]
                        num += 1
                        data += f" ---- {num} {i} {value} {code} \n"
                    client_socket.sendall(bytes(f" -- Inside Users Information: \n{data}", 'utf-8'))
                    print("We get a command -> Information Getting{inside}")
                    client_socket.close()
                else:
                    # 发送确认信息给客户端
                    client_socket.sendall(b'Data stored successfully')

                    #  关闭与客户端的连接
                    client_socket.close()
    server_socket.close()


def http_server():  # 未启用的 Beta [备用方案]
    from http.server import HTTPServer, SimpleHTTPRequestHandler

    def run(server_address):
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print("Running on http://localhost:8000/")
        httpd.serve_forever()

    if __name__ == "__main__":
        from sys import argv

        if len(argv) < 2:
            run(('Localhost', 8000))
        else:
            run((argv[1], 8000))


def asyncio_server():  # 未启用的 Beta [study information]
    async def handle_echo(reader, writer):
        data = await reader.read(1024)  # 异步读取数据
        message = data.decode('utf-8')
        addr = writer.get_extra_info('peer name')
        print(f"Received {message} from {addr}")

        print(f"Sending data back to {addr}")
        writer.write(data)  # 异步发送数据
        await writer.drain()
        print(f"Sent data successfully to {addr}")

        print(f"Closing the connection to {addr}")
        writer.close()  # 关闭连接

    async def main():
        server = await asyncio.start_server(handle_echo, '127.0.0.1', 8000)

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()

    asyncio.run(main())


socket_server()
