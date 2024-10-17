import openai

API_KEY = ""
client = openai.OpenAI(api_key={API_KEY})
print(client)

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'assistant', "content": "Kto wygrał f1 w 2020 roku"}]
)

print(response)
print(response.choices[0].message.content)
