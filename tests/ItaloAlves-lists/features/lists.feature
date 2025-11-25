# language: pt
Funcionalidade: Lists API - Italo Alves

  Contexto:
    Dado que a url base da API é "https://api.themoviedb.org/3"
    E que o endpoint para listar listas é "/list"

  # 1. Listar detalhes de uma lista – GET /list/{list_id}
  Cenário: Listar detalhes de uma lista existente
    Dado que existe uma lista com id "8283481"
    Quando eu enviar uma requisição `GET` para "/list/8283481"
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "id", "name", "description", "favorite_count", "item_count", "iso_639_1", "list_type" e "items"
    E o campo "items" deve ser um array
    E cada item do array deve ter os campos "adult", "backdrop_path", "id", "title", "original_language", "original_title", "overview", "poster_path", "media_type", "genre_ids", "popularity", "release_date", "video", "vote_average" e "vote_count"

  # 2. Verificar status de um item na lista – GET /list/{list_id}/item_status
  Cenário: Verificar se um filme está presente na lista
    Dado que existe uma lista com id "8283481"
    E que existe um filme com id "550"
    Quando eu enviar uma requisição `GET` para "/list/8283481/item_status" com os seguintes parâmetros:
      | parâmetro  | valor |
      | movie_id   | 550   |
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "id", "item_present"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo        | valor    |
      | id           | 550      |
      | item_present | boolean  |

  # 3. Criar uma nova lista – POST /list
  Cenário: Criar uma nova lista com sucesso
    Quando eu enviar uma requisição `POST` para "/list" com o seguinte corpo:
      """json
      {
        "name": "Minha Lista de Filmes",
        "description": "Lista com os melhores filmes de ação",
        "language": "pt-BR"
      }
      """
    Então o código de status da resposta deve ser 201
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code", "status_message" e "list_id"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | true  |
      | status_code    | 1     |

  # 4. Adicionar um filme à lista – POST /list/{list_id}/add_item
  Cenário: Adicionar um filme a uma lista existente
    Dado que existe uma lista com id "8283481"
    Quando eu enviar uma requisição `POST` para "/list/8283481/add_item" com o seguinte corpo:
      """json
      {
        "media_id": 550
      }
      """
    Então o código de status da resposta deve ser 201
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | true  |
      | status_code    | 12    |

  # 5. Remover um filme da lista – POST /list/{list_id}/remove_item
  Cenário: Remover um filme de uma lista existente
    Dado que existe uma lista com id "8283481"
    E que existe um filme com id "550" na lista
    Quando eu enviar uma requisição `POST` para "/list/8283481/remove_item" com o seguinte corpo:
      """json
      {
        "media_id": 550
      }
      """
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | true  |
      | status_code    | 13    |

  # 6. Limpar todos os itens da lista – POST /list/{list_id}/clear
  Cenário: Limpar todos os filmes de uma lista existente
    Dado que existe uma lista com id "8283481"
    Quando eu enviar uma requisição `POST` para "/list/8283481/clear" com o seguinte corpo:
      """json
      {
        "confirm": true
      }
      """
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | true  |
      | status_code    | 12    |

  # 7. Deletar uma lista – DELETE /list/{list_id}
  Cenário: Deletar uma lista existente
    Dado que existe uma lista com id "8283481"
    Quando eu enviar uma requisição `DELETE` para "/list/8283481"
    Então o código de status da resposta deve ser 200
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | true  |
      | status_code    | 13    |

  # 8. Cenário de erro - Lista não encontrada
  Cenário: Tentar obter detalhes de uma lista inexistente
    Quando eu enviar uma requisição `GET` para "/list/999999999"
    Então o código de status da resposta deve ser 404
    E a resposta deve ser um objeto `JSON`
    E o objeto deve ter os campos "success", "status_code" e "status_message"
    E a resposta deve ser um objeto com os seguintes valores:
      | campo          | valor |
      | success        | false |
      | status_code    | 34    |
