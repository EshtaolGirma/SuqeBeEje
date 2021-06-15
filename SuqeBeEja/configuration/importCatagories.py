from sqlalchemy.sql import text
from SuqeBeEja import engine
from SuqeBeEja.configuration.catagories import *

with engine.connect() as con:
    departmentsImportStatement = text(
        """
            INSERT INTO departmentTable(department_name) VALUES(:dep_name)
        """
    )
    for dep in Departments:
        current_dep = {"dep_name": dep}
        con.execute(departmentsImportStatement, **current_dep)

    subDepartmentsImportStatement = text(
        """
            INSERT INTO subDepartmentTable(sub_dep_name, department_id) VALUES(:sub_dep_name, :dep_id)
        """
    )
    index = 0
    for each_sub_dep in sub_dep:
        index += 1
        for sub_dep_name in each_sub_dep:
            add_sub_dep = {"sub_dep_name": sub_dep_name, "dep_id": index}
            con.execute(subDepartmentsImportStatement, **add_sub_dep)
