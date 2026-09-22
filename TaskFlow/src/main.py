tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n===== Lista de Tarefas =====")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")
    print()


def editar_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1

        if 0 <= indice < len(tarefas):
            nova_tarefa = input("Digite a nova descrição: ")
            tarefas[indice] = nova_tarefa
            print("Tarefa atualizada com sucesso!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Digite apenas números.\n")


def excluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1

        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Digite apenas números.\n")


def executar_sistema():
    while True:
        print("===== TaskFlow =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            editar_tarefa()

        elif opcao == "4":
            excluir_tarefa()

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    executar_sistema()