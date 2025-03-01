# Prompt Engineering Starter Pack

This repository contains various examples and techniques for prompt engineering using Python. The examples demonstrate different ways to interact with language models using prompts.

## Files

### `few_shot_prompt.py`
This script demonstrates the few-shot learning technique by providing multiple examples in the prompt to guide the model's response.

### `chain_of_thought_prompt.py`
This script showcases the chain-of-thought prompting technique, where the model is guided to think step-by-step to arrive at the correct answer.

### `basic-prompt.py`
This script provides a basic example of interacting with a language model using a simple prompt. It also demonstrates how to change the temperature parameter to control the randomness of the model's responses.

## Usage

1. Clone the repository:
    ```sh
    git clone git@personal.github.com:yirgagithub/Prompt-Engineering-Starter-Pack.git
    cd Prompt-Engineering-Starter-Pack
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the scripts:
    ```sh
    python few_shot_prompt.py
    python chain_of_thought_prompt.py
    python basic-prompt.py
    ```

## Repository Structure

- `few_shot_prompt.py`: Demonstrates few-shot learning with multiple examples.
- `chain_of_thought_prompt.py`: Demonstrates chain-of-thought prompting.
- `basic-prompt.py`: Basic example of prompt interaction and temperature control.
