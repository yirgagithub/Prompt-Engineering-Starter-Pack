# basic example
from main import set_open_params, get_completion

params = set_open_params()

prompt = "chatgpt is "

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(params, messages)
print(response.choices[0].message.content)


# change the temperature
params = set_open_params(temperature=0)
response = get_completion(params, messages)
print(response.choices[0].message.content)