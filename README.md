# UsersAPI ✅

Este projeto é um sistema de autenticação de usuário completo. Nele você é possivel:

- Cadastrar, atualizar e deletar usuários. 
- Gerar tokens para autenticações.
- Validar se o usuário possui permissão para acessar determinada rota.

A parte de autenticação possui duas modalidades:

- Autenticação da rota simples usando aquenas um token.
- Autenticação com duplo fator, onde é gerado um token e também é necessário validar um código que é enviado para o aplicativo de autenticação ou email do usuário.

A aplicação foi criada utilizando _Python_ e a biblioteca _FastAPI_, o banco de dados com _Postgres_ e a ferramenta _Flyway_ para ter o controle das versões do BD. Ela foi desenvolvidoa seguindo o padrão GitFlow, e usando o _Pre-commit_ para validar se cada commit está no padrão do _conventional commits_.

O desenvolvimento foi realizado seguindo os principios do _Clean Code, Clean Architecture_ e _TDD (Test-Driven-Development)_.


## Como utilizar

...

