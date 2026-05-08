import google.generativeai as genai

# 1. Configuration - Replace the text below with your actual API key
API_KEY = "YOUR_API_KEY_HERE"
genai.configure(api_key=API_KEY)

# 2. Initialize the Model (The 'Brain')
# We define this globally so app.py can import it easily
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Terminal function (for testing without the website)
def start_ai():
    print("--- AI Terminal Mode Active ---")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        try:
            response = model.generate_content(user_input)
            print(f"AI: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

# 4. Safety Block
# This prevents the terminal mode from starting when app.py imports this file
if __name__ == "__main__":
    start_ai()
