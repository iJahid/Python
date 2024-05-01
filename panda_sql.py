import pandas as pd
from sqlalchemy import create_engine
# import psycopg2
# postgre
# engine = create_engine(
#    "postgresql+psycopg2://postgres:a@localhost:5432/ccdb")
# df = pd.read_sql_table('cc_detail', engine)
# print(df)
# mysql database name 'test'
engine = create_engine(
    'mysql+pymysql://root:@localhost:3306/test')
df = pd.read_sql_table('customers', engine)
print(df)
query = '''
                       SELECT
                       customers.`name`,
                       customers.phone_num,
                       orders.`name` AS prod_name,
                       orders.amount
                       FROM
                       customers
                       INNER JOIN orders ON orders.customer_id=customers.id
                       '''
df = pd.read_sql_query(query, engine)
print(df)

# get the csv for insertion
dcust = pd.read_csv('newcustomers.csv')
print(dcust)
# rename the fiedl for matching database
dcust.rename(columns={
    'custname': 'name',
    'phone': 'phone_num'
}, inplace=True)

print(dcust)
# create New Table
dcust.to_sql('customers_new', con=engine, index=True, if_exists='replace')
# appending Exisitng Table
dcust.to_sql('customers', con=engine, index=False, if_exists='append')
df = pd.read_sql('customers', engine)
print(df)
