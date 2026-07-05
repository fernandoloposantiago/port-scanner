import socket
import time


# Dicionário de portas e serviços
servicos = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Alternativo"
}


def verificar_porta(ip, porta):
    try:
        conexao = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        conexao.settimeout(1)

        resultado = conexao.connect_ex((ip, porta))

        # Busca o serviço correspondente à porta
        servico = servicos.get(porta, "Desconhecido")

        if resultado == 0:
            print(f"✅ Porta {porta} aberta - {servico}")
            conexao.close()
            return True
        
        else:
            print(f"❌ Porta {porta} fechada - {servico}")
        conexao.close()
        return False

    except Exception as erro:
        print(f"Erro ao verificar a porta {porta}: {erro}")
        return FalseE


if __name__ == "__main__":
    print("=" * 60)
    print(" PORT SCANNER v1.0 ")
    print("Desenvolvido por Fernando José lôpo Santiago")
    print("=" * 60)

    ip = input("Digite o IP ou domínio: ")

    portas = [
        21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080 ]
    
    inicio = time.time()
     
    portas_abertas = 0
    portas_fechadas = 0 
    


    for porta in portas:
        status = verificar_porta(ip, porta)
        
        if status:
            portas_abertas += 1
        else:
            portas_fechadas += 1
            
    

    print("\n" + "=" * 60) 
    print("Resultado do SCAN")  
    print("=" * 60)
    print(f"Portas verificadas: {len(portas)}")  
    print(f"Portas abertas: {portas_abertas}")
    print(f"Portas fechadas: {portas_fechadas}")
    
    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo total de execução: {tempo_total:.2f} segundos")