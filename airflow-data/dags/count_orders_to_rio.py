from airflow.providers.sqlite.hooks.sqlite import SqliteHook
import csv

def count_orders():
    
    hook = SqliteHook(sqlite_conn_id="Northwind_small.sqlite")
    conn = hook.get_conn()
    cursor = conn.cursor()

    query = """
        with 
            order_table as (
                select 
                    *
                from `Order` 
                where ShipCity = 'Rio de Janeiro'
        )
        , orders_detail_table as (
            select 
                OrderID
                , Quantity 
            from `OrderDetail`
        )
        , joined as (
            select 
                SUM(orders_detail_table.Quantity) as total_quantity
            from orders_detail_table
            inner join order_table 
                on orders_detail_table.OrderID = order_table.ID
        )

        select 
            * 
        from joined
    """

    cursor.execute(query)
    result = cursor.fetchone()
    total_quantity = result[0] if result else 0

    count_txt_path = 'count.txt'
    with open(count_txt_path, 'w') as count_file:
        count_file.write(str(total_quantity))

    print(f"Quantidade total vendida com destino para o Rio de Janeiro adicionada a {count_txt_path}")
    
count_orders()