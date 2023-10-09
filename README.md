# Indicium - Airflow Challenge
This repository contains the solution for the Airflow Challenge of the Lighthouse 2023-4 program.

## The Challenge
The challenge consists of the following steps:

1- Create a task that reads data from the 'Order' table of the database available at `data/Northwind_small.sqlite``. This task should write to a file called `output_orders.csv``.

2- Create a task that reads data from the 'OrderDetail' table of the same database and performs a `join` with `output_orders.csv`. This task should calculate the quantity sold destined for Rio de Janeiro, and the count should be exported to a file `count.txt` containing only the value in text format.

3- Add a variable in Airflow with the `key` equal to `my_email` and in the value field, add your email address @indicium.tech.

4- Create a task execution order that should end with the task `export_final_output``.

## Installation
> The installation commands mentioned here are for the Ubuntu operating system. For other systems, adjustments to the commands may be necessary.

1- Clone the repository to your local machine.
Paste the following code into your terminal:

`git clone git@bitbucket.org:indiciumtech/airflow_debora.git`

2- Create a virtual environment.
Navigate to the local repository folder and in the terminal, type:

`python3 -m venv venv`

3- Activate the virtual environment.

`source venv/bin/activate`

4- Make changes to the "airflow.cfg" file.
To make the project run on your machine, some path changes will be necessary. You should replace the path where the repository was cloned on your computer.

> Wherever it says "path/to", replace it with the path on your computer.

`dags_folder = ////path/to/airflow-project/airflow-data/dags`

`sql_alchemy_conn = sqlite: ////path/to/airflow-project/data/Northwind_small.sqlite`

`base_log_folder = ////path/to/airflow-project/airflow-data/logs`

`dag_processor_manager_log_location = ////path/to/airflow-project/airflow-data/logs/dag_processor_manager/dag_processor_manager.log`

5- Install Apache Airflow.
To install Apache Airflow, enter the following code in your terminal:

`bash install.sh`

If everything went well, the terminal will display the following message:

```
standalone | 
standalone | Airflow is ready
standalone | Login with username: admin  password: ******
standalone | Airflow Standalone is for development purposes only. Do not use this in production!
standalone |

```
The password is generated automatically by Airflow and will appear in the logs, replacing "******."

Airflow runs on port 8080, so you can access it at
http://localhost:8080

7- In the Airflow interface, add the database connection:

- Connection Id: Northwind_small.sqlite
- Conn Type: SQLite
- Host: /path/to/airflow-project/data/nortwind_small.sqlite (the path to the file on your machine)
> All other options can be left blank.
- Save

8- Running the DAG.
To execute the DAG:

- In the "DAGS" tab, activate the DAG `desafio-airflow`;
- Click on "Trigger DAG" in the Airflow interface;
- Check the output in `final_output.txt`.