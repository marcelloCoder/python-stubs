# PYTHON STUBS CLIENTE E SERVIDOR

# Implementação de Autenticação nos Stubs Cliente-Servidor em Python

## Descrição

Este projeto implementa um sistema de autenticação básico em um ambiente cliente-servidor utilizando Python. Ele demonstra a utilização de **stubs** para comunicação entre o cliente e o servidor, incluindo funcionalidades como:

- Autenticação de usuário com bloqueio após múltiplas tentativas falhas.
- Registro de autenticações realizadas.
- Operações básicas de gerenciamento de tarefas (adicionar, remover, listar).

## Estrutura do Projeto

O projeto consiste em dois arquivos principais:

1. **server.py**: Código do servidor que lida com autenticações e operações de tarefas.
2. **client.py**: Código do cliente que se conecta ao servidor, realiza a autenticação e envia operações.

## Preparar o Ambiente

Para executar este projeto, siga os passos abaixo:

### 1. Criar os Arquivos

- **Servidor (`server.py`)**: Crie um arquivo chamado `server.py` e insira o código do servidor nele.
- **Cliente (`client.py`)**: Crie um arquivo chamado `client.py` e insira o código do cliente nele.

### 2. Executar o Servidor

1. **Abrir o Terminal:**
   - No seu sistema, abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `server.py` está localizado usando o comando `cd`.
  
2. **Iniciar o Servidor:**
   - Execute o servidor com o comando:
     ```bash
     python server.py
     ```
   - O servidor começará a ouvir na porta `65000` e estará pronto para receber conexões do cliente.

### 3. Executar o Cliente

1. **Abrir Outro Terminal:**
   - Abra um novo terminal ou prompt de comando.
   - Navegue até o diretório onde o arquivo `client.py` está localizado.

2. **Iniciar o Cliente:**
   - Execute o cliente com o comando:
     ```bash
     python client.py
     ```
   - O cliente tentará se conectar ao servidor, passar as credenciais e realizar a operação especificada (como adicionar uma tarefa).

## Implementação

### 1. Autenticação Básica

- A função `autenticar` no servidor verifica se as credenciais enviadas pelo cliente são válidas. 
- Se o nome de usuário e a senha estiverem corretos, a autenticação é bem-sucedida. Caso contrário, o número de tentativas falhas é incrementado.

### 2. Bloqueio Após Múltiplas Tentativas

- Após três tentativas de autenticação falhas, o sistema bloqueia o usuário, impedindo novas tentativas até que o servidor seja reiniciado.

### 3. Registro de Autenticações

- Cada autenticação bem-sucedida é registrada em um log, que pode ser consultado para fins de auditoria.

## Testes

### 1. Teste de Autenticação Bem-Sucedida

- Execute o cliente com as credenciais corretas (`username: admin`, `password: 1234`).
- Verifique no terminal do servidor que a autenticação foi bem-sucedida e a operação foi realizada.

### 2. Teste de Autenticação Falha

- Modifique o `client.py` para usar credenciais incorretas.
- Execute o cliente e observe que o servidor rejeitará a autenticação.
- Após três tentativas falhas, o usuário será bloqueado.

### 3. Teste de Operações de Tarefas

- Altere as operações no `client.py` para adicionar, remover ou listar tarefas.
- Observe no terminal do servidor como cada operação é processada após a autenticação bem-sucedida.

## Conclusão

Este projeto demonstra a implementação de autenticação básica em um ambiente cliente-servidor usando Python, além de funcionalidades adicionais como bloqueio após tentativas falhas e registro de autenticações. É um exemplo simples e funcional de como proteger operações críticas em uma aplicação distribuída.