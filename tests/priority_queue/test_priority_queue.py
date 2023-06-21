from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    file1 = {"nome_do_arquivo": "arquivo1.txt", "qtd_linhas": 10}
    file2 = {"nome_do_arquivo": "arquivo2.txt", "qtd_linhas": 3}
    file3 = {"nome_do_arquivo": "arquivo3.txt", "qtd_linhas": 7}

    queue.enqueue(file1)
    queue.enqueue(file2)
    queue.enqueue(file3)

    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 2

    assert queue.dequeue() == file2
    assert queue.dequeue() == file1
    assert queue.dequeue() == file3
    assert len(queue) == 0

    queue.enqueue(file1)
    queue.enqueue(file2)
    queue.enqueue(file3)

    assert queue.search(0) == file2
    assert queue.search(2) == file3
    assert queue.search(1) == file1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(-19)
