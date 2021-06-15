from SuqeBeEja import engine
from sqlalchemy import text
from flask import jsonify
from werkzeug.security import generate_password_hash


def createSellerAccountFun(new_seller):
    for key in new_seller:
        if new_seller[key] == "":
            return {'error': 'Empty field exist!!'}

    new_seller['sales_Password'] = generate_password_hash(
        new_seller['sales_Password'], method='pbkdf2:sha256', salt_length=8)

    createSellerStatement = text(
        """
            INSERT into sellerTable 
            (seller_name, company_name, seller_region, seller_city, seller_street_number, seller_phone_number, seller_email, seller_password) 
            Values (:sales_Name, :sales_company_Name, :sales_Region, :sales_City, :sales_Street_Number, :sales_Phone_Number, :sales_Email, :sales_Password)
        """
    )

    selectTable = text(
        """
            SELECT * FROM sellerTable WHERE seller_email = :sales_Email
        """
    )
    with engine.connect() as con:
        checkExistence = con.execute(selectTable, **new_seller)

        flag = None
        for row in checkExistence:
            flag = row

        if flag != None:
            return {"status": 'user exists'}
        else:
            try:
                con.execute(createSellerStatement, **new_seller)

                result = con.execute(selectTable, **new_seller)

                return jsonify({'Items': [dict(row) for row in result]})
            except Exception as error:
                return {"Error": str(error)}


def createCustomerAccountFun(new_buyer):
    for key in new_buyer:
        if new_buyer[key] == "":
            return {'error': 'Empty field exist!!'}

    new_buyer['buyer_Password'] = generate_password_hash(
        new_buyer['buyer_Password'], method='pbkdf2:sha256', salt_length=8)

    createSellerStatement = text(
        """
            INSERT into customerTable 
            (customer_name, customer_region, customer_city, customer_street_number, customer_phone_number, customer_email, customer_password) 
            Values (:buyer_name, :buyer_region, :buyer_city, :buyer_street_number, :buyer_phone_number, :buyer_email, :buyer_Password)
        """
    )

    selectTable = text(
        """
            SELECT * FROM customerTable WHERE customer_email = :buyer_email
        """
    )
    with engine.connect() as con:
        checkExistence = con.execute(selectTable, **new_buyer)

        flag = None
        for row in checkExistence:
            flag = row

        if flag != None:
            return {"status": 'user exists'}
        else:
            try:
                con.execute(createSellerStatement, **new_buyer)

                result = con.execute(selectTable, **new_buyer)

                return jsonify({'Items': [dict(row) for row in result]})
            except Exception as error:
                return {"Error": str(error)}
