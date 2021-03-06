# Machine Learning and Big Data

Data is considered big data when it exceeds the capacity of operational databases. Working with datasets of this size creates unique challenges. How will we store all of this data? How can we access it quickly? How do we back up this type of data? A project dealing with big data outgrows Excel, SQL, and NoSQL databases. 

## Four V's of Big Data  
There are four characteristics of big data. The four Vs of big data will help you determine when to migrate from regular data to big data solutions.  
- Volume refers to the size of data (e.g., terabytes of product information). For instance, a year's worth of stock market transactions is a large amount of data.  
- Velocity pertains to how quickly data comes in (customers across the world purchasing every second). As an example, McDonald's restaurants are worldwide with customers buying food at a constant rate, so the data comes in fast.  
- Variety relates to different forms of data (e.g., user account information, product details, etc.). Consider the breadth of Netflix user information, videos, photos for thumbnails, and so forth.  
- Veracity concerns the uncertainty of data (e.g., reviews might not be real and could come from bots). As an example, Netflix would want to verify whether users are actively watching the shows, falling asleep, or just playing them in the background.

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

- Tokenization

Tokenization is the concept of splitting a document, or line of text, into smaller subsets of data that can be analyzed. It's the building block of most NLP uses. You can tokenize by paragraph, sentence, word, letter, etc.

Original Sentence: NLP has many uses!

Tokenized by word: ["NLP","has","many","uses","!"]

- Normalization

Normalization is the process of taking misspelled words and converting them into their correct form, or sometimes a simpler form. This is another building block of NLP as it helps convert the text to a readable form, and allows us to create NLP programs on top of it. There are numerous ways to approach normalization, we will focus on two.

```
**Stemming** removes the suffix from a word and reduces it to its original form. This serves as a “rough” cut off the end of the word. An example of stemming might be to     reduce “horses” to “horse” and “ponies” to “poni.” As seen here, the truncated form is not always a real word.

**Lemmatization** removes the suffix from a word and reduces it to its original form. Lemmatization tends to be a “smoother” cut off the end of the word. It tries to return  to the original root word. In contrast to stemming, lemmatization always returns a real word. For example, the word “am” might be lemmatized to “be.” While stemming is a blunt  instrument that follows abstract rules regardless of real world usage, lemmatization performs a similar process but reduces words to their root. Lemmatization accomplishes this  by using a lexicon (a specialized dictionary) of words and their variant forms.
```

- Part-of-Speech Tagging

Part-of-Speech, or PoS can be helpful for a veriety of different models in NLP. PoS tagging is the concept of finding each word's part of speech in a given document.

