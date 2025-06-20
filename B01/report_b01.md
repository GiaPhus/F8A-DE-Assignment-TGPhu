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





---

## Introduction to Vector Databases

---

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