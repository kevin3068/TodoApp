from app.services.todo_service import TodoService


def test_service_criar_tarefa(service):
    """
    Testa a criação de uma nova tarefa através do TodoService.
    """
    task = service.create("Estudar Docker", "Revisar Dockerfile")

    assert task.id == 1
    assert task.title == "Estudar Docker"
    assert task.description == "Revisar Dockerfile"
    assert task.completed is False
    assert service.get_by_id(task.id) == task


def test_service_listar_todas_as_tarefas(service):
    """
    Testa se o serviço lista corretamente todas as tarefas cadastradas.
    """
    task1 = service.create("Estudar Docker", "Revisar Dockerfile")
    task2 = service.create("Estudar pytest", "Escrever testes")

    tasks = service.list_all()

    assert tasks == [task1, task2]
    assert len(tasks) == 2


def test_service_buscar_tarefa_por_id_existente(service):
    """
    Testa a busca de uma tarefa por ID quando ela existe no repositório.
    """
    task = service.create("Estudar Docker")

    result = service.get_by_id(task.id)

    assert result is not None
    assert result.id == task.id
    assert result.title == "Estudar Docker"


def test_service_buscar_tarefa_por_id_inexistente(service):
    """
    Testa a busca de uma tarefa por ID inexistente, esperando retorno None.
    """
    result = service.get_by_id(999)

    assert result is None


def test_service_atualizar_tarefa_existente(service):
    """
    Testa a atualização de título, descrição e status de conclusão de uma tarefa.
    """
    task = service.create("Título antigo", "Descrição antiga")

    updated_task = service.update(
        task.id,
        title="Título novo",
        description="Descrição nova",
        completed=True,
    )

    assert updated_task is not None
    assert updated_task.id == task.id
    assert updated_task.title == "Título novo"
    assert updated_task.description == "Descrição nova"
    assert updated_task.completed is True


def test_service_remover_tarefa_existente(service):
    """
    Testa a remoção de uma tarefa existente e verifica se ela deixa de existir.
    """
    task = service.create("Estudar Docker")

    result = service.delete(task.id)

    assert result is True
    assert service.get_by_id(task.id) is None


def test_service_remover_tarefa_inexistente(service):
    """
    Testa a tentativa de remoção de ID inexistente, esperando retorno False.
    """
    result = service.delete(999)

    assert result is False
