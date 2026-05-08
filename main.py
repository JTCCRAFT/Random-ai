import google.generativeai as genai

# This links your code to the AI "engine"
genai.configure(api_key="YOUR_API_KEY_HERE")

# Selecting the model (the 'brain')
model = genai.GenerativeModel('gemini-1.5-flash')

# The function that makes it work
def start_ai():
    user_input = input("Ask your AI something: ")
    response = model.generate_content(user_input)
    print(f"AI Response: {response.text}")

start_ai()
