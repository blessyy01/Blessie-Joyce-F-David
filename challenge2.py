reponses = {
    "hello": "hello, How can i help u?",
    "hi": "hi what can i do",
    "how are you": "im just a bot, but in doing great",
    "tell me about iloilo": "iloilo has phinma",
    "tell me about phinma": "phinma is a school",
    "bye": "good bye",
}

def get_bot_response(user_input):
    return reponses.get(user_input, "I don't understand.")

def main():
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print(f"chatbot: {response}")
        if user_input == "bye":
            break

if '_name_' == "_main_":
    main()