# 🏅 End-to-End Olympic Data Analytics Pipeline on Azure

This project demonstrates a complete, end-to-end data engineering pipeline built on the Microsoft Azure platform. It ingests, processes, stores, and serves historical Olympic data for analytics, mimicking a real-world enterprise data workflow.

This repository contains all the necessary code, scripts, and notebooks to replicate the project, from raw data ingestion to a clean, queryable data warehouse.

## 🏛️ Project Architecture

The pipeline follows a modern data architecture, leveraging several key Azure services to create a scalable and robust system.

The data flows through the following stages:

1.  **Ingestion:** **Azure Data Factory (ADF)** is used to orchestrate the pipeline. It pulls the raw Olympic data (e.g., from APIs or flat files) and lands it in our data lake.
2.  **Storage (Raw):** The raw, unprocessed data is stored in **Azure Data Lake Storage (ADLS) Gen2** in a `bronze` layer.
3.  **Transformation:** **Azure Databricks** reads the raw data from the `bronze` layer. Using PySpark notebooks, it cleans, transforms, aggregates, and enriches the data. The processed data is then written back to ADLS in `silver` (cleaned) and `gold` (aggregated) layers.
4.  **Serving:** The final, aggregated `gold` data is loaded into **Azure Synapse Analytics** (formerly SQL Data Warehouse). This high-performance analytics service serves the data to end-users for BI dashboards (like Power BI) or ad-hoc SQL queries.

### Visual Flow

`[Raw Data] -> ADF Pipeline -> ADLS Gen2 (Bronze) -> Databricks Notebook (Clean/Transform) -> ADLS Gen2 (Silver/Gold) -> ADF (Copy) -> Synapse Analytics -> [Power BI / SQL Queries]`

---

## 🛠️ Technology Stack

This project uses the following Azure services:

* **Orchestration:** Azure Data Factory (ADF)
* **Storage:** Azure Data Lake Storage (ADLS) Gen2
* **Transformation:** Azure Databricks (using PySpark)
* **Data Warehouse:** Azure Synapse Analytics

---

## 📁 Repository Structure
. ├── /data/ # Sample raw data files (if applicable) ├── /notebooks/ # Databricks notebooks (.py or .dbc) for transformation ├── /adf/ # ADF pipeline definitions (ARM templates or JSON) ├── /sql-scripts/ # SQL scripts for Synapse (table creation, etc.) └── README.md # This file

---

## 🚀 How to Run This Project

To set up and run this pipeline, you will need an active Azure subscription.

### 1. Prerequisites
* An **Azure Account** with subscription.
* Permissions to create and manage the following resources:
    * Resource Group
    * Azure Data Factory
    * Azure Data Lake Storage Gen2
    * Azure Databricks
    * Azure Synapse Analytics

### 2. Setup Azure Services
1.  **Provision Resources:** Create a new Resource Group and provision the four services listed above.
2.  **Configure Storage (ADLS):** Create containers in your ADLS account (e.g., `bronze`, `silver`, `gold`) to store the data at different stages.
3.  **Set up Databricks:** Create a Databricks workspace and a cluster. Import the notebooks from the `/notebooks` directory.
4.  **Set up Synapse:** Create a Synapse workspace and a dedicated SQL pool to act as your data warehouse.

### 3. Pipeline Execution
1.  **Configure ADF Linked Services:** In Azure Data Factory, create Linked Services to connect to your ADLS, Databricks, and Synapse instances.
2.  **Deploy ADF Pipelines:** Import the pipeline JSON or ARM templates from the `/adf` directory into your ADF workspace.
3.  **Run SQL Scripts:** Execute the scripts in `/sql-scripts` within your Synapse SQL Pool to create the final tables that will hold the `gold` data.
4.  **Trigger the Pipeline:** Run the main ADF pipeline. This will trigger the end-to-end flow:
    * Ingest raw data to `bronze`.
    * Execute the Databricks notebook to transform data and save it to `silver`/`gold`.
    * Copy the final `gold` data from ADLS into your Synapse Analytics tables.

### 4. Analyze the Data
Once the pipeline completes, you can connect a BI tool like Power BI to your Synapse Analytics workspace or query the tables directly using SQL to explore the Olympic data.