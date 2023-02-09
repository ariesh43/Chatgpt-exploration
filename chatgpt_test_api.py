import openai


openai.api_key = API_KEY
prompt = "Name some travel technology companies."
response = openai.Completion.create(
    engine="text-davinci-003", prompt=prompt, max_tokens=29, n=1
)
print(response)
