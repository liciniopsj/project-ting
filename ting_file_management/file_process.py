import sys
from ting_file_management.file_management import txt_importer


def process(file_path, instance):
    for entry in instance.queue:
        if entry['nome_do_arquivo'] == file_path:
            return

    lines = txt_importer(file_path)
    new_entry = {
        "nome_do_arquivo": file_path,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(new_entry)

    processed_entry = instance.queue[-1]
    print(processed_entry)


def remove(instance):
    if not len(instance):
        print("Não há elementos")
        return

    path_file = instance.search(0)["nome_do_arquivo"]
    instance.dequeue()
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        sys.stderr.write("Posição inválida\n")
