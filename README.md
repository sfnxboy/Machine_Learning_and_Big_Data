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


## Natural Language Processing

Natural language processing (NLP) is a growing field of study that combines linguistics and computer science for computers to understand written, spoken, and typed natural language. NLP is the process of converting normal language to a machine readable format, which allows a computer to analyze text as if it were numerical data. NLP may be used for:

- **Analyzing legal documents:** NLP can be used to analyze many types of legal documents. This can improve the outcome of a given case, as lawyers and staff can find critical information quickly.
- **U.S. Securities and Exchange Commission (SEC) filings:** NLP is used to analyze SEC filings for various businesses. Companies use NLP to analyze filings for real-time business intelligence.
- **Chatbots:** Chatbots are one of the most popular use cases. Chatbots can be used for selling products, customer support, and even medical help.

Due to the massive amounts of text data needed to drive insights, we'll have to learn how to manage that data. There are a number of important use cases to delve into:

- **Classifying text:** For many of the aforementioned use cases to work, a computer must know how to classify a given piece of text. Classification can mean a few different things in NLP. You can have classification of specific words, even specifying what the part of speech is. You can also classify what the text is as a whole.
- **Extracting information:** Many NLP tasks require the ability to retrieve specific pieces of information from a given document. Think of the case where we are extracting data from law documents. You might want to extract certain aspects of that document to present good cases.
- **Summarizing a document:** Summarization is a key aspect of NLP. It helps solve quite a few different problems. You can essentially create a model that summarizes a given document. This can be helpful to understand the high-level details of law documents, articles, and much more.

We need NLP so that computers can better analyze language and someday communicate seamlessly with humans. Despite significant advancements in NLP, computers still struggle to understand the whole context of a text. For now, they just understand definitions and the literal meaning of a text. They don't understand sarcasm or subtext or anything not explicitly defined or expressed.

Natural language processing can get tricky. When individuals converse, they may not always say what they intend to. Sarcasm is a great example. Say you are watching a game with a friend, and they ask you how your team is doing. You responding with "oh just fantastic," although you're incredibly frustrated because your favorite team is losing. On text, without detecting sarcasm, you are giving the impression that you are impressed by your teams performance. Another example is tone. Your coworker asks you for a favor, you can then respond with "Great, I'll get right on it" or Great! I'll get right on it!". The former line has a bland, tired voice behind it, whereas the second line definetly sounds more excited! Same text, different tones. These are just two examples of the complexity of dealing with natural language. 

### NLP Core Concepts

- __**Tokenization**__

**Tokenization** is the concept of splitting a document, or line of text, into smaller subsets of data that can be analyzed. It's the building block of most NLP uses. You can tokenize by paragraph, sentence, word, letter, etc.

**Original Sentence:** NLP has many uses!

**Tokenized by word:** ["NLP","has","many","uses","!"]

- **Normalization**

**Normalization** is the process of taking misspelled words and converting them into their correct form, or sometimes a simpler form. This is another building block of NLP as it helps convert the text to a readable form, and allows us to create NLP programs on top of it. There are numerous ways to approach normalization, we will focus on two.

  - **Stemming** removes the suffix from a word and reduces it to its original form. This serves as a “rough” cut off the end of the word. An example of stemming might be to     reduce “horses” to “horse” and “ponies” to “poni.” As seen here, the truncated form is not always a real word.

  - **Lemmatization** removes the suffix from a word and reduces it to its original form. Lemmatization tends to be a “smoother” cut off the end of the word. It tries to return  to the original root word. In contrast to stemming, lemmatization always returns a real word. For example, the word “am” might be lemmatized to “be.” While stemming is a blunt  instrument that follows abstract rules regardless of real world usage, lemmatization performs a similar process but reduces words to their root. Lemmatization accomplishes this  by using a lexicon (a specialized dictionary) of words and their variant forms.
