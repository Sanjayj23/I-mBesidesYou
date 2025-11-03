# AI Agent: Course Suggester Prototype

Author: Sanjay Jangir  
University: IIT Kanpur  
Department: Civil Engineering  

---

### Project Overview

This project is an AI agent designed to help students at IIT Kanpur discover courses in the Civil Engineering (CE) department. Users can ask questions in natural language, and the agent provides relevant course suggestions based on the current semester schedule and historical grading data.

The agent leverages a Planner–Tool–Executor architecture inspired by modular instruction-following AI design.

---

### Architecture

The system is composed of three key components:

- **Planner:**  
  A fine-tuned microsoft/Phi-3-mini-4k-instruct model that converts user queries into structured JSON search requests.

- **Tool:**  
  A Python function that processes the Planner’s JSON output to query final_database.json — the Retrieval-Augmented Generation (RAG) knowledge base containing course details and grading records.

- **Executor:**  
  The base Phi-3-mini model that synthesizes the Tool’s retrieved data into a coherent, natural-language response for the user.

For a detailed explanation of the architecture and methodology, refer to:
- Architecture_Document.md
- Data_Science_Report.md

---

### Setup Instructions

Clone the repository and install dependencies:

