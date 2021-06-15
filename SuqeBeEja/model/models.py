from flask_restplus import fields

customer_model_templet = {
    'buyer_name': fields.String,
    'buyer_region': fields.String,
    'buyer_city': fields.String,
    'buyer_street_number': fields.String,
    'buyer_phone_number': fields.Integer,
    'buyer_email': fields.String,
    'buyer_Password': fields.String
}

seller_model_templet = {
    'sales_Name': fields.String,
    'sales_company_Name': fields.String,
    'sales_Region': fields.String,
    'sales_City': fields.String,
    'sales_Street_Number': fields.String,
    'sales_Phone_Number': fields.Integer,
    'sales_Email': fields.String,
    'sales_Password': fields.String
}

product_model_templet = {
    'item_name': fields.String,
    'item_price': fields.Float,
    'item_sub_dep': fields.Integer,
    'item_quantity': fields.Integer,
    'item_brand': fields.String,
    'item_manufacturer': fields.String,
    'item_length': fields.Float,
    'item_width': fields.Float,
    'item_height': fields.Float,
    'item_weight': fields.Float,
    'condition': fields.String,
    'is_featured': fields.String,
    'item_features': fields.String,
    'item_description': fields.String
}
