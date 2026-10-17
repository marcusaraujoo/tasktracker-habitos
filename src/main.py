import sys

def validar_titulo():
    """Solicita e valida o título/nome do hábito, impedindo entradas vazias."""
    while True:
        titulo = input("Digite o nome do hábito: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O nome do hábito é obrigatório e não pode conter apenas espaços em branco!\n")

def validar_prioridade():
    """Solicita e valida a prioridade (Alta, Média ou Baixa)."""
    opcoes_validas = {
        "1": "Alta",
        "2": "Média",
        "3": "Baixa",
        "alta": "Alta",
        "média": "Média",
        "media": "Média",
        "baixa": "Baixa"
    }
    
    while True:
        print("Selecione a Prioridade:")
        print("  1. Alta")
        print("  2. Média")
        print("  3. Baixa")
        entrada = input("Escolha uma opção (1-3) ou digite o nome: ").strip().lower()
        
        if entrada in opcoes_validas:
            return opcoes_validas[entrada]
        print("[ERRO] Prioridade inválida! Escolha entre Alta, Média ou Baixa.\n")

def cadastrar_habito(lista_habitos):
    """Cadastra um novo hábito/tarefa aplicando as regras de validação."""
    print("\n--- CADASTRO DE NOVO HÁBITO ---")
    
    titulo = validar_titulo()
    
    for habito in lista_habitos:
        if habito["titulo"].lower() == titulo.lower():
            print(f"[AVISO] Já existe um hábito cadastrado com o nome '{titulo}' para hoje!\n")
            return

    descricao = input("Digite a descrição/detalhes (opcional): ").strip()
    if not descricao:
        descricao = "Sem descrição"
        
    prioridade = validar_prioridade()
    data_limite = input("Digite a meta de horário/frequência (ex: Manhã, 20:00 ou DD/MM/AAAA): ").strip()
    if not data_limite:
        data_limite = "Diário"

    novo_habito = {
        "id": len(lista_habitos) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    lista_habitos.append(novo_habito)
    print(f"\n[SUCESSO] Hábito '{titulo}' cadastrado com sucesso!")

def visualizar_habitos(lista_habitos):
    """Exibe todos os hábitos cadastrados ou mensagem caso esteja vazia."""
    print("\n--- ACOMPANHAMENTO DE HÁBITOS DIÁRIOS ---")
    if not lista_habitos:
        print("Nenhum hábito cadastrado no momento.")
        return

    concluidos = sum(1 for h in lista_habitos if h["status"] == "Concluído")
    print(f"Progresso do dia: {concluidos} de {len(lista_habitos)} hábito(s) concluído(s).\n")
    
    for habito in lista_habitos:
        print(f"[{habito['id']}] {habito['titulo']} - Status: {habito['status']}")
        print(f"    Descrição : {habito['descricao']}")
        print(f"    Prioridade: {habito['prioridade']}")
        print(f"    Meta/Prazo: {habito['data_limite']}")
        print("-" * 45)

def marcar_como_concluido(lista_habitos):
    """Permite alterar o status de um hábito para Concluído."""
    visualizar_habitos(lista_habitos)
    if not lista_habitos:
        return

    try:
        id_habito = int(input("\nDigite o ID do hábito que deseja marcar como Concluído (ou 0 para cancelar): "))
        if id_habito == 0:
            return
        
        for habito in lista_habitos:
            if habito["id"] == id_habito:
                habito["status"] = "Concluído"
                print(f"\n[PARABÉNS] Hábito '{habito['titulo']}' marcado como Concluído!")
                return
        
        print("[ERRO] Hábito com ID informado não foi encontrado.")
    except ValueError:
        print("[ERRO] Entrada inválida! Digite apenas números inteiros.")

def menu_principal():
    """Menu contínuo de navegação da aplicação CLI."""
    lista_habitos = []
    
    while True:
        print("\n==========================================")
        print("   TASKTRACKER - RASTREADOR DE HÁBITOS   ")
        print("==========================================")
        print("1. Cadastrar novo hábito")
        print("2. Visualizar hábitos cadastrados")
        print("3. Marcar hábito como concluído")
        print("4. Sair da aplicação")
        print("==========================================")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            cadastrar_habito(lista_habitos)
        elif opcao == "2":
            visualizar_habitos(lista_habitos)
        elif opcao == "3":
            marcar_como_concluido(lista_habitos)
        elif opcao == "4":
            print("\nEncerrando o TaskTracker de Hábitos... Até mais!")
            sys.exit(0)
        else:
            print("\n[ERRO] Opção inválida! Escolha um número entre 1 e 4.")

if __name__ == "__main__":
    menu_principal()
