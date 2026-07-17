print("Welcome to Khushi's AI Chatbot!")

responses = {
   
    "hello": "Hello! How can I help you?",
    "good morning": "Good morning! Have a wonderful day!",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! Hope you're doing well.",
    "good night": "Good night! Sweet dreams.",
    "how are you": "I'm doing great. Thanks for asking!",
    "who are you": "I am a simple AI chatbot created using Python.",
    "what is ai": "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.",
    "what is python": "Python is a simple and powerful programming language used for web development, AI, data science, and automation.",
    "what can you do": "I can answer simple predefined questions and chat with you.",
    "who made you": "I was created by Khushi as part of the DecodeLabs AI Internship.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",
    "bye": "Goodbye! Have a great day!",
    "help": "You can ask me about AI, Python, greetings, or type exit to quit."

}

while True:
    user = input("You: ").strip().lower()

    if user == "exit":
        print("Bot: Thank you. See you again!")
        break

    print("Bot:", responses.get(user, "Sorry, I don't understand."))
