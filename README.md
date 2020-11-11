# Machine Learning and Big Data

Data is considered big data when it exceeds the capacity of operational databases. Working with datasets of this size creates unique challenges. How will we store all of this data? How can we access it quickly? How do we back up this type of data? A project dealing with big data outgrows Excel, SQL, and NoSQL databases. 

## Hadoop

Apache Hadoop (Hadoop) is one of the most popular open source frameworks, with numerous technologies for big data. Google developed Hadoop to process large amounts of data by splitting data across a distributed file system. Dealing with big data can be quite taxing on computer hardware. So with the power of connected computers that work together and perform tasks, Hadoop can store and process data.

Hadoop has three main components:
1. Hadoop Distributed File System (HDFS) is a file system used to store data across server clusters (groups of computers). It is scalable (which means it handles influxes of data), fault-tolerant (handles hardware failure), and distributed (spread across multiple servers connected by a common core).
2. MapReduce is a programming model and processing technique for big data. MapReduce enables processing the large amount of data spread across the cluster in the HDFS by performing the same task for each file system.
3. Yet Another Resource Negotiator (YARN) manages and allocates resources across the clusters and assigns tasks.

### Map Reduce Process
A common tool to split datasets is Hadoop's MapReduce technique. It is used as a means to distribute and process data across your cluster (a collection of synced computers working in tandem.) This reduces the time it takes to analyze the data. During the mapping stage the map function, which is the function applied to each computer, takes a small piece of the input and then converts the data into key-value pairs, with key identifiers and associated values. Reducing is when you aggregate the results, in this case, by adding up the figures, giving each key some aggregated weight.

For example, say you wanted to run a word count on a document. The following image shows the MapReduce process for running word count on an input:

![image](https://user-images.githubusercontent.com/68082808/98761685-fb701480-23a3-11eb-965f-5bbe898822f1.png)

- **Input:** The entire file is fed to the word counter.
- **Splitting:** Each line of text is separated.
- **Mapping:** Each word in every line is assigned a value of 1.
- **Shuffling:** The words are combined and organized alphabetically, creating a list of the words' values.
- **Reducing:** The list of values are summed for each word.
- **Final Result:** The complete list of words and value (counts) are displayed.

The [MrJob](https://github.com/sfnxboy/Machine_Learning_and_Big_Data/tree/main/MrJob) folder in this repository contains code that executes the map reduce process via python script. You might have noticed that nowhere in the code is a file imported or opened. The mrjob library works by reading in a file passed to it in the terminal.

## Spark

Although Hadoop does the job of wrangling big data, it takes significant time configuring multiple servers on a computer. New technologies allow more flexibility in data processing. One of these technologies is **Spark**. Apache Spark (Spark) is a unified analytics engine for large-scale data processing. Spark lets you write applications in code that can run on Hadoop. However, Spark doesn't have to run on Hadoop, as it can run in stand-alone mode or in the cloud. Spark can be 100 times faster than Hadoop. This is because where Hadoop communicates with HDFS per computation, Spark uses in-memory computation and can retain as much as HDFS can in-memory.  Just like Hadoop's MapReduce, Spark works with data spread across a cluster, or a group of computers that work together.

The Spark architecture includes the driver, executors, and the cluster manager:

- The driver is the heart of the application. It is responsible for maintaining the application information; responding to the code or input; and analyzing, distributing, and scheduling work to the executors.
- The executors perform the code assigned by the driver and then report the state of the computation to the driver.
- The cluster manager controls the driver and executors and allocates resources to the machines on the Spark applications. The cluster manager is an external service for acquiring resources on the cluster. Spark can either use it's own standalone cluster manager that comes standard with Spark or another application (e.g., Apache Mesos, Hadoop YARN).

Spark is very accessible through different programming languages. Spark was written in Scala, a tough programming language. However, there is an API that works with many languages to translate the code into Spark code and execute. Spark has an API in Java, Python, SQL, and R. In this project we will be using Python's flavor of spark, PySpark.

### PySpark in Google Colab Notebooks

Before we can begin using Spark, we need a place to do so. Cloud-based notebooks provide a remote workspace with stronger resources than our local laptop might allow. Cloud notebooks permit us to share our work with others, such as coworkers, similar to GitHub. [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb) is a google-hosted notebook. 

Just like we do with our local environment, we need to install packages for libraries we want to use. PySpark does not come native to Google Colab and needs to be installed. Paste the following code into the cell of your Google Colab file: [PySpark install code](https://github.com/sfnxboy/Machine_Learning_and_Big_Data/blob/main/PySpark_install_GC.txt)

Create a Spark session by importing the library and setting the spark variable to the code below:
```
# Start Spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("DataFrameBasics").getOrCreate()
```

Working in Spark requires us to put data into DataFrames. If you're wondering if these DataFrames are comparable to those in Pandas, you're correct—Spark DataFrames are very similar. The schema, or structure, for DataFrames and datasets contains the column names and the data types contained within. Schema can be read when the data is loaded or manually defined.

Check out the following notebook file to see examples of dataset manipulation via PySpark: [PySpark_Demo1](https://github.com/sfnxboy/Machine_Learning_and_Big_Data/blob/main/PySpark_Demo1.ipynb)

