# Indicium - Airflow Challenge

Esse repositório contém a solução para o Desafio do Airflow do programa Lighthouse 2023-4.

## O desafio

O desafio consisite nas seguintes etapas:

1- Criar uma task que lê os dados da tabela 'Order' do banco de dados disponível em `data/Northwind_small.sqlite`. Essa task deverá escrever um aqui chamado `output_orders.csv`

2- Criar uma task que leia os dados da tabela 'OrderDetail' do mesmo banco de dados e realizar um `join` com `output_orders.csv`. Essa task deverá calcular a quantidade vendida com destino ao Rio de Janeiro, a contagen deverá ser exportada em um arquivo `count.txt` que contenha somente o valor em formato de texto.

3- Adicionar uma variável no Airflow com a `key` igual a `my_email` e no campo `value` adicionar o seu email @indicium.tech.

4- Criar uma ordenação de execução das tasks que deverá terminar com a task `export_final_output`. 

## Instalação

> Os comandos de instalação aqui citados são para o sistema operacional Ubuntu, para outros sistemas será necessário realizar ajustes nos comandos.

1- Clonar o repositório na sua máquina local.
Colar no terminal o seguinte código:

`git clone git@bitbucket.org:indiciumtech/airflow_debora.git`

2- Criar um ambiente virtual.
Acesse a pasta local do repositório e no terminal digite:

`python3 -m venv venv`

3- Ative o ambiente virtual.

`source venv/bin/activate`

4- Realizar alterações no arquivo "airflow.cfg"
Para que o projete rode na sua máquinas algumas alterações de caminho serão necessárias serem feitas, você deve colocar o caminho de onde o repositório foi clonado no seu computador.

> Onde estiver "your/path" substituir pelo caminho no seu computador.

`dags_folder = ////your/path/airflow_debora/airflow-data/dags`

`sql_alchemy_conn = sqlite: ////your/path/airflow_debora/data/Northwind_small.sqlite`

`base_log_folder = ////your/path/airflow_debora/airflow-data/logs`

`dag_processor_manager_log_location = ////your/path/airflow_debora/airflow-data/logs/dag_processor_manager/dag_processor_manager.log`

5- Instalar o airflow
Para instalar o airflow escreva o seguinte código no seu terminal:

`bash install.sh`


Se as coisas deram certo, no terminal vai aparecer a seguinte mensagem:

```
standalone | 
standalone | Airflow is ready
standalone | Login with username: admin  password: ******
standalone | Airflow Standalone is for development purposes only. Do not use this in production!
standalone |

```
A senha de fato é gerada automaticamente pelo Airflow e vai aparecer nos logs, no lugar de "****".

Airflow roda na porta 8080, então podemos acessar em 
http://localhost:8080


7- Na interface do Airflow, adicione a conexão com o banco de dados:

- Coon Id: Northwind_small.sqlite
- Conn Type: SQLite
- Host: /your/path/airflow_debora/data/nortwind_small.sqlite (caminho do arquivo na sua máquina)

> Todas as outras opções podem ser deixadas em branco.

- Save

8- Execução da DAG
Para executar a DAG:

- Na aba "DAGS" ative a DAG `desafio-airflow`;
- Clique em "Trigger DAG" na interface do Airflow;
- Verifique o output `final_output.txt`
