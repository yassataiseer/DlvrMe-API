import mysql.connector
import os
from mysql.connector.constants import flag_is_set
import requests, json
from decouple import config



class order:
    def connect():
        db =mysql.connector.connect(
        host = config('HOST') ,
        user = config('USERNAME') ,
        passwd = config('PASSWORD'),
        database = config('DATABASE'))
        return db 
    def delete_order(Username,Address,Item,Price,User_Info):
        db = order.connect()
        mycursor = db.cursor()
        Price1 = float(Price)
        mycursor.execute("DELETE FROM deliveries WHERE Username = %s AND Address = %s AND Item = %s AND Price = %s AND User_Info = %s",(Username,Address,Item,Price1,User_Info))
        db.commit()
        mycursor.close()
        db.close()
        return {"Status":True}
    def add_order(Username,Address,Item,Price,User_Info):
        db = order.connect()
        mycursor = db.cursor()
        try:
            url = 'http://photon.komoot.de/api/?q='
            mycursor.execute('SELECT * FROM deliveries')
            data = mycursor.fetchall()
            resp = requests.get(url=url+Address)
            data = json.loads(resp.text)
            a = data['features'][0]['geometry']['coordinates']
            lat = a[-1]
            lon = a[0]
            mycursor.execute("INSERT INTO deliveries (Username,Address,Latitude,longitude,Item,Price,User_Info) VALUES (%s,%s,%s,%s,%s,%s,%s)",(Username,Address,lat,lon,Item,Price,User_Info))
            db.commit()
            mycursor.close()
            db.close()
            return {"Status":True}
        except IndexError:
            db.close()
            return {"Status":False}
    def edit_order(Username,Address,Item,Price,User_Info):
        pass
    def get_order():
        db = order.connect()
        mycursor = db.cursor()
        data = ["Name","Address","Latitude","Longitude","Item","Price","Description"]
        mycursor.execute('SELECT * FROM deliveries')
        data1 = []
        a = mycursor.fetchall()
        for i in a:
            i = dict(zip(data,i))
            data1.append(i)
        mycursor.close()
        db.close()
        return data1
    def get_order_specific_person(username):
        db = order.connect()
        mycursor = db.cursor()
        data = ["Name","Address","Latitude","Longitude","Item","Price","Description"]
        mycursor.execute("SELECT * FROM deliveries WHERE Username = %s",(username,))
        data1 = mycursor.fetchall()
        final = []
        for i in data1:
            data2 = dict(zip(data,i))
            final.append(data2)
        mycursor.close()
        db.close()
        return final
    def grab_address(Address):
        db = order.connect()
        mycursor = db.cursor()
        mycursor.execute("SELECT * FROM deliveries WHERE Address = %s",(Address,))
        data = mycursor.fetchall()
        mycursor.close()
        db.close()
        if len(data)==0:
            return  {"Status":False}
        else:
            return  {"Status":True}
    def validate_address(address):
        try:
            url = 'http://photon.komoot.de/api/?q='
            resp = requests.get(url=url+address)
            data = json.loads(resp.text)
            a = data['features'][0]['geometry']['coordinates']
            return {"Status":True}
        except IndexError:
            return {"Status":False}
    def check_latitude(lat):
        db = order.connect()
        mycursor = db.cursor()
        while True:
            mycursor.execute("SELECT * FROM deliveries WHERE Latitude LIKE %s",(lat,))
            data = mycursor.fetchall()
            if len(data)==0:
                mycursor.close()
                db.close()
                return  lat
            else:
                lat = str(lat)
                lat = list(lat)
                lat[-1] = str(int(lat[-1])+1)
                lat = float("".join(map(str, lat)))
                #return lat
    def check_longitude(long):
        db = order.connect()
        mycursor = db.cursor()
        while True:
            mycursor.execute("SELECT * FROM deliveries WHERE longitude LIKE %s",(long,))
            data = mycursor.fetchall()
            if len(data)==0:
                mycursor.close()
                db.close()
                return  long
            else:
                long = str(long)
                long = list(long)
                long[-1] = str(int(long[-1])+1)
                long = float("".join(map(str, long)))
    

#print(order.check_longitude(-79.8437))
#print(order.get_order_specific_person('Eshal Taiseer'))
#print(order.add_order("Yassa Taiseer","1328fcacfjkcfjnkfjkfj cda cs x","Box",15,"I need this box delivered ASAP"))
#print(order.add_order('Eshal Taiseer', '452 Savoline Blvd Milton,', 'Toy', 15, 'I need this toy delivered ASAP my phone number is 123-456-789'))