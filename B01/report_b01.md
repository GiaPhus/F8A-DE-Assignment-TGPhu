---
title: report_b01
---

---
## Overview

---

### Task Purpose and Goals

<details - open>  
<summary>Purpose and goals of the B01 Vector Database Tutorial task</summary>  
---

- This report is developed as part of **Task B01 - Vector Database Tutorial**.
- The main goal is to create a clear, practical, and self-contained guide to **vector database technologies**.
- The report is intended for both **self-study** and **team knowledge sharing**, making the content accessible across technical and non-technical roles.
- The tutorial supports cross-functional understanding, targeting data engineers, analysts, and product teams.

#### Report Objectives

- Introduce **key concepts**, **definitions**, and **real-world use cases** of vector databases.
- Compare major tools in the current **vector database ecosystem**.
- Conduct a **deep dive** into one selected tool with architectural and implementation insights.
- Provide **practical implementation guidance** using hands-on examples.
- Summarize **best practices** for performance tuning, scalability, and deployment.

#### Style and Approach

- Written in a **simple, direct, and plain language** style.
- Content includes **diagrams**, **code samples**, and **GenAI prompt workflows** where applicable.
- The final product is designed to serve as both:
  - A **learning resource** for individuals, and
  - A **reference document** for onboarding and collaboration within teams.

---
</details>



## Terminology

- Before diving into Vector Databases, it is important to understand several related concepts that surround and support them.

### Vector

<details - open>  
<summary>A vector is a numerical representation of data in high-dimensional space</summary>  
---

- A **vector** is a list of numerical values, usually floats, representing an object (e.g., sentence, image, audio) in a multi-dimensional space.  
- Vectors are the core representation used in **semantic similarity**, enabling comparison between unstructured data.  
- The **distance** or **angle** between vectors determines how similar the data objects are.  
- Vector databases operate by storing and searching for these high-dimensional vectors.

---
</details>

### Embedding
<details - open>  
<summary>A vector is a numerical representation of unstructured information (such as text, images, audio) in a high-dimensional space </summary>  

- **Embedding** is the process of converting raw data (e.g., text, image, audio) into numerical vectors.  
- It allows machines to **capture the semantic meaning** of the input using pre-trained or fine-tuned machine learning models.  
- For example, the sentences “I like tea” and “I enjoy hot drinks” will have similar embeddings, reflecting their semantic similarity.  
- If we want to **understand relationships between images, text, or audio**, we must first **digitize** these data types into a common format — embedding enables this transformation.  
- Embeddings are essential for tasks such as **semantic search**, **recommendation systems**, **multi-modal AI**, and **retrieval-augmented generation (RAG)**.

![Embedding Images](diagrams/Embedding.png)


---
</details>

### Vector Embedding

<details - open>  
<summary>Vector embedding is the process of encoding unstructured data into numerical vectors</summary>  
---

- **Vector embedding** combines the idea of “vector” and “embedding” — it refers to the **resulting vector** produced after embedding data.  
- It is the actual **numerical representation** of unstructured data like text, image, or audio.  
- These vectors are used in **semantic search**, **similarity matching**, and **machine learning models**.  
- Vector embeddings preserve the **semantic structure** of the input data in a way that machines can compute on.  
- Example: "dog" and "puppy" will have vector embeddings that are close together in vector space.

![Vector Embedding Images](diagrams/VectorEmbedding.png)

---
</details>

### ANN (Approximate Nearest Neighbor)

<details - open>  
<summary>ANN enables fast similarity search by approximating the closest vectors</summary>  
---

- **ANN** is an algorithmic approach for finding vectors that are **similar** (nearest) to a given input vector.  
- It **trades accuracy for speed**, allowing scalable search across millions or billions of vectors.  
- Used extensively in recommendation engines, similarity search, and retrieval systems.  
- Common algorithms: **HNSW**, **IVF**, **LSH**, **ScaNN**.  
- Unlike brute-force exact search, ANN narrows the search space using index structures.

---
</details>

---

### Payload

<details - open>  
<summary>Payload is the metadata attached to a vector for filtering or enrichment</summary>  
---

- A **payload** is structured or unstructured metadata stored alongside a vector.  
- Examples: `{ "title": "Cat", "tags": ["animal", "pet"], "created_at": "2024-01-01" }`  
- Payloads help apply **filters**, support **hybrid search**, and provide contextual information.  
- They are not part of the vector itself but **extend the search capabilities**.  
- Payloads enable combining **semantic** (vector) and **symbolic** (metadata) filters.

---
</details>

---

### Indexing

<details - open>  
<summary>Indexing structures vectors to make search faster and more efficient</summary>  
---

