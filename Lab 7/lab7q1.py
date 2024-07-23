# lab7q1 Vic 24283699

import mysql.connector

try:
    cnx = mysql.connector.connect(user='rlawrenc', password='test', host='cosc304.ok.ubc.ca', database='WorksOn')
    cursor = cnx.cursor()
    query = ("SELECT dept.dno, dname, proj.pno, pname, SUM(hours), COUNT(eno) FROM workson,dept,proj WHERE budget > 140000 AND workson.pno = proj.pno AND dept.dno = proj.dno GROUP BY pno ORDER BY SUM(hours) DESC")    
    cursor.execute(query)
    print("dno" + " " + "dname" + "     pno " + " pname" + "" + "   hours" + "" + " numemp")
    for( dno, dname, pno, pname, sumeno, counteno ) in cursor:
        print( dno+ " " + dname+ " " + pno+ " " + pname,  sumeno,  counteno )
    cursor.close()
    
except mysql.connector.Error as err:  
    print(err)
    
finally:
    cnx.close()