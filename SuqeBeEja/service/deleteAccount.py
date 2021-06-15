from sqlalchemy import text
from SuqeBeEja import engine


def deleteSellerFun(seller_id):
    s_id = {"id": seller_id}
    deleteSellerStatement = text(
        """
            DELETE FROM sellerTable WHERE seller_id = :id
        """
    )
    with engine.connect() as con:
        try:
            con.execute(deleteSellerStatement, **s_id)
  
            return "Successfully deleted"
        except Exception as error:
            return "Error: " + str(error)


def deleteCustomerFun(customer_id):
    c_id = {"id": customer_id}
    deleteCustomerStatement = text(
        """
            DELETE FROM customerTable WHERE customer_id = :id
        """
    )
    with engine.connect() as con:
        try:
            con.execute(deleteCustomerStatement, **c_id)
  
            return "Successfully deleted"
        except Exception as error:
            return "Error: " + str(error)