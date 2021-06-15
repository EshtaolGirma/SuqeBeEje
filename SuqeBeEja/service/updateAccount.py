from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine


def updateSellerFun(seller, s_id):
    seller["s_id"] = s_id
    updateSellerStatement = text(
        """
            UPDATE sellerTable SET
            seller_name = :sales_Name, company_name = :sales_company_Name,
            seller_region = :sales_Region,
            seller_city = :sales_City, seller_street_number = :sales_Street_Number,
            seller_phone_number = :sales_Phone_Number, seller_email = :sales_Email
            WHERE seller_id = :s_id
        """
    )

    selectTable = text(
        """
            SELECT * FROM sellerTable WHERE seller_id = :s_id
        """
    )
    with engine.connect() as con:

        try:
            con.execute(updateSellerStatement, **seller)

            result = con.execute(selectTable, **seller)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def updateCustomerFun(customer, c_id):
    customer["c_id"] = c_id
    updateCustomerStatement = text(
        """
            UPDATE customerTable SET
            customer_name = :buyer_name, customer_region = :buyer_region,
            customer_city = :buyer_city, customer_street_number = :buyer_street_number,
            customer_phone_number = :buyer_phone_number, customer_email = :buyer_email
            WHERE customer_id = :c_id
        """
    )

    selectTable = text(
        """
            SELECT * FROM customerTable WHERE customer_id = :c_id
        """
    )
    with engine.connect() as con:

        try:
            con.execute(updateCustomerStatement, **customer)

            result = con.execute(selectTable, **customer)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)
