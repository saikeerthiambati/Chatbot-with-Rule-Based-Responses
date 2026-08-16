from datetime import datetime
import random

user_name = None


def get_response(text):
    global user_name
    text = text.lower().strip()

    # ---- Empty input ----
    if text == "":
        return "Please type something!"

    # ---- Name memory ----
    if "my name is" in text:
        user_name = text.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {user_name}!"

    # ---- Greetings ----
    elif "hi" in text or "hello" in text:
        greetings = [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! How's it going?",
            "Greetings! How can I assist you?",
            "Hi! Nice to see you. What can I help you with today?"
        ]
        if user_name:
            return f"Hello {user_name}! How can I help you?"
        return random.choice(greetings)

    # ---- How are you ----
    elif "how are you" in text:
        return "I'm just a bot, but I'm doing great! How about you?"

    # ---- Menu / Help ----
    elif "menu" in text or "options" in text or "help" in text:
        return ("Here's what I can do:\n"
                "  • Greet you (hi, hello)\n"
                "  • Tell you the time or date\n"
                "  • Share a Python/AI fact (type 'fact')\n"
                "  • Solve simple math (like: 5 + 3)\n"
                "  • Give a motivational quote (type 'quote')\n"
                "  • Calculate your age (type: I was born in 2005)\n"
                "  • Give you a compliment (type 'compliment')\n"
                "  • Remember your name (type: my name is Ravi)")

    # ---- Bot's name ----
    elif "your name" in text:
        return "I'm SAM Bot, a simple rule-based chatbot."

    # ---- Thanks ----
    elif "thank" in text:
        return "You're welcome! If you have any more questions, feel free to ask."

    # ---- Time ----
    elif "time" in text:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # ---- Date ----
    elif "date" in text:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    # ---- Facts (Python / ML / AI) ----
    elif "fact" in text:
        facts = [
            "Python was named after the comedy show 'Monty Python's Flying Circus', not the snake.",
            "The term 'Machine Learning' was coined by Arthur Samuel in 1959.",
            "Python is one of the most popular languages for AI because of libraries like TensorFlow, PyTorch, and scikit-learn.",
            "The first AI program was written in 1951 to play checkers.",
            "Deep Learning models are inspired by how neurons in the human brain work.",
            "Python doesn't need a compiler — it's an interpreted language, which makes testing AI code faster.",
            "ChatGPT and similar AI models are built using a neural network architecture called a Transformer, introduced in 2017.",
            "Google's TensorFlow and Facebook's PyTorch are the two most widely used ML frameworks, both usable in Python."
        ]
        return random.choice(facts)

    # ---- Motivational quote ----
    elif "quote" in text:
        quotes = [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Code is like humor. When you have to explain it, it's bad. – Cory House",
            "First, solve the problem. Then, write the code. – John Johnson",
            "Success is the sum of small efforts, repeated day in and day out."
        ]
        return random.choice(quotes)

    # ---- Compliment ----
    elif "compliment" in text:
        compliments = [
            "You're doing an amazing job learning to code!",
            "You ask great questions.",
            "You're going to be a great developer!"
        ]
        return random.choice(compliments)

    # ---- Age calculator ----
    elif "born in" in text:
        try:
            year = int(text.split("born in")[-1].strip())
            age = datetime.now().year - year
            return f"You are {age} years old (approximately)."
        except Exception:
            return "Please tell me a valid year, like: I was born in 2005"

    elif "calculate my age" in text or "my age" in text:
        return "Sure! Just tell me your birth year, like: I was born in 2005"

    # ---- Simple math (kept near the end since it's a broad check) ----
    elif any(op in text for op in ["+", "-", "*", "/"]):
        allowed_chars = "0123456789+-*/(). "
        if all(ch in allowed_chars for ch in text):
            try:
                result = eval(text)
                return f"The answer is {result}"
            except Exception:
                return "Sorry, I couldn't calculate that. Try something like 10 * 2."
        return "Please give me a valid math expression, like 5 + 3."

    # ---- Bye ----
    elif "bye" in text:
        return "Goodbye! Have a great day!"

    # ---- Default ----
    else:
        return "I'm sorry, I didn't understand that. Type 'menu' to see what I can do."


# ---------------- Startup message ----------------
print("Chat Bot: Hi! I'm SAM Bot. Here's what I can do:")
print("  • Greet you (hi, hello)")
print("  • Tell you the time or date")
print("  • Share a Python/AI fact (type 'fact')")
print("  • Solve simple math (like: 5 + 3)")
print("  • Give a motivational quote (type 'quote')")
print("  • Calculate your age (type: I was born in 2005)")
print("  • Give you a compliment (type 'compliment')")
print("Type 'menu' anytime to see this again. Type 'exit' or 'bye' to quit.\n")

# ---------------- Main loop ----------------
while True:
    user_input = input("You: ")

    if user_input.lower().strip() in ["exit", "bye"]:
        print("Chat Bot: Goodbye! Have a great day!")
        break

    response = get_response(user_input)
    print(f"Chat Bot: {response}")