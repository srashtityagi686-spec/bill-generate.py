import time as t
import mysql.connector


def bill():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="srashti@123", #enter your password
    use_pure=True,
    database="prod_info" #enter your database name
    )
    cur = con.cursor()
    Order_id=int(input("enter the order id: "))
    Product_Name=input("enter the product name: ")
    Price=float(input("enter the Price: "))
    Quantity=int(input("enter the Quantity: "))
    Amount=Price*Quantity
    sql = "INSERT INTO orderd (Order_id,Product_name,Price,Quantity,Amount) VALUES (%s,%s,%s,%s,%s)"
    values = (Order_id,Product_Name,Price,Quantity,Amount)
    cur.execute(sql,values)
    con.commit()
    print("✅ Data successfully inserted into Products table!")

    amount=Price*Quantity
    name=str(Order_id)
    time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {time}
    --------------------
    order id: {Order_id}
    product name: {Product_Name}
    Quantity: {Quantity}
    ---------------------
    final amount: {amount}''')
    f.close()
    cur.close()
    con.close()
    
bill()