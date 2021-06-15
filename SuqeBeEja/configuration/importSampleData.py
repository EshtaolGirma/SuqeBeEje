import csv
from SuqeBeEja import engine
from sqlalchemy.sql.expression import text



insertItemSQL = text(
    """
    INSERT INTO productTable(product_name, product_price, product_sub_dep,
    amount, seller, brand, manufacturer, length, width, height, weight,
    date_published, condition, is_featured, feature, description)
    VALUES(:name, :price, :sub_dep, :quantity, :provider, :brand, 
    :manufacturer, :length, :width, :height, :weight, :date_published, :condition, :is_featured, :features, :description) 
    """
)


with open('SuqeBeEja/configuration/SampleItems.csv', 'r') as sample:
    csv_reader = csv.reader(sample)

    next(csv_reader)
    li = []
    for item in csv_reader:
        items = {'name': item[0], 'price': item[1],
                'sub_dep': item[2], 'quantity': item[3],
                'provider': item[4], 'brand' : item[5],
                'manufacturer' : item[6], 'length' : item[7],
                'width' : item[8], 'height' : item[9],
                'weight' : item[10], 'date_published' : item[11],
                'condition' : item[12], 'is_featured' : item[13],
                'features' : item[14], 'description' : item[15]
                }
        with engine.connect() as con:
            result = con.execute(insertItemSQL, **items)
        li.append(result)
    print(li)