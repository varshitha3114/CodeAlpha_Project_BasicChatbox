class SimpleChatbot:
    def __init__(self):
        self.responses =  {
            "hi": ["Hello,How can I help you?"],
            "how are you": ["I'm doing well, thank you"],
            "your name": ["I'm a chatbot ,designed to help you"],
            "help": ["Sure, I can help for you"],
            "tell me about python": ["Python is a general-purpose, high-level programming language. It is easy to learn and use, and it is very powerful. "],
            "thankyou":["My pleasure,Is there anything else to help"],
            "bye": ["Bye! Take care,See you later."]
        }

    def respond(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return self.responses[key]
        return "I'm sorry, I didn't understand that."


def conversation():
    chatbot = SimpleChatbot()
    print("\n")
    print("Welcome! To ChatBox World.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        if isinstance(response, list):
            print("Bot:", response[0])  
        else:
            print("Bot:", response)
        if user_input.lower() == 'bye':
            break

# Start the chatbot conversation
conversation()
