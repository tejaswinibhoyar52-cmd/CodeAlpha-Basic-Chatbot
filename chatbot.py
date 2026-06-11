def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("Bot: Hi!")

        elif user in ["how are you", "how are u", "how are u?"]:
            print("Bot: I'm fine, thanks!")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()