from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine


def sellerStatistics(seller):
    itemsStatement = text(
        """ 
            SELECT pt.product_id,
             pt.product_name, pt.product_price, pt.amount, pt.brand, pt.manufacturer,
             pt.length, pt.width, pt.height, pt.weight, pt.date_published, pt.condition, pt.feature, pt.description, 
             dt.department_name, sdt.sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            
            WHERE pt.seller = :id
            """
    )

    soldItemsStatement = text(
        """ 
            SELECT pt.product_id,
             pt.product_name, pt.product_price, ot.amount, pt.brand, pt.manufacturer,
             pt.length, pt.width, pt.height, pt.weight, pt.date_published, pt.condition, pt.feature, pt.description, 
             dt.department_name, sdt.sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            INNER JOIN orderTable ot
            ON pt.product_id = ot.product_id
            WHERE pt.seller = :id AND ot.paid = :paid
            """
    )

    with engine.connect() as con:

        try:
            result = con.execute(itemsStatement, {'id': seller})
            sold_result = con.execute(
                soldItemsStatement, {'id': seller, 'paid': 'y'})

            return jsonify({'Unsold Items': [dict(row) for row in result]}, {'Sold Items': [dict(row) for row in sold_result]})
        except Exception as error:
            return "Error occurred" + str(error)
