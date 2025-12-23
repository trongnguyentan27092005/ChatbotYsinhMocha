#!/usr/bin/env python3
"""
ChatbotYsinhMocha - A Simple Interactive Chatbot
"""

import random
import re
from datetime import datetime


class ChatbotYsinhMocha:
    """A simple chatbot with predefined responses and pattern matching."""
    
    def __init__(self):
        self.name = "Ysinh Mocha"
        self.patterns = {
            r'\b(hi|hello|hey)\b': [
                f"Hello! I'm {self.name}. How can I help you today?",
                f"Hi there! {self.name} here. What's on your mind?",
                f"Hey! Nice to meet you!"
            ],
            r'\b(how are you|how do you do)\b': [
                "I'm doing great, thank you for asking! How about you?",
                "I'm fantastic! Thanks for checking in.",
                "I'm well, thanks! How can I assist you today?"
            ],
            r'\b(bye|goodbye|see you)\b': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! Feel free to come back anytime!"
            ],
            r'\b(thank|thanks)\b': [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Glad I could assist."
            ],
            r'\b(what.*your name|who are you)\b': [
                f"I'm {self.name}, your friendly chatbot assistant!",
                f"My name is {self.name}. Nice to meet you!"
            ],
            r'\b(help|what can you do)\b': [
                "I can chat with you! Try asking me about:\n- Greetings (hello, hi)\n- How I'm doing\n- My name\n- The time\n- Or just chat with me!",
                "I'm here to chat! Ask me anything or just say hello!"
            ],
            r'\b(time|what time)\b': 'time',
            r'\b(date|what.*date|today)\b': 'date',
            r'\b(mocha|coffee)\b': [
                "Mmm, I love mocha! ☕ It's the perfect blend of coffee and chocolate.",
                "Mocha is my favorite! Rich, chocolatey, and energizing!"
            ]
        }
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. What else would you like to talk about?",
            "Hmm, I'm not sure I understand completely, but I'm here to chat!",
            "That's a good point! What else is on your mind?",
            "I appreciate you sharing that with me!"
        ]
        
        self.response_counter = 0
    
    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input_lower = user_input.lower()
        
        # Check patterns
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower):
                # Handle special dynamic responses
                if responses == 'time':
                    return f"The current time is {datetime.now().strftime('%H:%M:%S')}"
                elif responses == 'date':
                    return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}"
                else:
                    return random.choice(responses)
        
        # Default response
        response = self.default_responses[self.response_counter % len(self.default_responses)]
        self.response_counter += 1
        return response
    
    def chat(self):
        """Main chat loop."""
        print(f"=" * 60)
        print(f"  Welcome to {self.name} Chatbot!")
        print(f"=" * 60)
        print("Type 'quit' or 'exit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit']:
                    print(f"\n{self.name}: Goodbye! Thanks for chatting with me! 👋")
                    break
                
                response = self.get_response(user_input)
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Thanks for chatting with me! 👋")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue


def main():
    """Entry point for the chatbot."""
    bot = ChatbotYsinhMocha()
    bot.chat()


if __name__ == "__main__":
    main()
