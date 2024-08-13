import socket
import json

def clienteStub(endereco, porta, argumentos):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((endereco, porta))  # Conexão

        mensagem = json.dumps(argumentos)  # Processo de serialização
        s.sendall(mensagem.encode())  # Envio e processo de codificação

        # Situação bloqueante até reply do servidor
        mensagemResposta = s.recv(1024)  # Recebe informações do servidor

        if not mensagemResposta: # Protocolo para garantir que a mensagem do servidor exista
            raise ValueError("Resposta vazia recebida do servidor")

        resultado = json.loads(mensagemResposta.decode())  # Processo de decodificação e desserialização
        return resultado

# Exemplo de autenticação e operação
credenciais = {"username": "admin", "password": "1234"}
operacao = {"op": "adicionar", "tarefa": "Almoçar"}

# Unindo as credenciais com a operação
argumentos = {**credenciais, **operacao}

# stub cliente finalizado
procedimentoRemoto = clienteStub('localhost', 65000, argumentos)

print("Resultado do procedimento remoto 1: ", procedimentoRemoto)
