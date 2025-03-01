from main import get_completion, set_open_params

params = set_open_params()
prompt = """The sum of the prime numbers in this group is greater than 20: 4, 7, 9, 15, 12, 2, 3.
A: The answer is True.

The sum of the prime numbers in this group is greater than 20: 17, 10, 19, 4, 8, 12, 24.
A: The answer is True.

The sum of the prime numbers in this group is greater than 20: 16, 11, 14, 4, 8, 13, 24.
A: The answer is True.

The sum of the prime numbers in this group is greater than 20: 17, 9, 10, 12, 13, 4, 2.
A: The answer is True.

The sum of the prime numbers in this group is greater than 20: 15, 32, 5, 13, 82, 7, 1. 
A:"""

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(params, messages)
print(response.choices[0].message.content)