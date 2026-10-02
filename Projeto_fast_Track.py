import datetime
import random

# --- UNIDADE 3: Estruturas de Dados ---
# Lista que funcionará como uma Fila (FIFO - First In, First Out)
fila_atendimento = []

def adicionar_chamado():
    print("\n--- Novo Chamado ---")
    try:
        # UNIDADE 1: Entrada e conversão de tipos
        nome = input("Nome do cliente: ").strip()
        prioridade = int(input("Prioridade (1 - Normal, 2 - Urgente): "))

        # UNIDADE 2: Condicional complexa
        if prioridade == 2:
            nivel = "Urgente"
        elif prioridade == 1:
            nivel = "Normal"
        else:
            print("Opção inválida. Definindo como Normal.")
            nivel = "Normal"

        # UNIDADE 3: Dicionário para organizar informações
        chamado = {
            "id": random.randint(1000, 9999), # UNIDADE 1: Biblioteca random
            "cliente": nome,
            "status": nivel,
            "hora": datetime.datetime.now().strftime("%H:%M:%S") # UNIDADE 1: Datetime
        }

        fila_atendimento.append(chamado)
        print(f"✅ Chamado #{chamado['id']} registrado com sucesso!")

    except ValueError:
        # UNIDADE 4: Tratamento de erro
        print("❌ Erro: Por favor, insira valores numéricos para a prioridade.")

def processar_atendimento():
    if not fila_atendimento:
        print("\n📭 Ninguém na fila para atender.")
    else:
        # Lógica de Fila: O primeiro a entrar é o primeiro a sair (pop(0))
        atendido = fila_atendimento.pop(0)
        print(f"\n🔔 Atendendo agora: {atendido['cliente']} (Chamado {atendido['id']})")
        print(f"Horário de registro: {atendido['hora']}")

def exibir_relatorio():
    """
    Exibe todos os chamados usando laços de repetição.
    """
    print("\n--- Lista de Espera Atual ---")
    if not fila_atendimento:
        print("Fila vazia.")
    else:
        # UNIDADE 2: Laço de repetição
        for idx, item in enumerate(fila_atendimento, 1):
            print(f"{idx}. [{item['status']}] {item['cliente']} - ID: {item['id']}")

# --- UNIDADE 2: Menu Principal ---
def menu():
    while True:
        print("\n============================")
        print("    SISTEMA FASTTRACK")
        print("============================")
        print("1. Novo Chamado")
        print("2. Atender Próximo")
        print("3. Listar Fila")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_chamado()
        elif opcao == '2':
            processar_atendimento()
        elif opcao == '3':
            exibir_relatorio()
        elif opcao == '4':
            print("Encerrando sistema... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
