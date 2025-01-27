import google.generativeai as genai

genai.configure(api_key="AIzaSyB2L4z3n7GybrOsNp9gmUmIW_CSdML5el0")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("How does AI work?")
print(response.text)
