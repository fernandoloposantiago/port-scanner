# 🌐 Port Scanner v1.0

<div align="center">

## 🛡️ Scanner de Portas TCP desenvolvido em Python

Projeto criado para estudos de **Python**, **Redes de Computadores** e **Segurança da Informação**.

**Desenvolvido por Fernando José Lôpo Santiago**

</div>

---

## 📖 Descrição

O **Port Scanner v1.0** é uma ferramenta educacional desenvolvida em Python para verificar uma lista predefinida de portas TCP em um endereço IP ou domínio informado pelo usuário.

O programa tenta estabelecer uma conexão com cada porta, identifica o serviço normalmente associado ao número da porta e apresenta um resumo final da verificação.

Este projeto faz parte da minha evolução prática nos estudos de **Análise e Desenvolvimento de Sistemas** e **Defesa Cibernética**.

---

## ✨ Funcionalidades

- Verificação de múltiplas portas TCP
- Entrada de endereço IP ou domínio
- Identificação do serviço normalmente associado à porta
- Classificação de portas abertas e fechadas
- Timeout para limitar o tempo de cada tentativa
- Tratamento de erros com `try` e `except`
- Contagem de portas verificadas
- Contagem de portas abertas
- Contagem de portas fechadas
- Medição do tempo total de execução
- Resumo final do scan

---

## 🔎 Portas verificadas

| Porta | Serviço associado |
|---|---|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3306 | MySQL |
| 8080 | HTTP Alternativo |

> O número da porta indica apenas o serviço normalmente associado. O scanner não confirma qual aplicação está realmente sendo executada naquela porta.

---

## 🖥️ Exemplo de execução

```text
============================================================
 PORT SCANNER v1.0
 Desenvolvido por Fernando José Lôpo Santiago
============================================================

Digite o IP ou domínio: 127.0.0.1

❌ Porta 21 fechada - FTP
❌ Porta 22 fechada - SSH
❌ Porta 23 fechada - Telnet
❌ Porta 25 fechada - SMTP
❌ Porta 53 fechada - DNS
❌ Porta 80 fechada - HTTP
❌ Porta 110 fechada - POP3
❌ Porta 143 fechada - IMAP
❌ Porta 443 fechada - HTTPS
❌ Porta 3306 fechada - MySQL
❌ Porta 8080 fechada - HTTP Alternativo

============================================================
Resultado do SCAN
============================================================
Portas verificadas: 11
Portas abertas: 0
Portas fechadas: 11
Tempo total de execução: 11.08 segundos
```

---

## 📂 Estrutura do projeto

```text
port-scanner/
├── .gitignore
├── main.py
└── README.md
```

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca `socket`
- Biblioteca `time`
- Git
- GitHub

---

## 📚 Conceitos aprendidos

Durante o desenvolvimento deste projeto, pratiquei:

- Endereços IPv4
- Portas de rede
- Comunicação TCP
- Sockets
- `AF_INET`
- `SOCK_STREAM`
- `settimeout()`
- `connect_ex()`
- Listas
- Laço `for`
- Dicionários
- Método `.get()`
- Funções
- `return True` e `return False`
- Contadores com `+= 1`
- Tratamento de erros com `try` e `except`
- Bloco `if __name__ == "__main__"`
- Medição de tempo com `time.time()`

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/fernandoloposantiago/port-scanner.git
```

### 2. Entre na pasta

```bash
cd port-scanner
```

### 3. Execute o programa

```bash
python main.py
```

---

## ⚠️ Uso responsável

Este projeto foi desenvolvido para fins educacionais.

Utilize a ferramenta apenas em:

- seu próprio computador;
- sistemas que você administra;
- laboratórios de estudo;
- ambientes em que você tenha autorização explícita para realizar testes.

Não utilize a ferramenta para verificar sistemas de terceiros sem autorização.

---

## 👨‍💻 Autor

**Fernando José Lôpo Santiago**

🎓 Estudante de Análise e Desenvolvimento de Sistemas

🛡️ Estudante de Defesa Cibernética

🐍 Desenvolvendo projetos práticos com Python e Segurança da Informação

---

## 🎯 Próximas melhorias

- Permitir que o usuário escolha as portas
- Validar melhor a entrada do usuário
- Diferenciar conexão recusada de tempo limite
- Registrar resultados em arquivo
- Adicionar data e horário da análise
- Criar testes automatizados
- Melhorar o desempenho da verificação

---

## ⭐ Objetivo do projeto

Fortalecer meus conhecimentos em:

- Python
- Redes de computadores
- Segurança da Informação
- Lógica de programação
- Git e GitHub
- Organização e documentação de projetos

---

## Obrigado por visitar o projeto!

Feedbacks técnicos e sugestões de melhoria são bem-vindos.# port-scanner
