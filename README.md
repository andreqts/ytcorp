# ytcorp

## PRÉ-REQUISITOS (requirements)

1. Linux UBUNTU 20 (ou sistema análogo)
1. Python 3.8.10 ou superior
1. Postgres 12 ou superior
1. SQLAlchemy 2.0.25 ou superior


## SETUP

1- Postgres
  - Configurar acessos (remoto ou local) conforme o uso pretendido (local ou remoto, _peer_, _trust_, _md5_ etc)
  - Criar base de dados antes de rodar o modelo
  - Configurar no arquivo _.bashrc_, no diretório HOME, as seguintes variáveis de ambiente: **YT_DB_NAME**, **YT_DB_USER**, **YT_DB_PASSWORD**, **YT_DB_HOST**, **YT_DB_HOST_PORT**.
