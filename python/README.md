https://sparkbyexamples.com/pyspark/how-to-install-and-run-pyspark-on-windows

# Java

install java 8 from https://www.oracle.com/java/technologies/downloads/#java8

set JAVA_HOME=C:\Program Files\Java\jre1.8.0_333

# Spark

download spark from https://spark.apache.org/downloads.html

extract the downloaded file spark-3.0.3-bin-hadoop2.7.tgz and move the folder spark-3.0.3-bin-hadoop2.7 to C:\spark

*DO NOT DOWNLOAD THE LATEST VERSION, IT IS BROKEN, DOWNLOAD THE VERSION 3.0 WITH HADOOP 2.7*

set SPARK_HOME=C:\spark

set HADOOP_HOME=C:\spark

# Winutils

download winutil for hadoop 2.8 from https://github.com/steveloughran/winutils and extract it to C:\spark\bin

# Other configurations

```
pip install pyspark findspark
```

Always insert:
```py
import findspark
findspark.init()
```
before importing pyspark.