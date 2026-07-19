# Basic Rule-Based Chatbot

A simple Python chatbot that responds to predefined user inputs using rule-based matching (if-elif logic). Built as a beginner-friendly project to practice core Python concepts.

## 📋 Task

**Task 4: Basic Chatbot**

Build a simple rule-based chatbot that:
- Accepts user input like `"hello"`, `"how are you"`, `"bye"`
- Returns predefined replies like `"hi!"`, `"i'm fine, thanks!"`, `"goodbye!"`

## 🧠 Key Concepts Used

- `if-elif` conditional statements
- Functions
- Loops (`while`)
- Input/Output (`input()`, `print()`)

## 📁 Files

| File | Description |
|------|-------------|
| `chatbot.py` | Main chatbot script |
| `README.md` | Project documentation |

## ⚙️ How It Works

1. `get_response(user_input)` — takes the user's text, cleans it up (lowercase + strip whitespace), and checks it against known phrases using `if-elif`.
2. `chatbot()` — runs a `while True` loop that keeps prompting the user for input and printing the chatbot's reply.
3. The loop ends when the user types a goodbye phrase (`bye`, `goodbye`, `see you`).

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python chatbot.py
```

## 💬 Example Conversation

```
Chatbot: Hi! Type 'bye' to exit.
You: hello
Chatbot: Hi! How can I help you today?
You: how are you
Chatbot: I'm fine, thanks! How about you?
You: bye
Chatbot: Goodbye! Have a great day!
```

## 🔧 Supported Inputs

| User Input | Chatbot Reply |
|---|---|
| `hello` / `hi` / `hey` | Hi! How can I help you today? |
| `how are you` | I'm fine, thanks! How about you? |
| `bye` / `goodbye` / `see you` | Goodbye! Have a great day! |
| `what is your name` / `who are you` | I'm a simple rule-based chatbot. |
| *(anything else)* | Sorry, I don't understand that. Can you rephrase? |

## 🚀 Possible Improvements

- Add more phrases and topics
- Make the chatbot remember the user's name during the conversation
- Add fuzzy matching for typos or slightly different phrasing
- Convert to a GUI or web-based chatbot

## 👤 Author

Built as part of a Python learning task series.
