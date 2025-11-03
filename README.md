AI Agent: Course Suggester Prototype

This is a submission for the "AI Agent Prototype" assignment.

Name: Sanjay Jangir

University: IIT Kanpur

Department: Civil Engineering

Project Overview

This project is an AI agent that helps students at IIT Kanpur find courses in the Civil Engineering (CE) department. Users can ask questions in natural language, and the agent will find courses based on the current schedule and historical grading data.

Architecture

The agent uses a Planner-Tool-Executor model:

Planner: A fine-tuned microsoft/Phi-3-mini-4k-instruct model that converts the user's prompt into a JSON query.

Tool: A Python function that uses this JSON to search a final_database.json (our RAG knowledge base).

Executor: The base Phi-3-mini model, which synthesizes the search results into a helpful, natural-language answer.

For a full breakdown, see Architecture_Document.md and Data_Science_Report.md.

How to Run

Setup:

pip install -r requirements.txt


(You will need transformers, torch, datasets, peft, trl, bitsandbytes, accelerate)

Run the Agent:

python agent.py


(This assumes you have combined the final agent code into a single agent.py file)
