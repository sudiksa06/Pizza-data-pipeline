import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(pizza_sales,pizza_recipe, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    pizza_recipe = pizza_recipe.drop_duplicates().reset_index(drop=True)
    pizza_sales = pizza_sales.drop_duplicates().reset_index(drop=True)


    #fact_table
    fact_table = pizza_sales[['order_details_id','order_id', 'pizza_id', 'quantity', 'unit_price', 'total_price' ]]

    
    #pizza_order_dim
    pizza_order_dim = pizza_sales[['order_id']]
    pizza_order_dim['datetime_column'] = pd.to_datetime(pizza_sales['order_date'] + ' ' + pizza_sales['order_time'], format='%Y-%m-%d %H:%M:%S')
    pizza_order_dim['order_month'] = pizza_order_dim['datetime_column'].dt.month_name()
    pizza_order_dim['order_day'] = pizza_order_dim['datetime_column'].dt.day_name()

    #pizza_id_dim
    pizza_id_dim = pizza_recipe[['pizza_name']]
    pizza_id_dim['pizza_id'] = pizza_sales['pizza_id']
    pizza_id_dim['pizza_size'] = pizza_sales['pizza_id'].str[-1]
    pizza_id_dim['pizza_size'] = pizza_id_dim['pizza_size'].replace({'s': 'small', 'm': 'medium', 'l': 'large'})
    pizza_id_dim['pizza_ingredients'] = pizza_recipe[['pizza_ingredients']]



    return {"fact_table":fact_table.to_dict(orient="dict"),
    "pizza_order_dim":pizza_order_dim.to_dict(orient="dict"),
    "pizza_id_dim":pizza_id_dim.to_dict(orient="dict")}


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
