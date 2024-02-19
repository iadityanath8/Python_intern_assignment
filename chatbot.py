from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello",
        ["Hi there! How can I assist you today?", "Hello! What can I help you with?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm feeling great, thanks for asking!"]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions and engage in conversation with you.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am based in cyberspace',]
    ],
    [
        r"how old are you ?",
        ["I am a chatbot, so I don't have an age.",]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by a developer using Python's NLTK library.",]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with various things. Please ask me a question.",]
    ],
    [
        r"quit",
        ["Bye! Take care. Have a great day!"]
    ],
]

def chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
