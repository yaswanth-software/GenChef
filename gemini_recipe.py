import google.generativeai as genai

genai.configure(api_key="AIzaSyAsd-VdPHDhVnZ_PlAVMYavh2hNNEy-uoU")

model = genai.GenerativeModel("gemini-pro")

prompt = (
    "Generate a creative recipe using only these ingredients: tomato, rice, onion. "
    "List the ingredients and provide clear step-by-step cooking instructions."
)

response = model.generate_content(prompt)
print(response.text)