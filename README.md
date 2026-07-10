# 🌐 Port Scanner v1.1

<div align="center">

## 🛡️ Scanner de Portas TCP desenvolvido em Python

Projeto criado para estudos de **Python**, **Redes de Computadores** e **Segurança da Informação**.

**Desenvolvido por Fernando José Lôpo Santiago**

</div>

---

## 📖 Descrição

O **Port Scanner v1.1** é uma ferramenta educacional desenvolvida em Python que permite ao usuário escolher quais portas TCP deseja verificar em um endereço IP ou domínio.

O programa tenta estabelecer uma conexão com cada porta informada, identifica o serviço normalmente associado ao número da porta e apresenta um resumo final da verificação.

Este projeto faz parte da minha evolução prática nos estudos de **Análise e Desenvolvimento de Sistemas** e **Defesa Cibernética**.

---

## ✨ Funcionalidades

- Verificação de múltiplas portas TCP
- Entrada de endereço IP ou domínio
- Escolha personalizada das portas pelo usuário
- Separação das portas informadas com `.split()`
- Conversão das portas para números inteiros com `int()`
- Validação de entradas que não são números
- Validação de portas no intervalo de 1 a 65535
- Encerramento seguro quando nenhuma porta válida é informada
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

## 🆕 Novidades da versão v1.1

Na versão anterior, o programa utilizava uma lista fixa de portas.

Agora o usuário pode escolher quais portas deseja verificar.

### Exemplo

```text
Digite as portas separadas por vírgula: 22,80,443
```

O programa:

1. recebe as portas como texto;
2. separa os valores pelas vírgulas;
3. converte cada valor para número inteiro;
4. valida se a porta está entre 1 e 65535;
5. ignora entradas inválidas;
6. verifica somente as portas válidas.

---

## 🔎 Serviços identificados

O programa possui um dicionário com alguns serviços normalmente associados a portas conhecidas:

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

Se o usuário escolher uma porta que não está nessa tabela, o programa poderá identificá-la como:

```text
Desconhecido
```

> O número da porta indica apenas o serviço normalmente associado. O scanner não confirma qual aplicação está realmente sendo executada naquela porta.

---

## 🖥️ Exemplo de execução

```text
============================================================
 PORT SCANNER v1.1
Desenvolvido por Fernando José Lôpo Santiago
============================================================
Digite o IP ou domínio: 127.0.0.1
Digite as portas separadas por vírgula: 22,80,443

❌ Porta 22 fechada - SSH
❌ Porta 80 fechada - HTTP
❌ Porta 443 fechada - HTTPS

============================================================
Resultado do SCAN
============================================================
Portas verificadas: 3
Portas abertas: 0
Portas fechadas: 3
Tempo total de execução: 3.02 segundos
```

---

## 🧪 Validação de entradas

### Entrada com texto inválido

```text
Digite as portas separadas por vírgula: 22,abc,443

⚠️ abc não é uma porta válida.
```

O programa ignora o valor inválido e continua verificando as portas válidas.

### Porta fora do intervalo permitido

```text
Digite as portas separadas por vírgula: 22,70000,443

⚠️ 70000 não é uma porta válida.
```

São aceitas somente portas entre:

```text
1 e 65535
```

### Nenhuma porta válida

```text
Digite as portas separadas por vírgula: abc,70000

⚠️ abc não é uma porta válida.
⚠️ 70000 não é uma porta válida.

⚠️ Nenhuma porta válida foi fornecida. Encerrando o programa.
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
- Listas vazias
- Laço `for`
- Dicionários
- Método `.get()`
- Método `.split()`
- Método `.append()`
- Conversão com `int()`
- Funções
- `return True` e `return False`
- Condições com `if` e `else`
- Validação de intervalos
- Contadores com `+= 1`
- Tratamento de erros com `try` e `except`
- `ValueError`
- Bloco `if __name__ == "__main__"`
- Medição de tempo com `time.time()`

---

## 🔄 Fluxo de desenvolvimento utilizado

A versão v1.1 foi desenvolvida utilizando um fluxo organizado no GitHub:

```text
Issue
  ↓
Branch
  ↓
Desenvolvimento
  ↓
Testes
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Merge
```

Durante essa evolução:

- uma Issue foi criada para registrar a nova funcionalidade;
- uma branch separada foi criada para o desenvolvimento;
- o código foi testado antes do commit;
- as alterações foram revisadas com `git status` e `git diff`;
- um Pull Request foi aberto;
- a nova funcionalidade foi integrada à branch principal.

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

### 4. Informe o endereço

Exemplo:

```text
127.0.0.1
```

### 5. Informe as portas

Exemplo:

```text
22,80,443
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

- [x] Permitir que o usuário escolha as portas
- [x] Validar entradas que não são números
- [x] Validar portas fora do intervalo permitido
- [x] Encerrar o programa quando nenhuma porta válida for informada
- [ ] Diferenciar conexão recusada de tempo limite
- [ ] Registrar resultados em arquivo
- [ ] Adicionar data e horário da análise
- [ ] Criar testes automatizados
- [ ] Melhorar o desempenho da verificação
- [ ] Permitir a escolha de um intervalo de portas

---

## ⭐ Objetivo do projeto

Fortalecer meus conhecimentos em:

- Python
- Redes de Computadores
- Segurança da Informação
- Lógica de programação
- Git e GitHub
- Issue, Branch e Pull Request
- Organização e documentação de projetos

---

## 🙏 Obrigado por visitar o projeto!

Feedbacks técnicos e sugestões de melhoria são bem-vindos.