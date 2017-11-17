import pymysql
import random
"""This is a batch system!"""
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='db_customer', autocommit=True)

def insert_into_db(count=51):
    """This function insert many customers name, cpf/cnpj and balance data in database, assigning each customer an unique ID."""
    cur = conn.cursor()
    query = "INSERT INTO tb_customer_account(id_customer, cpf_cnpj, nm_customer, is_active, vl_total) VALUES"
    id_random = random.randint(1,500)
    values = list()

    for item in range(1, count):
        customer = '({id_customer}, \'13089778\', \'Lapis da Silva\', 1, {vl_total})'
        values.append(customer.format(id_customer=id_random*item, vl_total=item*200))

    query += ', '.join(values)
    cur.execute(query)
    cur.close()
    
def search_into_db():
    """TThis function search data at database, return a list of customer that its IDs is above 
    1500 and lower than 1700 and the total value is above 560, then print it final average."""
    cur = conn.cursor()
    select = 'SELECT `nm_customer`, `vl_total` FROM `tb_customer_account`'
    condition = 'WHERE `id_customer` BETWEEN 1500 AND 2700 AND `vl_total` > 560 '
    sort = 'ORDER BY `vl_total`DESC'
    cur.execute(select + condition + sort)
    total_balance = 0
    count = 0
    for row in cur:
        print('Customer {customer}, balance: {total_value}$'.format(customer=row[0],total_value=row[1]))
        total_balance += row[1]
        count+=1
    final_average =  total_balance/count 
    print('Final average: {final:.2f}'.format(final=final_average))
    cur.close()

if __name__ == '__main__':
    insert_into_db()
    search_into_db()
    conn.close()