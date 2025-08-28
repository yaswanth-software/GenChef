import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

user_ingredients = ["spinach", "paneer", "garlic"]

dynamic_prompt = (
    f"Generate a creative recipe using only these ingredients: {', '.join(user_ingredients)}. "
    "List the ingredients and provide clear step-by-step cooking instructions."
)

response = model.generate_content(dynamic_prompt)

print(response.text)

# Log token usage (if available)
if hasattr(response, "usage_metadata"):
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    total_tokens = prompt_tokens + response_tokens
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(f"Total tokens used: {total_tokens}")
else:
    print("Token usage information is not available for this response.")