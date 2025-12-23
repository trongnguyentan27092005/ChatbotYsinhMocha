# ChatbotYsinhMocha

A simple, interactive chatbot built with Python that can engage in friendly conversations.

## Features

- 🤖 Interactive command-line chat interface
- 💬 Pattern-based response system
- ⏰ Can tell you the current time and date
- ☕ Special responses about mocha and coffee
- 🎯 Handles greetings, farewells, and common questions
- 🔄 Natural conversation flow with varied responses

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/trongnguyentan27092005/ChatbotYsinhMocha.git
cd ChatbotYsinhMocha
```

2. Make the chatbot executable (optional):
```bash
chmod +x chatbot.py
```

## Usage

Run the chatbot using Python:

```bash
python3 chatbot.py
```

Or if you made it executable:

```bash
./chatbot.py
```

## Example Conversation

```
============================================================
  Welcome to Ysinh Mocha Chatbot!
============================================================
Type 'quit' or 'exit' to end the conversation.

You: Hello
Ysinh Mocha: Hello! I'm Ysinh Mocha. How can I help you today?

You: What's your name?
Ysinh Mocha: I'm Ysinh Mocha, your friendly chatbot assistant!

You: What time is it?
Ysinh Mocha: The current time is 14:30:45

You: Tell me about mocha
Ysinh Mocha: Mmm, I love mocha! ☕ It's the perfect blend of coffee and chocolate.

You: Thanks!
Ysinh Mocha: You're welcome!

You: bye
Ysinh Mocha: Goodbye! Have a great day!
```

## How It Works

The chatbot uses regular expression pattern matching to identify user intents and respond appropriately. It can:

- Recognize greetings and respond warmly
- Answer questions about itself
- Provide time and date information
- Engage in small talk
- Handle farewells gracefully

## Customization

You can easily customize the chatbot by editing the `patterns` dictionary in `chatbot.py`. Add new patterns and responses to expand the chatbot's capabilities!

## License

Open source - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for improvements.
