import random


def data_reader(file_name):
    if file_name == "server.data":
        mode = 0
        ip = ""
        port = ""
        file = open(r"data\server.data", "r")
        data = file.readlines()
        for var in data:
            mode += 1
            for word in var:
                try:
                    int(word)
                except ValueError:
                    if word == "." and mode != 1:
                        ip += word
                    else:
                        continue
                else:
                    if mode != 1:
                        ip += word
                    else:
                        port += word
        information = (ip, int(port))
    elif file_name == "information.data":
        code = ""
        information = []
        file = open(r"data\information.data", "r")
        data = file.readlines()
        for var in data:
            for word in var:
                try:
                    int(word)
                except ValueError:
                    pass
                else:
                    code += word
            information.append(code)
            code = ""
    else:
        information = "File Error"
    return information


def dynamic_password():
    d_psw = ""
    letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'G', 'g',
               'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
               'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    words = ['@', '#', '$', '&', '%', '/', '*', '?']
    for var in range(10):
        letter = letters[random.randint(0, 51)]
        word = words[random.randint(0, 7)]
        number = str(random.randint(0, 9))
        lwn = random.randint(1, 3)
        if lwn == 1:
            d_psw += letter
        elif lwn == 2:
            d_psw += word
        else:
            d_psw += number
    return d_psw
