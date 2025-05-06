# Microsoft Fabric Data Engineering Project  

## Overview  
This project demonstrates an **end-to-end data pipeline** using **Microsoft Fabric**. It covers **data ingestion, transformation, and visualization** with **OneLake, Power BI, and Spark Notebooks**.  

## Technologies Used  
✅ **Microsoft Fabric** (Trial)  
✅ **OneLake** – Cloud-based data lake storage  
✅ **Power BI** – Data visualization  
✅ **Spark Notebooks** – Data transformation using Python  
✅ **SQL** – Querying and processing data  
✅ **GitHub** – Version control  

## Project Workflow  
### **1. Data Ingestion**  
- Loaded a public healthcare dataset into **OneLake**.  
- Used **Dataflows** for ETL (Extract, Transform, Load) operations.  

### **2. Data Transformation**  
- Used **Spark Notebooks** to clean and filter data.  
- Converted raw records into structured datasets for visualization.  

### **3. Data Visualization**  
- Built a **Power BI report** to analyze healthcare trends.  
- Created interactive dashboards for decision-makers.  

## How to Run This Project  
1. **Sign up for Microsoft Fabric trial** [here](https://app.fabric.microsoft.com/home?experience=fabric-developer).  
2. **Clone this repository**:  
   ```sh
   git clone https://github.com/krice05/fabric-data-pipeline-earthquake.git

## Business Case

Earthquake data is incredibly valuable for understanding seismic events and mitigating risks. Government agencies, research institutions, and insurance companies rely on up-to-date information to plan emergency responses and assess risks. With this automated pipeline, we ensure these stakeholders get the latest data in a way that’s easy to understand and ready to use, saving time and improving decision-making.

### Solution Overview

We're going to use **Microsoft Fabric** to build an end-to-end earthquake data pipeline using the **medallion architecture**. This involves:

- **Bronze Layer**: Collect raw earthquake data.
- **Silver Layer**: Transform it into a clean, structured format.
- **Gold Layer**: Enrich it with calculated fields for analysis.
- **Power BI**: Visualise the data interactively.
- **Data Factory**: Automate the entire process, ensuring up-to-date information daily.

![image](https://github.com/user-attachments/assets/1d87bdea-2005-43f1-803f-9af21a22068a)

### Medallion Architecture in Action

Let’s break down each layer:

1. **Bronze Layer (Raw Data Ingestion)**
    - **What It Does**: This layer is for storing raw data, exactly as we receive it.
    - **How We Do It**: Fetch earthquake data from an external API using a Python script and store it as **JSON files** in the Fabric Lakehouse.
    - **Why It’s Important**: This keeps the original data safe for audit or if you ever need to trace issues back to their source.
2. **Silver Layer (Data Transformation)**
    - **What It Does**: This layer takes the raw data and cleans it up for use.
    - **How We Do It**: Convert the **JSON files** into **Delta tables**. Here, we clean and filter the data—adding structured columns like event time, magnitude, and location.
    - **Why It’s Important**: This creates a clean, easy-to-use version of the data, ready for most reporting needs.
3. **Gold Layer (Data Enrichment)**
    - **What It Does**: This layer prepares data for high-quality analysis.
    - **How We Do It**: Use the Silver Layer data to create more meaningful information, like **country codes** and **significance classifications**. The final output is saved as a **Delta table**.
    - **Why It’s Important**: This gives you an enriched dataset that’s optimised for analysis, providing ready-to-use insights.
4. **Power BI Visualisation**
    - **What It Does**: Visualises the data to make it understandable at a glance.
    - **How We Do It**: Load the **Gold Layer** data into Power BI to create an interactive dashboard. Here, you can see trends and patterns in earthquake occurrences, like the number of events by country or the severity over time.
    - **Why It’s Important**: Visualisation is crucial for communicating complex data simply—making insights accessible to everyone.
5. **Orchestration with Data Factory**
    - **What It Does**: Automates the entire pipeline so that it runs every day.
    - **How We Do It**: Use **Data Factory** to set up a daily schedule, automating data collection, transformation, and enrichment.
    - **Why It’s Important**: Automation means you don’t need to manually update the data—ensuring stakeholders always have up-to-date information.

![image](https://github.com/user-attachments/assets/795bb864-da01-428f-bd1b-d21cfe65390a)
