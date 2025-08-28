import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

chain_of_thought_prompt = """
Let's think step by step.

Ingredients: tomato, rice, onion

First, analyze how these ingredients can be combined in a dish.
Next, plan the cooking steps in logical order.
Finally, write out the recipe with clear instructions.

Show your reasoning before giving the final recipe.
"""

response = model.generate_content(chain_of_thought_prompt)
print(response.text)