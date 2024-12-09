
FROM apache/airflow:2.10.3-python3.12

USER root
# Install required packages including procps
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
         default-jdk \
         gcc \
         python3-dev \
         procps \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable for default JDK
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH="$JAVA_HOME/bin:$PATH"

USER airflow
RUN pip install apache-airflow apache-airflow-providers-apache-spark pyspark
