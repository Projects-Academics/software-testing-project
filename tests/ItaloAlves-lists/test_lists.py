import requests
from pytest import scenarios, given, when, then, parsers


# Carrega os cenários do arquivo de feature
scenarios("features/lists.feature")


# Contexto
# ========

@given(parsers.cfparse('que a url base da API é "{base_url}"'), target_fixture="base_url")
def base_url(base_url: str) -> str:
    return base_url


@given(parsers.cfparse('que o endpoint para listar listas é "{path}"'), target_fixture="path")
def endpoint(path: str) -> str:
    return path


@given(parsers.cfparse('que existe uma lista com id "{list_id}"'), target_fixture="list_id")
def existing_list_id(list_id: str) -> str:
    return list_id


@given(parsers.cfparse('que existe um filme com id "{movie_id}"'), target_fixture="movie_id")
def existing_movie_id(movie_id: str) -> str:
    return movie_id


# Cenários
# ========

# 1. Listar detalhes de uma lista – GET /list/{list_id}

@when(parsers.cfparse('eu envio uma requisição `GET` para "{path}/{list_id}"'), target_fixture="response")
def send_get_list_details_request(base_url: str, path: str, list_id: str):
    url = base_url + path + "/" + list_id
    resp = requests.get(url)
    return resp


@when(parsers.cfparse('eu envio uma requisição `GET` para "{path}"'), target_fixture="response")
def send_get_simple_request(base_url: str, path: str):
    url = base_url + path
    resp = requests.get(url)
    return resp


# 2. Verificar status de um item na lista – GET /list/{list_id}/item_status

@when(parsers.cfparse('eu enviar uma requisição `GET` para "{path}/{list_id}/item_status" com os seguintes parâmetros:'), target_fixture="response")
def send_get_item_status_request(base_url: str, path: str, list_id: str, datatable):
    # datatable contém a tabela de parâmetros (parâmetro, valor)
    params = _datatable_to_dict(datatable)
    query_params = {row["parâmetro"]: row["valor"] for row in params}
    url = base_url + path + "/" + list_id + "/item_status"
    resp = requests.get(url, params=query_params)
    return resp


# 3. Criar uma nova lista – POST /list

@when(parsers.cfparse('eu envio uma requisição `POST` para "{path}" com o seguinte corpo:'), target_fixture="response")
def send_post_create_list_request(base_url: str, path: str):
    # Corpo fixo baseado no arquivo de feature
    body = {
        "name": "Minha Lista de Filmes",
        "description": "Lista com os melhores filmes de ação",
        "language": "pt-BR",
    }
    url = base_url + path
    resp = requests.post(url, json=body)
    return resp


# 4. Adicionar um filme a lista – POST /list/{list_id}/add_item

@when(parsers.cfparse('eu envio uma requisição `POST` para "{path}/{list_id}/add_item" com o seguinte corpo:'), target_fixture="response")
def send_post_add_item_request(base_url: str, path: str, list_id: str):
    body = {"media_id": 550}
    url = base_url + path + "/" + list_id + "/add_item"
    resp = requests.post(url, json=body)
    return resp


# 5. Remover um filme da lista – POST /list/{list_id}/remove_item

@when(parsers.cfparse('eu envio uma requisição `POST` para "{path}/{list_id}/remove_item" com o seguinte corpo:'), target_fixture="response")
def send_post_remove_item_request(base_url: str, path: str, list_id: str):
    body = {"media_id": 550}
    url = base_url + path + "/" + list_id + "/remove_item"
    resp = requests.post(url, json=body)
    return resp


# 6. Limpar todos os itens da lista – POST /list/{list_id}/clear

@when(parsers.cfparse('eu envio uma requisição `POST` para "{path}/{list_id}/clear" com o seguinte corpo:'), target_fixture="response")
def send_post_clear_list_request(base_url: str, path: str, list_id: str):
    body = {"confirm": True}
    url = base_url + path + "/" + list_id + "/clear"
    resp = requests.post(url, json=body)
    return resp


# 7. Deletar uma lista – DELETE /list/{list_id}

@when(parsers.cfparse('eu envio uma requisição `DELETE` para "{path}/{list_id}"'), target_fixture="response")
def send_delete_list_request(base_url: str, path: str, list_id: str):
    url = base_url + path + "/" + list_id
    resp = requests.delete(url)
    return resp


#===================
# Funções auxiliares


def _extract_list_from_response(response):
    data = response.json()
    if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
        return data["data"]
    return data


def _extract_object_from_response(response):
    data = response.json()
    if isinstance(data, dict) and "data" in data and isinstance(data["data"], dict):
        return data["data"]
    return data


def _datatable_to_dict(datatable):
    if not datatable:
        return []
    headers = datatable[0]
    result = []
    for row in datatable[1:]:
        row_dict = {}
        for i, header in enumerate(headers):
            if i < len(row):
                row_dict[header] = row[i]
        result.append(row_dict)
    return result


# Then steps (verificações)
# ==========================


@then(parsers.cfparse('o código de status da resposta deve ser {status_code:d}'))
def check_status_code(status_code: int, response):
    assert response.status_code == status_code


@then('a resposta deve ser um objeto `JSON`')
def check_json_object(response):
    data = _extract_object_from_response(response)
    assert isinstance(data, dict)


@then(parsers.cfparse('o objeto deve ter os campos "{fields}"'))
def check_object_fields(response, fields):
    fields_clean = fields.replace(' e ', ',')
    expected_fields = [f.strip().strip('"') for f in fields_clean.split(',') if f.strip()]
    data = _extract_object_from_response(response)
    for f in expected_fields:
        assert f in data


@then('a resposta deve ser um objeto com os seguintes valores:')
def check_object_values(response, datatable):
    data = _extract_object_from_response(response)
    rows = _datatable_to_dict(datatable)
    for row in rows:
        campo = row['campo']
        valor = row['valor']
        actual_value = data.get(campo)
        if isinstance(actual_value, bool):
            expected_bool = valor.lower() in ['true', '1', 'yes']
            assert actual_value == expected_bool, f"Campo {campo}: esperado {expected_bool}, obtido {actual_value}"
        elif isinstance(actual_value, int):
            expected_int = int(valor)
            assert actual_value == expected_int, f"Campo {campo}: esperado {expected_int}, obtido {actual_value}"
        else:
            expected_str = valor.strip('"')
            assert str(actual_value) == expected_str, f"Campo {campo}: esperado '{expected_str}', obtido '{actual_value}'"


@then('o campo "items" deve ser um array')
def check_items_is_array(response):
    data = _extract_object_from_response(response)
    assert isinstance(data.get('items'), list)


@then(parsers.cfparse('cada item do array deve ter os campos "{fields}"'))
def check_items_fields(response, fields):
    fields_clean = fields.replace(' e ', ',')
    expected_fields = [f.strip().strip('"') for f in fields_clean.split(',') if f.strip()]
    data = _extract_object_from_response(response)
    items = data.get('items', [])
    assert isinstance(items, list)
    for item in items:
        for f in expected_fields:
            assert f in item
