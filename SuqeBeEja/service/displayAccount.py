from flask import jsonify
from sqlalchemy.sql import text
from SuqeBeEja import engine


def displaySalesPersonAccount(salesperson_id):
    s_id = {"id": salesperson_id}
    displaySellerStatement = text(
        """
            SELECT * FROM sellerTable WHERE seller_id = :id
        """
    )

    with engine.connect() as con:
        result = con.execute(displaySellerStatement, **s_id)
    return jsonify({'Salesperson': [dict(row) for row in result]})


def displayCustomerAccount(customer_id):
    c_id = {"id": customer_id}
    displayCustomerStatement = text(
        """
            SELECT * FROM customerTable 
        """
    )

    with engine.connect() as con:
        result = con.execute(displayCustomerStatement)
    return jsonify({'Customer': [dict(row) for row in result]})
