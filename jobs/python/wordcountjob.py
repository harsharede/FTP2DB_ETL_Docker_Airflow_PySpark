import os
from ftplib import FTP
from pyspark.sql import SparkSession
from pyspark import SparkFiles
import tempfile

ftp_host = "sparkingflow-ftp-server-1"
ftp_user = "alpineftp"
ftp_pass = "alpineftp"
remote_path = "/home/ftpusers/data/test1234.csv"

# Create a temporary directory
temp_dir = '/home/shared/data'
file_name = "test1234.csv"
local_file_path = os.path.join(temp_dir, file_name)


spark = SparkSession.builder.config("fs.ftp.impl", "org.apache.hadoop.fs.ftp.FTPFileSystem").appName("CSVReadExample").getOrCreate()

try:
    print('££££££££££££££££££££££££££££££££££ spark.read.format("csv").option("header", "true").load(local_file_path)')
    df = spark.read.format("csv").option("header", "true").option("delimiter", ";").load(local_file_path)
    df.show()
    print(df)
    df.createOrReplaceTempView('sql_view')
    spark.sql("SELECT * FROM sql_view where Location ='London'").show()
    print('££££££££££££££££££££££££££££££££££')
except Exception as e:
    print('failed  df = spark.read.format("csv").option("header", "true").load(local_file_path)')
    print(e)

spark.stop()
