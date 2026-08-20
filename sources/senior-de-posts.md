# Senior Data Engineer Posts
From newest to oldest

---

In the previous post we talked about some of the dimensions of data quality, and in this post we will look at one of my favorite tools for measuring data quality dimensions: GreatExpectations.

GreatExpectations is one of the tools and technologies used for measuring and testing data quality. The Rules applied to data fields at the Dataset/Table level can be filled into a file in JSON or YAML format, and the code can be built using the great_expectations library in Python.

For example, as in the attached images:

Let's assume Company X processes medical claims for a number of healthcare providers, submitting invoices for the health services provided to patients, and this company — or the entity that monitors these claims — wants to measure its data quality using the 6 well-known dimensions. First, the rules applied to the data fields are gathered from the concerned and responsible departments, then the technical team converts them into a JSON file, and Python is used to Scan the Rules against the Table in the database (for example PostgreSQL). The results then appear as a Score for each Data Quality Dimension for each column or data field, as shown in the images.

What distinguishes this tool is that it is open source and is used by many organizations for the purpose of measuring data quality. It has also proven its effectiveness for us, as it was used in the center at the Databases level, and it can also be automated — we automated the GreatExpectations Jobs via Apache Airflow and then created a dashboard to monitor data quality periodically.

---

Among the data quality dimensions, there are dimensions that are measured in an automated and direct way, such as Completeness and Uniqueness.

We will focus more on a very important dimension, which is Validity, which simply means: do the field values comply with the rules set in advance?

Here we refer to Business Rules that are collected and documented together with the business teams and the departments related to the nature of the data.

Examples of rule categories in real estate data:

Data Type: the price is a decimal number, not text.
Format: the mobile number starts with 05 and contains 10 digits.
Range: the property area is between 20 and 5,000 meters, and the price is greater than zero.
Domain: the district is within an approved list of districts, and the property type is within (villa, apartment, floor, land).
Cross field: price per meter = price ÷ area, and the listing date is not in the future.

Here the intent may be clear to some, but some people may confuse Accuracy with Validity, and in reality there is a fundamental difference between them. For example:

A listing for a 450 m villa in Al-Narjis district at a price of 2,750,000 riyals may comply with the rules set in advance, but this does not mean that the villa actually exists. Validity is measured against the rules, while Accuracy is measured against reality.

Summary:

Validity is one of the easiest data quality dimensions to apply — with alignment with the business teams while collecting the rules — and the highest in return in terms of positive impact on the organization in making sound decisions.

In the next post, God willing, we will apply this practically using one of my favorite open source technologies, with a realistic scenario for collecting business rules on data fields, measuring data quality dimensions, and automating them.

---

In Apache Spark, one of the most common problems that affect performance is what is known as data skew.

It is a situation that occurs when some values are repeated much more than others, which leads to an unbalanced distribution and partitioning of the data. This makes some tasks process huge amounts of data while others remain almost empty, causing slowness in executing the tasks and operations.

One of the solutions: broadcast join.
It is one of the special types of Join and a technique for improving performance in Spark, where the small table is copied to all the Nodes in the Cluster instead of shuffling the large table. This reduces the impact of data skew and improves performance noticeably, without needing to use other types of Join that are very expensive to execute.

In the example below there is Python code using the PySpark library, with data generated at large volumes that simulates real data. Executing the code took seconds, and the reason is the efficiency of using broadcast join to solve this problem.

---

As a data engineer, I deal daily with all kinds of data, and through direct contact with the challenges of data integration, cleansing, and unification across multiple systems and disparate sources, I have distilled a set of fundamental lessons that have proven their deep impact on the success of organizations, the most important of which are:

1- Clear governance is the cornerstone.

Having a governance framework that defines the roles (data owner, quality officer, user), the policies, and the responsibilities is what turns data quality from scattered individual efforts into a sustainable institutional system.

The impact: faster decisions, clear accountability, and more efficient investment in data.

2- Quality starts at the source.

Correcting data after it has been entered costs the organization and the team working on it. Automation is a healthy step, but quality is the responsibility of the source.

The impact: lower operational costs, fewer errors, and higher reliability of reports.

3- What is not measured cannot be improved!

Adopting clear indicators to measure the quality dimensions (accuracy, completeness, consistency, timeliness) and publishing periodic reports turns quality from a slogan into performance that can be tracked and improved.

The impact: continuous and objective improvement instead of unorganized efforts.

4- Data quality is an organizational culture, not a technical task!

The success of any data quality initiative depends on all employees realizing that data is an organizational asset and that its quality is everyone's responsibility.

