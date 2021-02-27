# empacotador

O nosso empacotador de dados 📦

## Como esse repositório está organizado?

Na pasta _datasets_ você irá encontrar as bases de dados que estamos
disponibilizando. Ela segue a estrutura:

```
datasets
  <orgao-publico>
    <base-de-dados>
        query.sql
        tableschema.json
```

## De onde vem os dados?

Os dados são coletados e armazenados pela [Maria Quitéria](https://github.com/DadosAbertosDeFeira/maria-quiteria/).
Você pode acessá-los em nossa página no [Kaggle](https://www.kaggle.com/dadosabertosdefeira/).

Para baixar os dados localmente você precisará ter configurado a variável de ambiente
`DATABASE_URL` (veja o arquivo `.env.example`).

Então execute o script seguinte passando como parâmetro o arquivo sql desejado e o nome escolhido:

```
python fetch_data.py datasets/prefeitura/licitacoes/query.sql
python fetch_data.py datasets/prefeitura/licitacoes/query.sql --filename licitacoes-da-prefeitura
```

O arquivo com o resultado será criado na mesma pasta do arquivo sql informado.

## Como os dados são exportados?

Por enquanto é feito de maneira manual. Dentro de cada diretório de _datasets_
você encontrará um `query.sql` com a _query_ utilizada para exportação dos dados.

## Como os dados são validados?

Utilizamos o [Frictionless Data](https://frictionlessdata.io) para criar o esquema de dados e,
posteriormente, validá-los. Veja mais sobre o _table-schema_ [aqui](https://specs.frictionlessdata.io/table-schema/#concepts).

## Como contribuir?

Para contribuir você precisará ter instalado:

* Postgres 9+
* Poetry

Esse repositório segue o [código de conduta e o guia de contribuição](https://github.com/DadosAbertosDeFeira/guias)
do Dados Abertos de Feira.
