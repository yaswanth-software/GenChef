import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

multi_shot_prompt = """
Example 1:
Ingredients: egg, bread, cheese
Recipe:
1. Beat the egg in a bowl.
2. Dip bread slices in the egg.
3. Place cheese between bread slices.
4. Cook on a pan until golden brown.

Example 2:
Ingredients: potato, peas, carrot
Recipe:
1. Boil potato, peas, and carrot until soft.
2. Mash the vegetables together.
3. Season with salt and pepper.
4. Serve warm.

Now, generate a recipe using these ingredients: tomato, rice, onion. List the ingredients and provide clear step-by-step cooking instructions.
"""

response = model.generate_content(multi_shot_prompt)
print(response.text)