- **Indexing** is the process of organizing vectors to optimize query performance.  
- Without indexing, searching would require scanning all vectors (**brute-force**).  
- Index types vary depending on speed vs. accuracy trade-offs (e.g., **Flat**, **HNSW**, **IVF**).  
- A good index improves **latency**, **memory usage**, and **accuracy** of results.  
- Some databases support **dynamic indexing** for real-time insertions and updates.

---
</details>

---

### RAG (Retrieval-Augmented Generation)

<details - open>  
<summary>RAG combines retrieval and generation to produce context-aware answers</summary>  
---

- **RAG** is an architecture that integrates **vector search** (retrieval) with **LLMs** (generation).  
- A vector DB retrieves relevant documents based on the query embedding.  
- The retrieved context is then fed into a **language model** to generate accurate, grounded responses.  
- RAG helps overcome LLM limitations like hallucination and outdated knowledge.  
- Used in **AI assistants**, **enterprise Q&A bots**, and **document-based search systems**.

---
</details>

---

### Collection

<details - open>  
<summary>A collection is a logical group of vectors and their payloads</summary>  
---

- A **collection** is the top-level container in a vector database.  
- Similar to a table in SQL or an index in Elasticsearch.  
- Each collection contains:
  - A unique schema,
  - A set of vectors,
  - Their associated payloads,
  - Indexing strategy and metadata.  
- Collections allow for **namespace isolation**, **query scope restriction**, and **versioned datasets**.

---
</details>


---

## Introduction to Vector Databases

---
### Concept Overview and Motivation

<details - open>  
<summary>Definition, motivation, and use cases of vector databases</summary>  
---

- A **Vector Database** is a specialized system designed to store, manage, and search high-dimensional vectors.  
- These vectors typically represent **unstructured data** such as text, images, video, or audio, which are encoded via **embedding models**.  
- Traditional databases are not optimized for **similarity search** based on vector distances (e.g., cosine similarity, Euclidean distance).  
- Vector databases enable **semantic search** — retrieving data that is *contextually similar*, not just textually identical.  
- They are optimized for **Approximate Nearest Neighbor (ANN)** algorithms, supporting fast and scalable vector retrieval.

#### Why Vector Databases Matter

- Explosion of unstructured data requires new ways to represent and query information.
- Embeddings provide a way to compare meaning, not exact matches.
- Vector DBs power intelligent applications like:
  - **Search engines** (semantic, multi-modal)
  - **Recommendation systems**
  - **Chatbots and AI assistants** (via Retrieval-Augmented Generation)
  - **Image/audio recognition**

#### Core Characteristics

- Store billions of vectors efficiently with fast indexing.
- Support hybrid filtering using metadata (payloads).
- Integrate with AI/ML workflows and embedding pipelines.
- Scale horizontally and offer high throughput for real-time applications.

#### Real-World Example
- Instead of matching exact keywords, vector DBs compare the *meaning* of your query:  
  - Input question: **"How to cook beef pho?"**  
    - → is embedded as a vector: `[0.12, 0.45, 0.89, ...]`  
  - System finds documents with similar vectors, like:
    - “Traditional Pho Recipe at Home”
    - “Tips for Rich Pho Broth”  
  - It ignores unrelated content like:
    - “How to Make Pizza”  
- This enables much **smarter, intent-based retrieval** than keyword matching.

#### Popular Vector Database Tools

- A growing ecosystem of open-source and commercial tools exists to support vector-based search:
  - **Qdrant**
  - **Pinecone**
  - **Weaviate**
  - **Milvus**
  - **FAISS** (by Meta)
  - **ElasticSearch** (with vector support)
- These tools differ in indexing strategies, scalability, hybrid search capabilities, and ecosystem integration.

---
</details>

## Comparison of Popular Vector Database Tools

---

### Overview of Tools

<details - open>  
<summary></summary>
---


---

</details>


### Feature Comparison Table
<details - open>  
<summary></summary>
---


---

</details>

## Deep Dive on Qdrant

### Architecture & Components
<details - open>  
<summary></summary>
---


---

</details>

### Core Concepts Refresher
<details - open>  
<summary></summary>
---

#### Vector Similarity Search

---

#### Approximate Nearest Neighbor (ANN)




---



</details>

## Deployment and Setup

<details - open>  
<summary></summary>
---


---

</details>


## Implementation Guidance – Practical Usage Examples

### Example: Semantic Search with Qdrant and Sentence Transformers
<details - open>  
<summary></summary>
---


---

</details>

## Best Practices – Optimization and Performance



## Demo Code 

### Recommendation system (Spotify ELT Project) 