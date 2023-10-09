from airflow.providers.sqlite.hooks.sqlite import SqliteHook
import csv

def extract():
    hook = SqliteHook(sqlite_conn_id="Northwind_small.sqlite")
    conn = hook.get_conn()
    cursor = conn.cursor()
    query = """
        select
            * 
        from `Order`
    """
    cursor.execute(query)
    data = cursor.fetchall()
        
    output_csv_path = 'output_orders.csv'

    with open(output_csv_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        column_names = [description[0] for description in cursor.description]
        csv_writer.writerow(column_names)

        csv_writer.writerows(data)

    print(f"Tabela 'Order' criada no {output_csv_path}")

extract()