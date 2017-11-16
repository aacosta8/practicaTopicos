from __future__ import print_function

# tf-idf
from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF, IDF

# KMeans
from numpy import array
from math import sqrt
from pyspark.mllib.clustering import KMeans, KMeansModel

if __name__ == "__main__":
    sc = SparkContext(appName="Alexander_Julian")  # SparkContext

    documents = sc.wholeTextFiles("hdfs://...")
    documents_values = documents.values().map(lambda line: line.split(" "))

    hashingTF = HashingTF()
    tf = hashingTF.transform(documents_values)

    idf = IDF().fit(tf)
    tfidf = idf.transform(tf)

    clusters_model = KMeans.train(tfidf, 2, maxIterations=10)
    clusters = clusters_model.predict(tfidf).collect()

    print("clusters:")
    print clusters
    for each in clusters:
        print(each)
sc.stop()