The impact: higher commitment, less resistance to change, and sustainability of the initiatives over the long term.

5- Linking quality to decisions.

When data quality is linked to performance indicators and funding, it turns from a secondary activity into an organizational priority that everyone commits to.

The impact: more precise decisions, greater trust in data, and a tangible return on data initiatives.

Summary:

Data quality is an organizational duty for making correct decisions 👍🏼

---

Excited to share that I've earned the chDB Professional badge from ClickHouse!

chDB is an in-process SQL OLAP engine powered by ClickHouse, think of it as "ClickHouse without the server." It lets you run blazing-fast analytical queries directly inside your Python, Go, Rust, or Node.js applications, with zero infrastructure to manage.
The goal: bring ClickHouse's industry-leading speed on massive datasets straight into your code, perfect for embedded analytics, data science notebooks, ETL pipelines, and serverless workloads.
Big thanks to the ClickHouse team for building such a powerful tool and offering this learning path. Onward to more data adventures! 🚀

---

The Medallion Architecture methodology is known as a framework for designing and processing data in data lakes, aiming to improve data quality gradually through successive stages.

It consists of three main layers:

- The Bronze Layer for raw data
- The Silver Layer for data that has been cleaned and restructured
- The Gold Layer for data that is ready for analysis purposes
In the images there is an example that was applied on the Databricks environment within my project to build the Riyadh Data Lakehouse, which includes all the services, facilities, and activities related to Riyadh. I dedicated the example to building a Data Pipeline for hotel bookings; the data was pulled from the TripAdvisor and Booking applications, then refined, and a Dataset was built as a report to track hotel performance. The processing is done via Apache Spark, and the data is stored in Managed Tables and Delta Tables on a monthly and automated basis.

I also attached a sample of the hotel booking data for May 2026 on my account on the Kaggle platform in Parquet format.

---

I'm excited to share that I've officially passed the Databricks Certified Data Engineer exam.

This certification wasn't easy, it truly tests your understanding of end-to-end data engineering concepts within the Databricks ecosystem. I'd highly recommend having at least 6 months of hands-on experience working in a Databricks environment before attempting the exam to gain real-world exposure to the platform.

During my preparation and practical experience, I deepened my skills across key areas such as Apache Spark fundamentals and performance tuning, Delta Lake architecture and ACID transactions, ETL pipeline design, data ingestion and transformation, workflow orchestration using Databricks jobs, Databricks SQL for analytics and queries, data governance, schema enforcement, and quality checks.

This certification validates not just theoretical knowledge, but the ability to design and implement efficient, scalable, and reliable data pipelines in production.

---

As a data engineer, I see dbt as the most powerful tool in the Transform stage within the ELT methodology.

Through dbt, it has become possible to transform raw tables into organized models, and it has become easier since it is built with SQL Queries, with full tracking of the data path (Data Pipelines).

A practical example:

I built a Data Warehouse for healthcare data that contains data on patient visits and the services provided during the visit, such as examinations and medication prescriptions. I created a structure based on a staging layer followed by Facts and Dims tables, on dummy data that simulates real data, for the purpose of highlighting the power of dbt in the Transformations stage.

This tool can be used to automate this stage and schedule it via Apache Airflow, and it also supports many database systems such as PostgreSQL, Snowflake, and others.

---

As a data engineer, in many projects I face the challenge that the API interface of the target system is still under development, while we need to start building and testing the ETL to simulate the data extraction process using the same Data Elements.

In this case, using FastAPI is a very effective option, because it allows creating REST APIs quickly and efficiently, which enables us to build an interface that simulates the real API with the same structure and required data, to facilitate testing the extraction and processing operation early and smoothly.

Example:

Let's assume we have a project to build an insurance claims processing system, and one of the requirements is to pull the data and process or store it according to the needs of the data and business intelligence department for preparing reports. The agreement was to prepare an API with certain elements, but it needs time. In this case, the data engineer can start building a Data Pipeline that simulates the process of pulling the data from the API with the same procedure, using dummy data that simulates real data and covers all possible scenarios according to the requirements set in advance. In the images there is a practical example in Python that simulates the idea, where there is code that builds the API and other code that tests the API, with the result in JSON Data format.

Many technologies such as Airflow and others can be used for automation.

---

