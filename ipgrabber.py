import socket

def obter_endereco_ip():
    try:
        host = input("Digite o nome de domínio: ")
        endereco_ip = socket.gethostbyname(host)
        print(f"{host} ---> {endereco_ip}")
    except socket.gaierror:
        print("Erro ao obter o endereço IP. Certifique-se de fornecer um nome de domínio válido.")

if __name__ == "__main__":
    obter_endereco_ip()


