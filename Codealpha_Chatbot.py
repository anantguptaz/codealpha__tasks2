def get_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif text in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif text in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"
    elif text in ["what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot."
    elif text == "":
        return "Please type something so I can respond."
    else:
        return "Sorry, I don't understand that. Can you rephrase?"


def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break


if __name__ == "__main__":
    chatbot()