In a world where data is accelerating and becoming more complex, building an effective analytical system becomes a real challenge that requires a balance between speed, structure, and organization.
ClickHouse provided the solution on the speed side, as it is a columnar database that relies on the MergeTree engine, which sorts, indexes, and merges data intelligently, allowing queries to be executed in fractions of a second even with billions of rows.
Meanwhile, dbt came to add a layer of structure and flexibility in building and transforming SQL-LIKE Queries into organized models that are testable, documented, and versioned, and it supports many databases. Airflow took care of the organization side, as it automates the operations and tasks in an organized manner.
To simulate the idea, I present to you an ELT Pipelines project that combines these technologies, with the generation of dummy data resembling medical claims data, and building a Star Schema using dbt.
ClickHouse succeeded in handling millions of rows with amazing speed, while dbt organized all the transformation stages clearly, and Airflow managed the automation of the tasks with complete flexibility.

---

In Apache Spark, the Lazy Evaluation model plays an important role in improving the data processing workflow. Instead of executing any of the Transformations operations immediately, it builds a Logical Plan to record and save the operations that must be executed, and their execution is deferred until an "Action" is taken, upon which it executes the previously recorded operations. That is why using Spark is considered effective when dealing with large-volume data.

In the example below:

I performed operations on a Dataframe for movies containing the details of all the movies, and the images show the operations for querying the movies followed by a show() action to execute the previously stored operations.

---

How do you query millions of rows in partitioned Parquet files using DuckDB without needing Spark?

Before we start the explanation, let's give you a simple definition of Parquet.

What is a Parquet file?

It is a columnar and compressed file format used to store data at large volumes and analyze it with very high speed and efficiency.

What do we mean by columnar storage?
It means that it stores the data as separate columns, which speeds up the reading process.

What do we mean by a compressed file?
It reduces the size of the data and saves storage space, so you can store a Dataset with millions of rows, but using Parquet it will reduce the storage space significantly.

It is used in Python, Spark, Hive, and other technologies.

Example:

If we have a folder containing 3 Parquet files, each one containing a Dataset with 10 million rows, and we want to read them into a Dataframe — and because pandas does not support reading Parquet files directly, we use PyArrow to help us read quickly — you will notice in code image number 1 that it took seconds to read and store 30 million rows in a Dataframe!

Okay, so what is the concept of Partitioning here and how does it help us?

Partitioning, in short, is dividing the Dataset into small parts, or we could call them Sub Datasets, so that they are arranged as folders for you and contain the divided data.

Notice with me in this example in image number 2: we performed the Partitions operation on the Dataframe we have and divided it in the form of hierarchy folders as shown in the image, and we used DuckDB, which is a database that works with high efficiency on memory. Our goal was to build a query on the Partitioned files, telling it we want the data where the year is 2024 and the month is 6. In this case, the data retrieval operation is fast: it skips all the Partitions that do not apply to the condition we set, and goes to the 2024 folder, and to the folder inside it for month 6, and retrieves the data from it.

One last note:

The data is not real; it was generated using the Faker library in Python for the purpose of explaining the idea only 😁

---

The best formats for storing data in Python?

It is commonly known among many data scientists/analysts/engineers that the most common format is CSV for storing data, given its simplicity, ease of exchange, and widespread use. However, there are data formats that greatly outperform it in terms of storage and performance.

Therefore, I ran a comparison on data containing 10 million rows, and I limited the experiment to three data formats which are considered the best and most efficient, and they are:

- Pickle format
- Parquet format
- Feather format
Details of the experiment:

- Random data was generated: 10 million rows with various columns (numbers, text…) using the Faker library
- Time taken to generate the data: 124.21 seconds
The results:

Pickle format:

Writing: 11.53 seconds
Reading: 5.04 seconds
File size: 1010.16 megabytes
Notes: relatively fast but its size is large

Parquet format:

Writing: 19.48 seconds
Reading: 13.24 seconds
File size: 340.50 megabytes
Notes: slower but distinguished by its small file size

Feather format:

Writing: 9.40 seconds
Reading: 11.41 seconds
File size: 702.78 megabytes
Notes: the fastest in writing but slightly slower in reading

We conclude that the Pickle format is optimal for fast storage inside Python despite its large size, while Parquet is distinguished by its small file size and its suitability for long-term storage, and it is suitable with tools and technologies such as Dask and PySpark, whereas Feather offers fast performance in writing with medium-speed reading.

---

One of the reasons that makes me like using Polars over Pandas in Single Machine Computation is the speed in reading compared to Pandas. The reason is that it is built on the Rust language, meaning it is fast in execution like C/C++ languages, and also the biggest reason is that it uses something called PyArrow.

What is PyArrow?

It is simply an in memory columnar data format that allows you to read the data and store it faster in a Dataframe, such that it reads column by column and stores in an Arrow Array.

Unlike Pandas, whose very method of reading and storing data is via NumPy Arrays.

---
