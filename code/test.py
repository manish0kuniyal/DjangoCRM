import psycopg2 as pg2

hostname='localhost'
database='dvdRental'
username='postgres'
pwd='sql'
port_id=5432

conn=pg2.connect(dbname=database,user=username,password=pwd,port=port_id,host=hostname)

print("..connected",conn)
conn.close()
