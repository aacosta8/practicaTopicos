# Practica 4 Tópicos especiales en Telemática
### Clústering de Documentos a partir de Métricas de Similitud basado en Big Data


Integrantes del grupo:
 * Alexander Acosta Jiménez
 * Julián  David Arango López

 ## 1. Descripción del proyecto:
 Este proyecto  consiste en analizar un conjunto de documentos (datasets), y dado un número k reagrupar los documentos dependiendo de su grado de similitud. En esta ocasión el proyecto se apoyo de dos bibliotecas de spark para lograr este objetivo, las cuales son K-Means (agrupar por similitud) y TF-IDF(calcular el peso de una palabra en cada documento. Insumo para el algoritmo de K-Means).

 ## 2. Como de ejecutar:

 Para ejecutar localmente se debe correr el siguiente comando:

    ```spark-submit spark_kmeans.py```

 Y para ejecutarlo en el cluster el siguiente comando:

 ``` spark-submit --master yarn --deploy-mode cluster --executor-memory 2G --num-executors 4 spark_kmeans.py```

 Para realizar las pruebas se crearon subconjuntos de 50, 100, 150, 200, 250, 300, 350 y 400 documentos, que estan contenidos en carpetas en el DFS nombrados con el número de documento.
 Estan ubicados en la siguiente ruta hdfs:///user/jarangol/datasets/<numero_de_docs>"
 y la salida esta ubicada en la siguiente ruta "hdfs:///user/jarangol/kmeans/<test_numero_cantidaddocs"

 ## 3. Dependencias:
 * TF-IDF (Term frequency – Inverse document frequency): Es un método de vectorización de características ampliamente utilizado en la minería de textos para reflejar la importancia de un término para un documento

 El calculo del TF es solo contar las ocurrencias de una palabra en un documento.

 Para calcular el IDF se utiliza la sigiente formula:

 ![Tech](/formula04_idf.png)

 Después de calcular esto se procede a calcular el TF-IDF de la siguiente manera:
 ![Tech](/tf-idf.png)

 * K-Means: Es uno de los algoritmos de clustering más comúnmente utilizados que agrupa los puntos de datos en un número predefinido de clusters.

## 4. Referencias:
https://spark.apache.org/docs/
