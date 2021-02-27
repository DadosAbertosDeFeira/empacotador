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

## Como os dados são exportados?

Por enquanto é feito de maneira manual. Dentro de cada diretório de _datasets_
você encontrará um `query.sql` com a _query_ utilizada para exportação dos dados.

## Como os dados são validados?

Utilizamos o [Frictionless Data](https://frictionlessdata.io) para criar o esquema de dados e,
posteriormente, validá-los. Veja mais sobre o _table-schema_ [aqui](https://specs.frictionlessdata.io/table-schema/#concepts).

## Como contribuir?

* Postgres
* Poetry
