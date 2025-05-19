# AI Chat Log Summarizer

A Python-based tool to read `.txt` chat logs between a User and an AI, analyze the conversation, and generate a summary.

---

## Features

- Parse chat logs to separate User and AI messages
- Count message statistics
- Extract top 5 most common keywords (excluding stop words)
- Generate a clear text summary
- Optional: Extendable for TF-IDF-based keyword analysis (Not Included here)

## Sample Input (chat.txt)
User: Hello!</br>
AI: Hi! How can I assist you today?</br>
User: Can you explain what machine learning is?</br>
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.

## Sample Output
===== Chat Summary =====

The conversation had 4 exchanges.

User messages: 2, </br>AI messages: 2

The conversation mainly focused on: machine, learning, data, ai, systems.

Most common keywords:
 machine: 1 </br>
 learning: 1 </br>
 data: 1 </br>
 ai: 1 </br>
 systems: 1 </br>

 ## How to Run
1. Clone the repository: </br>
   git clone https://github.com/Tamal1144/ai-chat-log-summarizer.git </br>
   cd ai-chat-log-summarizer
2. Make sure Python 3 is installed.
3. Place your chat file as chat.txt in the root folder.
4. Run the summarizer: </br>
    python chat_summarizer.py

## Folder Structure
├── chat.txt </br>
├── chat_summarizer.py </br>
└── README.md </br>

## Requirements
1.Python 3.x </br>
2.No external libraries required for the basic version

# Outputs
## Chat Log Parsing
![image](https://github.com/user-attachments/assets/57d0e22d-a01f-4575-b0fe-fa1b13e31360)
## Message Statistics
![image](https://github.com/user-attachments/assets/dbc78ed6-c1e7-4a83-917b-5d541aa240c6)
## Keyword Analysis
![image](https://github.com/user-attachments/assets/c3e8ef7b-6653-488e-8d66-b68d8dd603a5)
## Generate Summary
![image](https://github.com/user-attachments/assets/2c86e4c7-a65a-4f87-a298-d1c3f23b12a4)
