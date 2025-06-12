
import mysql.connector
  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database ="tespit"
)
 
print(dataBase)

mycursor = dataBase.cursor()
mycursor2 = dataBase.cursor()
mycursor3 = dataBase.cursor()
mycursor.execute("SELECT il, ilce, mah ,cilt ,hane, gorev  FROM personel ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[5] + " ...") 
  #print(x[0] +" "+ x[1])  
  il = x[0] 
  ilce = x[1]
  mah = x[2]
  cilt = str(x[3])
  hane = str(x[4])
  gorev = x[5]

  sql2 = "SELECT count(id) FROM personel where il LIKE '"+il+"' and ilce LIKE '"+ilce+"'  and mah LIKE '"+mah+"' and cilt LIKE '"+cilt+"' and hane LIKE '"+hane+"'"
  mycursor2.execute(sql2)
  myresult2 = mycursor2.fetchall()
  for y in myresult2:  
    print (y[0])
    knt = str(y[0])
    sql3 = "UPDATE personel SET knt = "+knt+" WHERE gorev LIKE '"+gorev+"'"
    mycursor3.execute(sql3)
    dataBase.commit()
 
  

dataBase.close()