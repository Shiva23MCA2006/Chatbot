import nltk
import random
import string

# Download NLTK data
nltk.download('punkt')  # Tokenizer
nltk.download('wordnet')  # WordNet for synonyms and lemmatization
from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help you today?"],
    "how are you": ["I'm just a bot, but I'm doing well. How about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "what is your name": ["I'm a chatbot, and you can call me Bot!"],
    "default": ["I'm sorry, I didn't understand that. Can you rephrase?"]
}

def get_response(user_input):
    """
    Function to fetch a response based on user input.
    """
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    # Match response
    for key in responses.keys():
        if key in tokens:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def chatbot():
    """
    Function to run the chatbot interaction.
    """
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
 