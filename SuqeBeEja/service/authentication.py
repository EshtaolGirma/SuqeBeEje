from SuqeBeEja import engine
from flask import jsonify
from sqlalchemy.sql.expression import text

def authenticationfunction(email, password):
    with engine.connect() as con:
        departmentsImportStatement = text(
        """
            SELECT * FROM productTable
        """
        )
        result = con.execute(departmentsImportStatement)
    return jsonify({'Items': [dict(row) for row in result]})

    