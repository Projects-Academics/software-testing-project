# language: pt

Funcionalidade: Automação Avançada da API TMDB
  Como o QA Estudante Erick Vitor
  Quero validar o ciclo completo de vida dos dados (Criar, Ler, Deletar)
  Para garantir que a API processa avaliações e sessões corretamente.
  
  Nota Técnica: Como a API escolhida possui restrições de acesso para a função PUT (Atualizar) 
  com o Token atual, validarei os fluxos de GET, POST e DELETE.

  Contexto:
    Dado que possuo um Token de acesso válido

  Cenário: Fluxo de Avaliação de Séries de TV (Código 1)
    Quando eu consulto os detalhes da série "Game of Thrones" (ID 1399)
    Então o código de status deve ser 200
    E eu envio uma avaliação de nota 9.0 para esta série
    Então o código de status deve ser 201 (Criado)
    E eu deleto a avaliação da série
    Então o código de status deve ser 200 (Sucesso)

  Cenário: Fluxo de Avaliação de Filme Específico (Código 2)
    Quando eu consulto os detalhes do filme "Clube da Luta" (ID 550)
    Então o código de status deve ser 200
    E eu envio uma avaliação de nota 8.5 para este filme
    Então o código de status deve ser 201
    E eu deleto a avaliação enviada
    Então o código de status deve ser 200

  Cenário: Fluxo de Filmes em Cartaz "Now Playing" (Código 3)
    Quando eu consulto a lista de filmes em cartaz
    Então o código de status deve ser 200
    E eu busco os detalhes do filme específico (ID 534649)
    Então o código de status deve ser 200
    E eu envio uma avaliação de nota 8.0 para este filme
    Então o código de status deve ser 201
    E eu deleto a avaliação enviada
    Então o código de status deve ser 200

  Cenário: Fluxo de Filmes Populares (Código 4)
    Quando eu consulto a lista de filmes populares
    Então o código de status deve ser 200
    E eu busco os detalhes do filme específico (ID 634649)
    Então o código de status deve ser 200
    E eu envio uma avaliação de nota 7.5 para este filme
    Então o código de status deve ser 201
    E eu deleto a avaliação enviada
    Então o código de status deve ser 200

  Cenário: Fluxo de Sessão de Convidado (Código 5)
    Quando eu crio uma nova Sessão de Convidado
    Então o código de status deve ser 200
    E o ID da sessão (guest_session_id) não deve ser nulo
    
  Cenário: Avaliação via Sessão de Convidado (Código 5 - Parte 2)
    Dado que gero uma Sessão de Convidado ativa
    Quando eu avalio um filme (ID 550) com nota 8.0 usando o ID da sessão na URL
    Então o código de status deve ser 201
    E eu deleto a avaliação usando o ID da sessão na URL
    Então o código de status deve ser 200