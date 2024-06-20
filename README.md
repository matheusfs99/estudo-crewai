# Testando CrewAI

## Para mais informações sobre o CrewAI:
 - Site: https://www.crewai.com/
 - Documentação: https://docs.crewai.com/
 - Repositório: https://github.com/joaomdmoura/crewAI

## Para rodar o código siga os seguintes passos:

Clone o repositório em um diretório local do seu computador;
```shell
git clone git@github.com:matheusfs99/estudo-crewai.git
```

Acesse o repositório;
```shell
cd teste-crewai
```

Copie o arquivo .env-example para um arquivo .env e adicione uma API_KEY válida do GPT à variável de ambiente;
```shell
cp .env-example .env
```

Inicialize o contener e execute a aplicação com o comando:
```shell
docker-compose up --build
```