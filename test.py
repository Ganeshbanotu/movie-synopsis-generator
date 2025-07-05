import google.generativeai as genai
genai.configure(api_key="your_key_here")
model = genai.GenerativeModel("models/gemini-pro")
response = model.generate_content("Say something interesting about dinosaurs.")
print(response.text)
