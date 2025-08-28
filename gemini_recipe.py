import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

prompt = (
    "Generate a creative recipe using only these ingredients: tomato, rice, onion. "
    "List the ingredients and provide clear step-by-step cooking instructions."
)

response = model.generate_content(prompt)
print(response.text)