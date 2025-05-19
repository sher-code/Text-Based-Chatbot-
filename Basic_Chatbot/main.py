import nltk
nltk.download('punkt')
nltk.download('wordnet')



from nltk.chat.util import Chat, reflections

# Define a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Sher Muhammad.", "You can call me ChatBuddy."]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm doing fine!", "All good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem!", "It's okay, don't worry about it."]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that!", "Awesome! Keep it up."]
    ],
    [
        r"what (.*) want ?",
        ["I just want to chat with you!", "Helping you is my goal."]
    ],
    [
        r"(.*) created you ?",
        ["Sher Muhammad created me using Python and NLTK.", "A human made me."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual entity, but you can say I'm from the cloud!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "It was nice talking to you. Bye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Tell me more!", "Interesting..."]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the chat
def start_chat():
    print("Hi! I'm ChatBuddy. Type 'bye' to exit.")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()
