import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

user_ingredients = ["spinach", "paneer", "garlic"]

dynamic_prompt = (
    f"Generate a creative recipe using only these ingredients: {', '.join(user_ingredients)}. "
    "List the ingredients and provide clear step-by-step cooking instructions."
)

response = model.generate_content(
    dynamic_prompt,
    generation_config={"temperature": 0.7}  # Set temperature for creativity
)

print(response.text)