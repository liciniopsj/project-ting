def exists_word(word, instance):
    found = []

    for item in range(len(instance)):
        occurrences = []

        for line_index, line_content in enumerate(instance.search(item)['linhas_do_arquivo']):
            if word.casefold() in line_content.casefold():
                occurrences.append({'linha': line_index + 1})

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

        for line_index, line_content in enumerate(instance.search(item)['linhas_do_arquivo']):
            if word.casefold() in line_content.casefold():
                occurrences.append({'linha': line_index + 1, 'conteudo': line_content})

        if occurrences:
            results.append({
                'palavra': word,
                'arquivo': instance.search(item)['nome_do_arquivo'],
                'ocorrencias': occurrences,
            })

    return results

