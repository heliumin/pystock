
import pymysql;

def getLinkFromDb():
    db = pymysql.connect(host="localhost", user="root", password="", database="stock")
    cur = db.cursor()
    cur.execute("use stock;")
    cur.execute("select * from stock.STOCK_INDUSTRY")
    data=cur.fetchall()
    return data

if __name__ == "__main__":
    links = getLinkFromDb()
