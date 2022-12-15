# TP3 ITBA Cloud data engineer --> airflow + Docker + DB + Dashboard



## Steps:

- [x] Levantar airflow con el file `docker-compose` YAML file.

- [x] Crear database en postgres SQL en donde van a estar la data de stocks (en el caso del ejemplo: SPY, AAPL, MSFT)

Database Scheme:
<img width="526" alt="database_scheme" src="https://user-images.githubusercontent.com/66229520/207979758-b31d3ed1-a0f7-4972-b588-97fe90ba67e6.png">


Database Databases:
<img width="919" alt="database_list_of_databases" src="https://user-images.githubusercontent.com/66229520/207979771-5584a7a3-53fe-4835-adcf-7fb87edc66c8.png">

Database Tables:
<img width="1306" alt="database_tables" src="https://user-images.githubusercontent.com/66229520/207979785-af4b8df8-02d5-4eec-b9da-3999b65d396d.png">

- [x] La base de datos se inicia/crea con un .sql script dentro del init.sql de postgres. 

- [x] Se desarrollo el modelo para captar datos desde la API de distintos TICKERS, guardarlos en una base de datos (previamente creada y configurada) y luego levantar una app de plotly para ver los stats de closing prices

<img width="1411" alt="DAG_airflow" src="https://user-images.githubusercontent.com/66229520/207979806-9a91d448-ad01-48b6-8649-bfcdf688a645.png">


➲ Se crearon los files de las consignas, la clase de python con el cliente SQL, los files de carga de datos y extracción de datos y el dag correspondiente

- [x] Se pueden ver los datos en un grafico creado con plotly

Plotly ticker Microsoft:
<img width="1423" alt="dash pic1" src="https://user-images.githubusercontent.com/66229520/207979690-68ec7b78-4738-4a66-a1ec-2f69e065997b.png">


Plotly ticker Apple:
<img width="1422" alt="dashpic2" src="https://user-images.githubusercontent.com/66229520/207979711-b57b4847-d5d2-4c03-b784-1dd6a2226d0f.png">


Plotly ticker S&P:
<img width="1420" alt="dashpic3" src="https://user-images.githubusercontent.com/66229520/207979722-8cdac39a-6b57-4cd8-aef4-2965739a4d12.png">





## Deploy and test

- Clonar el repo
- Adentro del directorio principal correr `docker-compose up -d` (se puede optar por subir primero airflow-init para determinar que esta todo ok, y luego hacer el docker-compose up -d )
- Logearse [Airflow UI](http://localhost:8080) _(user: airflow, password: airflow)_
- Activar el dag y esperar a que corra todo
- Abrir [Ticker Dashboard](http://127.0.0.1:8050), elegir el ticker y ver el grafico de los precios
           
