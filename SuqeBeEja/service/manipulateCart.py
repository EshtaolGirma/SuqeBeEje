from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine


def displayCartContent(customer_id):
    displayCartStatement = text(
        """
        SELECT pt.product_name, pt.product_id, ot.amount, product_price
        FROM productTable pt
        INNER JOIN orderTable ot
        ON pt.product_id = ot.product_id
        INNER JOIN customerTable ct 
        ON ct.customer_id = ot.customer_id
        WHERE ot.customer_id = :id AND paid = :paid
        """
    )

    with engine.connect() as con:

        try:
            result = con.execute(displayCartStatement, {
                                 'id': customer_id, 'paid': 'n'})

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def addItemToCart(customer, product, quantity):
    addToCartStatement = text(
        """
        INSERT INTO orderTable
        (customer_id, product_id, amount, paid)
        VALUES (:customer, :product, :quantity, :paid)
        """
    )

    item = {'customer': customer, 'product': product,
            'quantity': quantity, 'paid': 'n'}

    with engine.connect() as con:

        try:
            result = con.execute(addToCartStatement, **item)

            return displayCartContent(customer)
        except Exception as error:
            return "Error occurred" + str(error)


def editItemOnCart(customer, product, quantity):

    item = {'customer': customer, 'product': product,
            'quantity': quantity, 'paid': 'n'}
    editCartStatement = text(
        """
        UPDATE orderTable SET amount = :quantity
        WHERE customer_id = :customer AND product_id = :product AND paid = :paid
        """
    )

    with engine.connect() as con:

        try:
            con.execute(editCartStatement, **item)

            return displayCartContent(customer)
        except Exception as error:
            return "Error occurred" + str(error)


def deleteItemFromCart(customer, product):
    deleteCartStatement = text(
        """
        DELETE FROM orderTable WHERE customer_id = :customer AND product_id = :product AND paid = :paid
        """
    )
    item = {'customer': customer, 'product': product, 'paid': 'n'}
    with engine.connect() as con:

        try:
            con.execute(deleteCartStatement, **item)

            return displayCartContent(customer)
        except Exception as error:
            return "Error occurred" + str(error)


# CHECK amount size
