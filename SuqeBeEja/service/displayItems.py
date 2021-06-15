from sqlalchemy import text
from flask import jsonify
from SuqeBeEja import engine
from datetime import date
import datetime


def displayFeaturedItems():
    current_date = date.today()
    lastweek = current_date - datetime.timedelta(days=7)
    expire = {'current': current_date, 'lastweek': lastweek, 'status': 'day'}
    featuredItemsStatement = text(
        """ 
            SELECT product_id,
             product_name, product_price, product_sub_dep, amount, brand, manufacturer,
             length, width, height, weight, date_published, condition, feature, description, 
             seller_name, company_name, seller_phone_number, seller_email,
             department_name, sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            INNER JOIN sellerTable st
            ON pt.seller = st.seller_id
            WHERE pt.is_featured = :status AND date_published BETWEEN :lastweek AND :current 
            """
    )

    with engine.connect() as con:

        try:
            result = con.execute(featuredItemsStatement, **expire)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def displayItemsByDepartment(dep_name):
    selector = {'name': '%'+dep_name+'%'}
    selectByDepName = text(
        """ 
            SELECT 
             product_name, product_price, product_sub_dep, amount, brand, manufacturer,
             length, width, height, weight, date_published, condition, feature, description, 
             seller_name, company_name, seller_phone_number, seller_email,
             department_name, sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            INNER JOIN sellerTable st
            ON pt.seller = st.seller_id
            WHERE department_name LIKE :name
            """
    )

    with engine.connect() as con:

        try:
            result = con.execute(
                selectByDepName, **selector)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def displayItemsBySubDepartment(sub_dep_name):
    selector = {'name': '%'+sub_dep_name+'%'}
    selectByDepName = text(
        """ 
            SELECT 
             product_name, product_price, product_sub_dep, amount, brand, manufacturer,
             length, width, height, weight, date_published, condition, feature, description, 
             seller_name, company_name, seller_phone_number, seller_email,
             department_name, sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            INNER JOIN sellerTable st
            ON pt.seller = st.seller_id
            WHERE sub_dep_name LIKE :name
            """
    )

    with engine.connect() as con:

        try:
            result = con.execute(
                selectByDepName, **selector)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)


def displayItemsByName(product_name):
    selector = {'name': '%'+product_name+'%'}
    # return str(selector["name"])
    selectByName = text(
        """ 
            SELECT 
             product_name, pt.product_id, product_price, product_sub_dep, amount, brand, manufacturer,
             length, width, height, weight, date_published, condition, feature, description, 
             seller_name, company_name, seller_phone_number, seller_email,
             department_name, sub_dep_name
            FROM productTable pt 
            INNER JOIN subDepartmentTable sdt
            ON sdt.sud_dep_id = pt.product_sub_dep
            INNER JOIN departmentTable dt
            ON dt.dep_id = sdt.department_id
            INNER JOIN sellerTable st
            ON pt.seller = st.seller_id
            WHERE product_name LIKE :name
            """
    )

    with engine.connect() as con:

        try:
            result = con.execute(selectByName, **selector)

            return jsonify({'Items': [dict(row) for row in result]})
        except Exception as error:
            return "Error occurred" + str(error)
