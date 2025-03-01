from main import set_open_params, get_completion

# Set your parameters for the OpenAI model
params = set_open_params()

prompt = """
Which planet in our solar system is the heaviest and which is the lightest?

Reasoning Path A:
1. Jupiter is the largest planet by far in terms of mass.
2. Mercury is the smallest planet and has the least mass.
3. Therefore, Jupiter is the heaviest and Mercury is the lightest.

Reasoning Path B:
1. Jupiter has more mass than all other planets combined.
2. Mercury is smaller and less massive than Venus, Earth, or Mars.
3. Hence, Jupiter is heaviest, Mercury is lightest.

Reasoning Path C:
1. Among the gas giants, Jupiter is clearly the most massive.
2. Among the terrestrial planets, Mercury is the smallest and lightest.
3. This confirms Jupiter as the heaviest, Mercury as the lightest.

Final Answer: 
Jupiter is the heaviest planet, and Mercury is the lightest planet.

Q Which country is the largest?
"""

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(params, messages)
print(response.choices[0].message.content)
