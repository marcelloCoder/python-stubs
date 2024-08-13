import socket
import json

# "Banco de dados" simulado de tarefas e autenticações
tarefas = []
users = {"admin": "1234"}  # Dicionário de usuários e senhas
auth_attempts = {}  # Contagem de tentativas de autenticação
auth_log = []  # Registro de autenticações realizadas

MAX_ATTEMPTS = 3  # Número máximo de tentativas permitidas

def autenticar(username, password):
    if username in auth_attempts and auth_attempts[username] >= MAX_ATTEMPTS:
        return "Bloqueado: Muitas tentativas de autenticação"

    if username in users and users[username] == password:
        auth_log.append(f"Usuário {username} autenticado com sucesso.")
        auth_attempts[username] = 0  # Reset da contagem de tentativas
        return "Autenticado"
    else:
        auth_attempts[username] = auth_attempts.get(username, 0) + 1
        if auth_attempts[username] >= MAX_ATTEMPTS:
            return "Bloqueado: Muitas tentativas de autenticação"
        return "Falha na autenticação"

def addTarefa(tarefa):
    tarefaDesc = {"id": len(tarefas) + 1, "tarefa": tarefa}
    tarefas.append(tarefaDesc)
    return f"Tarefa: '{tarefa}' adicionada com sucesso"

def removeTarefa(idTarefa):
    for tarefa in tarefas: 
        if tarefa["id"] == idTarefa:
            tarefas.remove(tarefa)
            return f"Tarefa: '{tarefa['tarefa']}' removida com sucesso"
    return "ID não identificado"

def listTarefa():
    if not tarefas:
        return "Nenhuma tarefa encontrada"
    return tarefas

def servidorStub(porta):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", porta))  # Vincula o servidor a um endereço e porta
        s.listen()  # O servidor permanecerá ouvindo
        print("O servidor está ouvindo - porta:", porta)

        while True:
            conexaoCliente, endereco = s.accept()  # Criação de objeto de comunicação com cliente

            with conexaoCliente:  # Statement usado para fechar bloco na finalização
                print("Conectado pelo cliente - IP: ", endereco)

                mensagem = conexaoCliente.recv(1024)
                if not mensagem:  # Verifica se existe algum valor em bytes dentro de mensagem
                    break  # Finaliza o bloco

                argumentos = json.loads(mensagem.decode())  # Decodificação e desserialização

                # Autenticação
                if 'username' in argumentos and 'password' in argumentos:
                    resposta = autenticar(argumentos['username'], argumentos['password'])
                else:
                    resposta = "Erro: Credenciais de autenticação não fornecidas"

                if resposta == "Autenticado":
                    # Processar operações apenas se autenticado
                    if argumentos['op'] == "adicionar":
                        resposta = addTarefa(argumentos['tarefa'])
                    elif argumentos['op'] == 'remover':
                        resposta = removeTarefa(argumentos['id'])
                    elif argumentos['op'] == 'listar':
                        resposta = listTarefa()
                    else:
                        resposta = "Operação inválida"

                reply = json.dumps(resposta)  # Processo de serialização
                conexaoCliente.sendall(reply.encode())  # Envio do retorno e a codificação

servidorStub(65000)
