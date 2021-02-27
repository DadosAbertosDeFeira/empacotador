import argparse
import os
import pathlib
import urllib.parse as urlparse

import psycopg2
from psycopg2 import Error

url = urlparse.urlparse(os.environ["DATABASE_URL"])


def execute_query(query, filename):
    try:
        connection = psycopg2.connect(
            dbname=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port,
        )
        cursor = connection.cursor()
        print("PostgreSQL conectado.")

        output = f"COPY ({query}) TO STDOUT WITH CSV HEADER"
        with open(f"{filename}.csv", "w") as f:
            cursor.copy_expert(output, f)
        print(f"Resultado: {filename}.csv")
    except Error as error:
        print("Erro durante conexão com o PostgreSQL.", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o PostgreSQL fechada.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gera pacotes de dados.")
    parser.add_argument("query_filepath", help="Arquivo com query.sql")
    parser.add_argument(
        "--filename", default="results", help="Nome do arquivo de resultados."
    )
    args = parser.parse_args()
    path = pathlib.Path(args.query_filepath)
    filepath = f"{path.parent}/datapackage-{args.filename}"

    print(f"Query: {path}")
    execute_query(path.read_text(), filepath)
