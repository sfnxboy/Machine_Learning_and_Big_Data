# Machine Learning and Big Data

Data is considered big data when it exceeds the capacity of operational databases. Working with datasets of this size creates unique challenges. How will we store all of this data? How can we access it quickly? How do we back up this type of data? A project dealing with big data outgrows Excel, SQL, and NoSQL databases. Apache Hadoop (Hadoop) is one of the most popular open source frameworks, with numerous technologies for big data. Google developed Hadoop to process large amounts of data by splitting data across a distributed file system. Dealing with big data can be quite taxing on computer hardware. So with the power of connected computers that work together and perform tasks, Hadoop can store and process data.

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
