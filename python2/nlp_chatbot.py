import nltk
import random
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?",]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created using NLTK. You can call me NLP Bot!",]
    ],
    [
        r"how are you?",
        ["I'm just a program, but functioning well! How about you?",]
    ],
    [
        r"(.*) help (.*)",
        ["I can answer basic questions and have simple conversations. What do you need help with?",]
    ],
    [
        r"(.*) weather (.*)",
        ["I don't have real-time weather data, but you can check weather services for accurate forecasts.",]
    ],
    [
        r"quit|bye|goodbye",
        ["Goodbye! It was nice talking to you.", "See you later!",]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?",]
    ]
]

def chatbot():
    print("Welcome to the NLP Chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

