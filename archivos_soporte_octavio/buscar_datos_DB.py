import pymysql
import pandas as pd
import pylab  as pl

# amplio el tapaño de los puntos
pl.rcParams['agg.path.chunksize'] = 10000

try:
    conexion = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='',
                             db='employees')
    try:
        #cargo el data frame de la base de datos en el were tiene una condicion que sean mejor a 1997
        salarios_array = pd.read_sql_query("SELECT s.emp_no,s.salary, s.from_date , d.dept_name, (DATEDIFF(s.to_date,s.from_date)/365) TIEMPO_Y FROM `salaries` s inner join employees e on s.`emp_no` = e.emp_no INNER join dept_emp de on de.emp_no = e.emp_no INNER join departments d on  d.dept_no = de.dept_no WHERE /* s.from_date < '1997-01-01' AND */ s.emp_no = 10001", conexion)
        #convierto el campo fecha con pando para que se agraficable
        salarios_array.from_date = pd.to_datetime(salarios_array.from_date)
        
        #salarios_array['salary']['dept_name'].plot(figsize=(20, 10))
       # pl.plot(salarios_array['salary'], salarios_array['dept_name'] )
        pl.plot(salarios_array['from_date'], salarios_array['salary'])
        
        pl.show()
        pl.plot(salarios_array['from_date'], salarios_array['TIEMPO_Y'])
        
        pl.show()
        
    finally:
        conexion.close()
    
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)