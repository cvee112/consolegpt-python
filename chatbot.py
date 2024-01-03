# Import OpenAI
from openai import OpenAI

# Create client
client = OpenAI()

# Define chat function
def chat(prompt, model, temperature, chatbot_name):
    context.append({"role": "user", "content":f'{prompt}'})
    response = client.chat.completions.create(
        model=model,
        messages=context,
        temperature=temperature
    )
    context.append({"role": "assistant", "content":f'{response.choices[0].message.content}'})
    print(f"\n{chatbot_name}: {response.choices[0].message.content}")

# Give introduction and go to part 1 (choose your model)
print("""
===============\n
INTRODUCTION\n
===============\n
Welcome to CustomGPT! Here, you'll get an opportunity to chat with a custom bot.\n
\n===============\n
DESIGN YOUR BOT\n
===============\n
Note: If you want the defaults, just leave the fields blank.\n
-------------------------\n
PART 1: CHOOSE YOUR MODEL\n
-------------------------\n
Choose wisely! Advanced models are more capable but cost more.\n
See https://platform.openai.com/docs/models for more details.\n""")

# Ask for model number
models = {
        '1': 'gpt-4-1106-preview',
        '2': 'gpt-4-vision-preview',
        '3': 'gpt-4',
        '4': 'gpt-4-32k',
        '5': 'gpt-3.5-turbo-1106',
        '6': 'gpt-3.5-turbo',
        '7': 'gpt-3.5-turbo-16k'
}

print("""The available models are:\n
        1. gpt-4-1106-preview\n
        2. gpt-4-vision-preview\n
        3. gpt-4\n
        4. gpt-4-32k\n
        5. gpt-3.5-turbo-1106 (default)\n
        6. gpt-3.5-turbo\n
        7. gpt-3.5-turbo-16k\n""")

while True:
    model_choice = int(input("\nModel number (1-7): "))
    if not ValueError:
        break

if model_choice.strip() == "":
    model = models['5']
else:
    model = models[str(model_choice)]

# Go to part 2 (customize your bot)
print("""\n--------------------------\n
PART 2: CUSTOMIZE YOUR BOT\n
--------------------------""")

# Ask for custom instructions
custom_instructions = input("\nCustom instructions (optional): ")

if custom_instructions.strip() == "":
    custom_instructions = "You are a helpful assistant."

# Ask for chatbot name
chatbot_name = input("\nChatbot name (optional): ")

if chatbot_name.strip() == "":
    chatbot_name = "Assistant"

# Ask for temperature within valid range
temperature = -1

while temperature < 0 or temperature > 1:
    temperature = input("\nTemperature [0.0 to 1.0] (optional): ")
    if temperature.strip() == "":
        temperature = 0.7
    else:
        temperature = float(temperature)

# Go to part 3 (summary of parameters)
print(f"""\n-----------------------------\n
PART 3: SUMMARY OF PARAMETERS\n
-----------------------------\n
Model: {model}\n
Custom instructions: {custom_instructions}\n
Chatbot name: {chatbot_name}\n
Temperature: {temperature}""")

# Create initial context
context = [{'role':'system', 'content':f'{custom_instructions}'}]  # accumulate messages

# Transition to chat proper
print(f"""\n\n===================\n
CHAT WITH {chatbot_name.upper()}\n
===================\n
If you want to end the chat at any point, type \"/end\" then <Enter>.\n""")

# Chat until user inputs "/end"
while True:
    prompt = input("\nUser: ")
    if prompt.strip() != '/end':
        chat(prompt, model, temperature, chatbot_name)
    else:
        break

# Give outro
print(f"""\n\n=============\n
END OF SESSION\n
=============\n
Thanks for chatting with {chatbot_name}!\n""")
