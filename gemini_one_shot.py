import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

one_shot_prompt = """
Example:
Ingredients: egg, bread, cheese
Recipe:
1. Beat the egg in a bowl.
2. Dip bread slices in the egg.
3. Place cheese between bread slices.
4. Cook on a pan until golden brown.

Now, generate a recipe using these ingredients: tomato, rice, onion. List the ingredients and provide clear step-by-step cooking instructions.
"""

response = model.generate_content(one_shot_prompt)
print(response.text)