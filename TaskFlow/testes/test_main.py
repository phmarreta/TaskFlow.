from src.main import tarefas, adicionar_tarefa, editar_tarefa, excluir_tarefa


def setup_function():
    tarefas.clear()


def test_adicionar_tarefa(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Estudar Python")

    adicionar_tarefa()

    assert len(tarefas) == 1
    assert tarefas[0] == "Estudar Python"


def test_editar_tarefa(monkeypatch):
    tarefas.append("Tarefa antiga")

    respostas = iter(["1", "Tarefa nova"])
    monkeypatch.setattr("builtins.input", lambda _: next(respostas))

    editar_tarefa()

    assert tarefas[0] == "Tarefa nova"


def test_excluir_tarefa(monkeypatch):
    tarefas.append("Tarefa para excluir")

    monkeypatch.setattr("builtins.input", lambda _: "1")

    excluir_tarefa()

    assert len(tarefas) == 0