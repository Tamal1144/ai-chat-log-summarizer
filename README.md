# AI Chat Log Summarizer

A Python-based tool to read `.txt` chat logs between a User and an AI, analyze the conversation, and generate a summary.

---

## Features

- Parse chat logs to separate User and AI messages
- Count message statistics
- Extract top 5 most common keywords (excluding stop words)
- Generate a clear text summary
- Optional: Extendable for TF-IDF-based keyword analysis

## Sample Input (chat.txt)
User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what machine learning is?
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.

## Sample Output
===== Chat Summary =====

The conversation had 4 exchanges.

User messages: 2, AI messages: 2

The conversation mainly focused on: machine, learning, data, ai, systems.

Most common keywords:
 machine: 1
 learning: 1
 data: 1
 ai: 1
 systems: 1

 ## How to Run
1. Clone the repository:
   git clone https://github.com/Tamal1144/ai-chat-log-summarizer.git
   cd ai-chat-log-summarizer
2. Make sure Python 3 is installed.
3. Place your chat file as chat.txt in the root folder.
4. Run the summarizer:
    python chat_summarizer.py

## Folder Structure
├── chat.txt
├── chat_summarizer.py
└── README.md

## Requirements
1.Python 3.x
2.No external libraries required for the basic version
