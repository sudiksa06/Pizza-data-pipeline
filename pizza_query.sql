CREATE TABLE pizza AS
SELECT
    f.order_details_id,
    f.order_id,
    f.pizza_id,
    f.quantity,
    f.unit_price,
    f.total_price,
    pid.pizza_name,
    pid.pizza_size,
    pid.pizza_ingredients,
    pod.datetime_column,
    pod.order_month,
    pod.order_day
FROM
    fact_table f
JOIN
    pizza_id_dim pid ON f.pizza_id = pid.pizza_id
JOIN
    pizza_order_dim pod ON f.order_id = pod.order_id;
