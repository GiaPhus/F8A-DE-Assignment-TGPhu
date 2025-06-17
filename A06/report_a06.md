---
title: report_a06_rapid_analytics_solution
---
---
## Summary
- Design a **temporary analytics solution** to deliver fast and actionable business insights while the complete data infrastructure is still under construction
- Prioritize **speed of deployment** over architectural perfection to address urgent analytics needs from business teams
- Implement **data ingestion using Data Fusion**, allowing low-code pipelines to rapidly integrate batch and streaming sources
- Store and analyze data in **BigQuery**, leveraging its scalability, SQL support, and integration with visualization tools
- Provide **business dashboards via Looker Studio**, enabling teams to interact with live data through an intuitive interface
---

### Key Terms for Understanding the Overall System
<details open>
<summary>Plain-language explanations of technologies and components used in this solution</summary>
---
- **Data Fusion**
  - A Google Cloud tool that helps connect and move data from many sources using a simple drag-and-drop interface  
  - Allows building data pipelines **without much coding**  

- **Pub/Sub**  
  - A service for receiving real-time data (e.g. from websites, apps, or IoT devices)  
  - Works like a messaging system: some sources **publish** data, and others **subscribe** to process it  

- **Dataflow**  
  - A service that processes and transforms data, especially streaming data  
  - Ensures the right format and structure before storing in the data warehouse  

- **BigQuery**  
  - A fully-managed cloud database used for analyzing large datasets using SQL  
  - Stores both temporary and long-term business data  

- **GCS (Google Cloud Storage)**  
  - A place to store **raw files**, like CSVs or JSON, similar to Google Drive but for systems  

- **Looker Studio**  
  - A web-based tool for creating **interactive dashboards** from BigQuery and other sources  
  - Business users can view charts, KPIs, and trends without needing to write SQL  

- **Dashboard**  
  - A visual report with charts and tables that summarize key business information  
  - Helps teams make decisions based on current data  
---
</details>

---
## System Architecture
---

### Data Sources
<details open>
<summary>Overview of batch and streaming data origins</summary>
---
- **Batch sources** such as exported CSV files from internal tools, CRM systems, or external vendors.
- **Streaming sources** like real-time application logs, user activity data, or IoT device events.
---
</details>

### Ingestion Layer
<details open>
<summary>Batch and streaming pipelines using Data Fusion and Pub/Sub</summary>
---
#### Batch Ingestion – via Data Fusion
- Google Cloud **Data Fusion** is used to create visual ETL pipelines that ingest batch files from various sources.
- These files are stored temporarily or long-term in **Google Cloud Storage (GCS)**.
- Data Fusion handles format conversions, schema mapping, and basic cleaning.

---
#### Streaming Ingestion – via Pub/Sub + Dataflow
- Streaming data (e.g. app events) is pushed into **Google Cloud Pub/Sub**.
- A **Dataflow** pipeline subscribes to these topics and processes data in real-time.
- Data is cleaned, parsed, and loaded directly into **BigQuery** or staged via GCS.
---
</details>

### Storage and Analytics Layer
<details open>
<summary>BigQuery as the central warehouse for batch and streaming</summary>
---
- The core data warehouse is **BigQuery**, where both batch and streaming data converge.

#### For batch data:
- GCS is mounted as an **external table** in BigQuery.
- This allows querying without duplicating storage and supports schema changes easily.

---
#### For streaming data:
- Dataflow loads data directly into BigQuery managed tables with append-only strategy.
---
</details>

### Visualization Layer
<details open>
<summary>Dashboards in Looker Studio using live BigQuery data</summary>
---
- **Looker Studio** connects directly to BigQuery to build interactive dashboards.
- Business users can filter views, track KPIs, monitor trends, and create custom charts without needing SQL knowledge.
- Dashboards are updated in near-real-time depending on streaming latency and refresh policies.
---
</details>

### Flexibility & Change Accommodation
<details open>
<summary>System flexibility and long-term integration potential</summary>
---
- Using **external tables** from GCS ensures flexibility in case schemas evolve.
- **Looker dashboards** are easy to reconfigure, enabling business teams to adjust to changing needs quickly.
- The whole system is modular, so each component (ingestion, storage, visualization) can be replaced or upgraded individually.
---
</details>
