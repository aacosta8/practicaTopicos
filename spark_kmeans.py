from __future__ import print_function

# expresiones regulares
import re

# tf-idf
from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF

# KMeans
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel


if __name__ == "__main__":
    # Creamos el contexto, con el nombre de la app
    sc = SparkContext(appName="Alexander_Julian")  # SparkContext

    # lista de todos los documentos, (Key = name, value= document content)
    documents = sc.wholeTextFiles("hdfs://.")
    # Lista de solo los names de los documents
    documents_names = documents.keys().collect()
    # Lista de listas con el contenido de los documentos
    documents_values = documents.values().map(lambda line: line.split(" "))

    # Contador de frecuencias de cada palabra, por cada documento
    hashingTF = HashingTF()
    tf = hashingTF.transform(documents_values)

    idf = IDF().fit(tf)
    # Multiplica los tf por los idf para dar el peso correspondiente de cada
    # termino para cada documento
    tfidf = idf.transform(tf)

    k = 2 #numero de clusters
    # calcular kmeans
    clusters_model = KMeans.train(tfidf, k, maxIterations=10)
    clusters = clusters_model.predict(tfidf).collect()

    # creamos una lista de listas para agrupar los documentos
    k_groups = [[] for i in range(k)]

    # Agregamos a cada grupo, los documentos que pertenecen a él.
    for i,cluster in enumerate(clusters):
        k_groups[cluster]+= re.findall('\/\w*$', documents_names[i])

    for j in ranke(k):
        print "---------------------------------------------------------------
        print "Cluster ",j
        print "---------------------------------------------------------------
        print k_groups[j]
        print "---------------------------------------------------------------"
    salida = sc.parellelize()
    salida.saveAsTextFile("hdfs:///user/jarangol/kmeans1")
    sc.stop()
