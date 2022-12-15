# TP3 ITBA Cloud data engineer --> airflow + Docker + DB + Dashboard



## Steps:

- [x] Levantar airflow con el file `docker-compose` YAML file.

- [x] Crear database en postgres SQL en donde van a estar la data de stocks (en el caso del ejemplo: SPY, AAPL, MSFT)
![db](/documents/database_scheme.PNG "db scheme")
![db](/documents/database_list_of_databases.PNG "db databases")
![db](/documents/database_tables.PNG "db tables")

- [x] La base de datos se inicia con un .sql script dentro del init.sql de postgres. 

- [x] Se desarrollo el modelo para captar datos desde la API de distintos TICKERS, guardarlos en una base de datos (previamente creada y configurada) y luego levantar una app de plotly para ver los stats de closing prices

![dag](/documents/DAG_airflow.PNG "DAG")


➲ Se crearon los files de las consignas, la clase de python con el cliente SQL, los files de carga de datos y extracción de datos y el dag correspondiente

- [x] Se pueden ver los datos en un grafico creado con plotly

![plotly](/documents/dash_pic1.PNG "plotly")
![plotly](/documents/dash_pic2.PNG "plotly")
![plotly](/documents/dash_pic3.PNG "plotly")




## Deploy and test

- Clonar el repo
- Adentro del directorio principal correr `docker-compose up -d` (se puede optar por subir primero airflow-init para determinar que esta todo ok, y luego hacer el docker-compose up -d )
- Logearse [Airflow UI](http://localhost:8080) _(user: airflow, password: airflow)_
- Activar el dag y esperar a que corra todo
- Abrir [Ticker Dashboard](http://127.0.0.1:8050), elegir el ticker y ver el grafico de los precios
           