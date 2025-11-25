import requests
import os
import pytest
from dotenv import load_dotenv
from pytest_bdd import scenarios, given, when, then, parsers

# Carrega variáveis do arquivo .env na raiz do projeto
load_dotenv()


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


@given(parsers.cfparse('que existe um filme com id "{movie_id}" na lista'), target_fixture="movie_id")
def existing_movie_in_list(movie_id: str) -> str:
    return movie_id


# Cenários
# ========
def _resolve_list_id(list_id: str) -> str:
    """Allow overriding list_id via env var TMDB_LIST_ID without changing feature."""
    return os.getenv("TMDB_LIST_ID", list_id)


def _build_auth():
    """Build headers/params using either v4 bearer or v3 api_key."""
    headers = {}
    params = {}
    bearer = os.getenv("TMDB_BEARER_TOKEN")
    api_key = os.getenv("TMDB_API_KEY")
    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
    if api_key:
        params["api_key"] = api_key
    return headers, params


# 1. Listar detalhes de uma lista – GET /list/{list_id}

@when(parsers.cfparse('eu enviar uma requisição `GET` para "{path}/{list_id}"'), target_fixture="response")
def send_get_list_details_request(base_url: str, path: str, list_id: str):
    list_id = _resolve_list_id(list_id)
    url = base_url + path + "/" + list_id
    headers, params = _build_auth()
    if not headers and not params:
        pytest.skip("Defina TMDB_BEARER_TOKEN ou TMDB_API_KEY no .env para executar GET.")
    resp = requests.get(url, headers=headers, params=params)
    return resp


@when(parsers.cfparse('eu enviar uma requisição `GET` para "{path}"'), target_fixture="response")
def send_get_simple_request(base_url: str, path: str):
    url = base_url + path
    headers, params = _build_auth()
    if not headers and not params:
        pytest.skip("Defina TMDB_BEARER_TOKEN ou TMDB_API_KEY no .env para executar GET.")
    resp = requests.get(url, headers=headers, params=params)
    return resp


# 2. Verificar status de um item na lista – GET /list/{list_id}/item_status

@when(parsers.cfparse('eu enviar uma requisição `GET` para "{path}/{list_id}/item_status" com os seguintes parâmetros:'), target_fixture="response")
def send_get_item_status_request(base_url: str, path: str, list_id: str, datatable):
    # datatable contém a tabela de parâmetros (parâmetro, valor)
    params = _datatable_to_dict(datatable)
    query_params = {row["parâmetro"]: row["valor"] for row in params}
    list_id = _resolve_list_id(list_id)
    headers, base_params = _build_auth()
    if not headers and not base_params:
        pytest.skip("Defina TMDB_BEARER_TOKEN ou TMDB_API_KEY no .env para executar GET.")
    url = base_url + path + "/" + list_id + "/item_status"
    query_params.update(base_params)
    resp = requests.get(url, headers=headers, params=query_params)
    return resp


# 5. Buscar filmes por texto – GET /search/movie com parâmetros na query

@when(parsers.cfparse('eu enviar uma requisição `GET` para "{path}" com os seguintes parâmetros:'), target_fixture="response")
def send_get_with_query_params(base_url: str, path: str, datatable):
    # datatable contém a tabela de parâmetros (parâmetro, valor)
    rows = _datatable_to_dict(datatable)
    query_params = {row["parâmetro"]: row["valor"] for row in rows}
    headers, base_params = _build_auth()
    if not headers and not base_params:
        pytest.skip("Defina TMDB_BEARER_TOKEN ou TMDB_API_KEY no .env para executar GET.")
    url = base_url + path
    query_params.update(base_params)
    resp = requests.get(url, headers=headers, params=query_params)
    return resp


"""Não há mais cenários de escrita (POST/DELETE); apenas GETs são usados."""


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


@then(parsers.cfparse('o campo "{field}" deve ser um array'))
def check_field_is_array(response, field: str):
    data = _extract_object_from_response(response)
    assert isinstance(data.get(field), list)


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
        # validação leve de tipos
        if 'genre_ids' in item:
            assert isinstance(item['genre_ids'], list)
            assert all(isinstance(g, int) for g in item['genre_ids'])
