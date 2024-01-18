import database.psql as psql


def get_warehouses() -> dict:
    sql = f"""SELECT 
        warehouses.id AS warehouses_id,
        warehouses.title,
        warehouses.user_id,
        warehouses.integration_id,
        warehouses.status_id
        FROM public.warehouses
        LEFT JOIN public.warehouse_statuses ON warehouses.status_id = warehouse_statuses.id
        LEFT JOIN public.integrations ON warehouses.integration_id = integrations.id
        """
    try:
        data = {"data": psql.sql_fetchall(sql)}
    except Exception as e:
        print(e)
        data = {"data": []}
    return data