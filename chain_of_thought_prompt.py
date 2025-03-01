from main import set_open_params, get_completion

params = set_open_params()
prompt = """The capital of France is Paris.
A: Let's think step by step. France is a country in Europe. The capital city of France is Paris. The answer is Paris.

The capital of Japan is Tokyo.
A: Let's think step by step. Japan is a country in Asia. The capital city of Japan is Tokyo. The answer is Tokyo.

The capital of Canada is Ottawa.
A: Let's think step by step. Canada is a country in North America. The capital city of Canada is Ottawa. The answer is Ottawa.

The capital of Australia is Canberra.
A: Let's think step by step. Australia is a country in Oceania. The capital city of Australia is Canberra. The answer is Canberra.

The capital of Brazil is Brasília.
A: Let's think step by step. Brazil is a country in South America. The capital city of Brazil is Brasília. The answer is Brasília.

The capital of Ethiopia is?
"""

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

response = get_completion(params, messages)
print(response.choices[0].message.content)