![image](https://user-images.githubusercontent.com/68082808/98901760-4ceed100-2482-11eb-902b-3f3f19523aea.png)

![image](https://user-images.githubusercontent.com/68082808/98897010-61c66700-2478-11eb-94a4-11dbe89b55c0.png)

Check the code out yourself! Source Code: [PoS](https://github.com/sfnxboy/Machine_Learning_and_Big_Data/blob/main/Part_of_Speech_Tagging.ipynb)

- Natural Language Generation

Natural Language Generation (NGL) is the processing task of generating natural language from a machine representation system such as a knowledge base. Popular examples include chatbots, automated custom reports, and custom webpage content. Most of the technology already exists to create meaningful content from natural language generation.

- Bag-of-Words

When we're building datasets for NLP, we need to consider how our program will interact with the text document we provide. If we create a bag-of-words (BoW) model (i.e., the most frequent words), we can build models from that. The basic idea behind this model is this: We have a document of words, but we don't care about the order of the words. We can count these words and create models based on how frequently they appear.

- n-gram

In NLP, there is an n-gram method, which is a sequence of items from a given text. With n-gram, you create groupings of items from the text of size 1 or more. The following n-grams are common:

Unigram is an n-gram of size 1.
Bigram is an n-gram of size 2.
Trigram is an n-gram of size 3.

For instance, a unigram for "I love programming" would be "I","love" and "programming". Its bigram would break up the sentence into sequential two-word chunks "I love", and "love programming", and the trigram would of course be "I love programming. Of course for longer sentences, we can always use larger groupings where n is a positive number. N-grams can be used for a variety of NLP tasks, but most involve text mining or extraction. You can also use n-grams for spellcheck and text summarization.

- Text Similarity

Another popular use case for NLP is determining document or sentence similarity. These are important use cases, because they can tell us a lot about a document and its contents. There are a number of ways to do text similarity, with varying levels of difficulty.

### Natural Language Processing Analyses

There are three types of NLP analyses:

-  analysis is essentially checking the dictionary definition of each element of a sentence or document. In this type of analysis, we don't care about the words that come before or after the word in question—we just care about the given word.
- Sentiment analysis pertains to what the text means. Is it positive, negative, or neutral? You can come up with a score of how positive or negative the text is using NLP.
- Semantic analysis entails extracting the meaning of the text. You want to analyze the meaning of each word, and then relate that to the meaning of the text as a whole.

Within NLP, named-entity recognition (NER) is the concept of taking a document and finding all of the important terms within it. An important term can mean anything, from a politicians name, to a verb, to a place. Many names are already recognized, but you can always add more names to the list of recognized entities, as necessary. You train a model on data labeled with important entities so that the model can better distinguish which entities should be labeled in a different dataset.

### Natural Language Processing Pipeline

1. Raw Text: Start with the raw data.
2. Tokenization: Separate the words from paragraphs, to sentences, to individual words.
3. Stop Words Filtering: Remove common words like "a" and "the" that add no real value to what we are looking to analyze.
4. Term Frequency-Inverse Document Frequency (TF-IDF): Statistically rank the words by importance compared to the rest of the words in the text. This is also when the words are converted from text to numbers.
5. Machine Learning: Put everything together and run through the machine learning model to produce an output.

### Term Frequency-Inverse Document Frequency Weight (TF-IDF)  
When assessing the value of the remaining text, the "value" of a word is determined by how often it appears in the text. For example, if when reading an article and you see the word "Python" several times, its safe to assume that this may be an important term. PySpark can apply TF-IDF, a statistical weight showing the importance of a word in a document. Term frequency (TF) measures the frequency of a word occurring in a document, and inverse document frequency (IDF) measures the significance of a word across a set of documents. Multiplying these two numbers would determine the TF-IDF. Consider the previous example of the technology article. If "Python" appears 20 times in a 1,000-word article, the TF weight would be 20 divided by 1,000 which equals 0.02. Assume that this article resides in a database with other articles, totaling 1,000,000 articles. IDF takes the number of documents that contain the word Python and compares to the total number of documents, then takes the logarithm of the results. For example, if Python is mentioned in 1000 articles and the total amount of articles in the database is 1,000,000, the IDF would be the log of the total number of articles divided by the number of articles that contain the word Python.  
```
IDF = log(total articles / articles that contain the word Python)
IDF = log(1,000,000 / 1000) = 3
```  
The product of our TF and IDF are as follows:  
```TF-IDF = TF * IDF = 0.2 * 3 = .6```  
Computers deal with numbers, not text, so for a computer to determine the TF-IDF, it needs to convert all the text to a numerical format. There are two possible ways to do so. The first is by CountVectorizer, which indexes the words across all the documents and returns a vector of word counts corresponding to the indexes. The indexes are assigned in descending order of frequency. For example, the word with the highest frequency across all documents will be given an index of 0, and the word with the lowest frequency will have an index equal to the number of words in the text. The second method is HashingTF, which converts words to numeric IDs. The same words are assigned the same IDs and then mapped to an index and counted, and a vector is returned. For our Python example, if it gets a numerical ID of 4278 and it appeared 20 times, the vector would be 4278 : 20.
