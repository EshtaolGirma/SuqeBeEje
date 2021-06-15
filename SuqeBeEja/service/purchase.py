from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine


def payout(customer):
    item = {'customer': customer, 'paid': 'y'}
    checkStatement = text(
        """
        UPDATE orderTable SET paid = :paid
        WHERE customer_id = :customer
        """
    )

    getOriginalQuantityStatement = text(
        """
        SELECT amount FROM productTable WHERE product_id = :item_id
        """
    )

    getSoldItemQuantityStatement = text(
        """
        SELECT amount, product_id
        FROM orderTable
        WHERE customer_id = :id AND paid = :paid
        """
    )
    removeSoldItemStatement = text(
        """
        UPDATE productTable SET amount = :new_amount
        """
    )

    with engine.connect() as con:

        try:
            soldQuantityResult = con.execute(
                getSoldItemQuantityStatement, {'id': customer, 'paid': 'n'})
            for i in soldQuantityResult:
                soldQuantity = i[0]
                soldItemID = i[1]
                initialQuantityResult = con.execute(getOriginalQuantityStatement, {
                    'item_id': soldItemID})
                for j in initialQuantityResult:
                    initialQuantity = j[0]

                con.execute(removeSoldItemStatement, {
                            'new_amount': int(initialQuantity - soldQuantity)})
            con.execute(checkStatement, **item)

            return "Successful"
        except Exception as error:
            return "Error occurred" + str(error)


def purchaseHistroy(customer):
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
                                 'id': customer, 'paid': 'y'})

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)
