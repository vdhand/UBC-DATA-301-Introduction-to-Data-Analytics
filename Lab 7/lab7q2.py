# lab7q2 Vic 24283699

import mysql.connector
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

ageList = []
salaryList = []

try:
    cnx = mysql.connector.connect(user='rlawrenc', password='test', host='cosc304.ok.ubc.ca', database='WorksOn')
    cursor = cnx.cursor()
    query = ("SELECT timestampdiff(YEAR, bdate, CURDATE()), salary FROM  emp WHERE salary > 20000 AND salary < 55000 ORDER BY salary DESC")    
    cursor.execute(query)
    print("age" + " " + "salary")
    for(age, salary) in cursor:
        print( int(age), salary )
        ageList.append(float(age))
        salaryList.append(float(salary))
    cursor.close()
    
except mysql.connector.Error as err:  
    print(err)
    
finally:
    cnx.close()

x = np.array(ageList)
y = np.array(salaryList)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print("Predicted y-values:",predict_y)
pred_error = y - predict_y
print("Prediction error:",pred_error)
degr_freedom = len(x) - 2
residual_std_error = np.sqrt(np.sum(pred_error**2) / degr_freedom)
print("Residual error:",residual_std_error)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.plot(x, y, 'o')
plt.plot(x, predict_y, 'k-')
plt.show()