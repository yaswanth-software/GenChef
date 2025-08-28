import google.generativeai as genai
import json

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

user_ingredients = ["spinach", "paneer", "garlic"]

structured_prompt = (
    f"Generate a creative recipe using only these ingredients: {', '.join(user_ingredients)}. "
    "Return the output as a JSON object with two fields: 'ingredients' (a list of ingredients) and 'steps' (a list of step-by-step instructions)."
)

response = model.generate_content(structured_prompt)

# Try to parse the response as JSON
try:
    recipe_json = json.loads(response.text)
    print(json.dumps(recipe_json, indent=2))
except json.JSONDecodeError:
    print("Could not parse response as JSON. Raw response:")
    print(response.text)