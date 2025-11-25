# language: pt
Funcionalidade: Lists API - Italo Alves

  Contexto:
    Dado que a url base da API é "https://api.themoviedb.org/3"
    E que o endpoint para listar listas é "/list"

  # 1. Listar detalhes de uma lista – GET /list/{list_id}
  Cenário: Listar detalhes de uma lista existente
    Dado que existe uma lista com id "8283481"
    Quando eu enviar uma requisição `GET` para "/list/8283481"
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`

  # 2. Verificar status de um item na lista – GET /list/{list_id}/item_status
  Cenário: Verificar se um filme está presente na lista
    Dado que existe uma lista com id "8283481"
    E que existe um filme com id "550"
    Quando eu enviar uma requisição `GET` para "/list/8283481/item_status" com os seguintes parâmetros:
      | parâmetro  | valor |
      | movie_id   | 550   |
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`

  # 3. Listar filmes populares – GET /movie/popular
  Cenário: Listar filmes populares
    Quando eu enviar uma requisição `GET` para "/movie/popular"
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`

  # 4. Detalhes de um filme – GET /movie/{movie_id}
  Cenário: Obter detalhes de um filme existente
    Dado que existe um filme com id "550"
    Quando eu enviar uma requisição `GET` para "/movie/550"
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`

  # 5. Buscar filmes por texto – GET /search/movie
  Cenário: Buscar filmes pelo título
    Quando eu enviar uma requisição `GET` para "/search/movie" com os seguintes parâmetros:
      | parâmetro | valor        |
      | query     | Fight Club   |
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "page", "results", "total_pages" e "total_results"
    E o campo "results" deve ser um array
    E cada item do array deve ter os campos "id", "title", "overview", "poster_path" e "release_date"

  # 8. Cenário de erro - Lista não encontrada
  Cenário: Tentar obter detalhes de uma lista inexistente
    Quando eu enviar uma requisição `GET` para "/list/999999999"
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | false |
      | status_code    | 6     |
