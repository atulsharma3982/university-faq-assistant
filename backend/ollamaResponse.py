from ollama import chat

messages = [
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    {
        'role': 'assistant',
        'content': "The sky is blue because of the way the Earth's atmosphere scatters sunlight.",
    },
    {
        'role': 'user',
        'content': 'What is the weather in Tokyo?',
    },
    {
        'role': 'assistant',
        'content': """The weather in Tokyo is typically warm and humid during the summer months, with temperatures often exceeding 30°C (86°F). The city experiences a rainy season from June to September, with heavy rainfall and occasional typhoons. Winter is mild, with temperatures
        rarely dropping below freezing. The city is known for its high-tech and vibrant culture, with many popular tourist attractions such as the Tokyo Tower, Senso-ji Temple, and the bustling Shibuya district.""",
    },
    ]

while True:
    user_input = input('Chat with history: ')
    response = chat(
        'cogito-2.1:671b',
        messages=[*messages, {'role': 'user', 'content': user_input}],
    )

    # Add the response to the messages to maintain the history
    messages += [
        {'role': 'user', 'content': user_input},
        {'role': 'assistant', 'content': response.message.content},
    ]
    print(response.message.content + '\n')

# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# api_key = os.getenv("OLLAMA_API_KEY")

# url = "https://ollama.com/api/chat"

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# data = {
#     "model": "gpt-oss:20b-cloud",
#     "messages": [
#         {"role": "user", "content": "Hello"}
#     ]
# }

# response = requests.post(url, json=data, headers=headers)

# print(response.status_code)
# print(response.text)