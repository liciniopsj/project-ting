def instance_search(instance, item):
    return instance.search(item)['linhas_do_arquivo']


def exists_word(word, instance):
    found = []

    for item in range(len(instance)):
        occurrences = []

        for index, content in enumerate(instance_search(instance, item)):
            if word.casefold() in content.casefold():
                occurrences.append({'linha': index + 1})

        if occurrences:
            found.append({
                'palavra': word,
                'arquivo': instance.search(item)['nome_do_arquivo'],
                'ocorrencias': occurrences,
            })

    return found


def search_by_word(word, instance):
    results = []

    for item in range(len(instance)):
        occurrences = []

        for index, content in enumerate(instance_search(instance, item)):
            if word.casefold() in content.casefold():
                occurrences.append({'linha': index + 1, 'conteudo': content})

        if occurrences:
            results.append({
                'palavra': word,
                'arquivo': instance.search(item)['nome_do_arquivo'],
                'ocorrencias': occurrences,
            })

    return results
