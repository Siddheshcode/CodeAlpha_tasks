#Basic Rule-Based Chatbot

def chatbot_response(user_input):
user_input = user_input.lower()

if user_input == "hello":  
    return "Hi! 👋"  
elif user_input == "how are you":  
    return "I'm fine, thanks! 😊"  
elif user_input == "bye":  
    return "Goodbye! 👋 Have a nice day!" 
elif user_input == "good morning":
    return "Good morning!"
elif user_input == "good evening":
    return "Good evening!"
elif user_input == "what is your name?":
    return "I am a simple chatbot."
elif user_input == "what can you do?":
    return "I can chat with you using simple rules."
else:  
    return "Sorry, I don't understand that."

#Main program loop

print("🤖 Chatbot is running...")
print("Type 'hello', 'how are you', or 'bye' to chat.")
print("Type 'bye' to exit.\n")