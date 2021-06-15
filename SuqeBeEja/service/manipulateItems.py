from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine
import datetime

selectItem = text(
    """
        SELECT * from productTable WHERE product_id = :item_id
        """
)


def addNewItem(item, seller_id):
    for key in item:
        if item[key] == "":
            return "Error: Empty file exists!!"

    item['date'] = datetime.date.today()
    item['item_provider'] = seller_id
    createItemStatement = text(
        """
            INSERT into productTable
            (product_name, product_price, product_sub_dep, amount, seller,
            brand, manufacturer, length, width, height, weight, date_published, 
            condition, is_featured, feature, description) VALUES
            (:item_name, :item_price, :item_sub_dep, :item_quantity, :item_provider,
            :item_brand, :item_manufacturer, :item_length, :item_width, :item_height,
            :item_weight, :date, :condition, :is_featured, :item_features, :item_description) RETURNING product_id
        """
    )

    with engine.connect() as con:
        try:
            i_id = con.execute(createItemStatement, **item).first()
            item_id = {'item_id': i_id[0]}

            result = con.execute(selectItem, **item_id)

            return jsonify({'Items': [dict(row) for row in result]})

        except Exception as error:
            return {"Error": str(error)}


def updateItem(item, seller_id, item_id):
    item['item_provider'] = seller_id
    item['item_id'] = item_id
    updateItemStatement = text(
        """
            UPDATE productTable SET
            product_name = :item_name, product_price = :item_price, 
            product_sub_dep = :item_sub_dep, amount = :item_quantity, seller = :item_provider,
            brand = :item_brand, manufacturer = :item_manufacturer, 
            length = :item_length, width = :item_width, height = :item_height, weight = :item_weight, 
            condition = :condition, is_featured = :is_featured, 
            feature = :item_features, description = :item_description
            WHERE product_id = :item_id
        """
    )

    with engine.connect() as con:

        try:
            con.execute(updateItemStatement, **item)

            result = con.execute(selectItem, **item)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def deleteItem(seller_id, item_id):
    i_id = {"id": item_id, 'seller' : seller_id}
    deleteCustomerStatement = text(
        """
            DELETE FROM productTable WHERE product_id = :id AND seller = :seller
        """
    )
    with engine.connect() as con:
        try:
            con.execute(deleteCustomerStatement, **i_id)
  
            return "Successfully deleted"
        except Exception as error:
            return "Error: " + str(error)
