import random
from db_query_script.date_gen import f

datelist = f()

l = [
    ('1', '1900', '25'),
('2', '7900', '10'),
('3', '15000', '2'),
('4', '1500', '5'),
('5', '1190', '12'),
('6', '3500', '5'),
('7', '3200', '10'),
('8', '1490', '15'),
('9', '2500', '5'),
('10', '790', '20'),
]


def random_part():
    return l[random.randint(0, 9)]

def inv_gen(i):
    if i < 10:
        return 'INV0000'+str(i+1)
    if i < 100:
        return 'INV000'+str(i+1)
    if i < 1000:
        return 'INV00'+str(i+1)


def query_gen():
    query = f'''INSERT INTO d_entry (entry_id, part_id, container_qty, pieces_qty, price, time, cust_id, invoice_no)
VALUES '''
    postfix_query = ''
    for i in range(1000):
        part_id, price, c_capacity = random_part()
        
        c_qty = random.randint(2, 50)
        p_qty = random.randint(0, 50)
        cust_id = random.randint(1, 100)

        t_price = (int(c_qty) * int(c_capacity) + int(p_qty)) * float(price)
        
        inv = inv_gen(i)
        postfix_query += f"('{i+1}', '{part_id}', '{c_qty}', '{p_qty}', '{t_price}', '{datelist[i]}', '{cust_id}', '{inv}')," + "\n"
    return query+postfix_query

with open('text.txt', 'w') as file:
    file.write(query_gen())