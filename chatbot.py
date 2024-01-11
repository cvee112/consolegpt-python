# Import libraries
from openai import OpenAI
import os
import ast 
import validators

# Create client
client = OpenAI()

# Define Chatbot class
class Chatbot:
    def __init__(self, model="gpt-3.5-turbo-1106", temperature=0.7, custom_instructions="You are a helpful assistant.", chatbot_name = "Assistant"):
        self.model = model
        self.temperature = temperature
        self.custom_instructions = custom_instructions
        self.chatbot_name = chatbot_name
        self.context = [{'role':'system', 'content':f'{custom_instructions}'}]

    def chat(self, prompt):
        self.context.append({"role": "user", "content":f'{prompt}'})
        if self.model == 'gpt-4-vision-preview':
            response = client.chat.completions.create(
                model=self.model,
                messages=self.context,
                temperature=self.temperature,
                max_tokens=2048
            )
        else:
            response = client.chat.completions.create(
                model=self.model,
                messages=self.context,
                temperature=self.temperature
            )
        self.context.append({"role": "assistant", "content":f'{response.choices[0].message.content}'})
        print(f"\n{self.chatbot_name}: {response.choices[0].message.content}")

    def chat_image(self, prompt, url):
        self.context.append({"role": "user", "content": [
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": url
                }
            }
        ]})
        response = client.chat.completions.create(
            model=self.model,
            messages=self.context,
            temperature=self.temperature,
            max_tokens=300
        )
        self.context.append({"role": "assistant", "content":f'{response.choices[0].message.content}'})
        print(f"\n{self.chatbot_name}: {response.choices[0].message.content}")

    def save(self, file_path):
        with open(file_path, "w") as fp:
            fp.write(f"""{{"model": "{self.model}"}}\n"""\
                    f"""{{"custom_instructions": "{self.custom_instructions}"}}\n"""\
                    f"""{{"chatbot_name": "{self.chatbot_name}"}}\n"""\
                    f"""{{"temperature": "{self.temperature}"}}\n""") 
            for message in self.context:
                fp.write("%s\n" % message)
            print(f'\n\nChat history saved at {file_path}')
        with open("path_memory.txt", "r") as memory:
            lines = memory.readlines()
        with open("path_memory.txt", "w") as memory:
            for line in lines:
                if line.strip() != file_path.strip():
                    memory.write(line)
        with open("path_memory.txt", "a") as memory:
            memory.write(file_path + "\n")

# Define bool_yn function
def bool_yn(choice, default=True):
    if choice == '':
        return default
    elif choice.strip()[0].lower() == 'y':
        return True
    elif choice.strip()[0].lower() == 'n':
        return False
    else:
        print("\nInvalid input. Input only 'y' or 'n'.")

# Define offer_presets function
def offer_presets(): 
    while True:
        skip_customization = bool_yn(input("\nSkip customization [y]/n? "))
        if isinstance(skip_customization, bool):
            break  
    return skip_customization

# Define get_file_path function
def get_file_path(existing_path ='', already_exists=False): 
    while True:
        directory = input("\nDirectory (optional): ")
        if directory == '':
            directory = os.getcwd()
            break
        elif os.path.exists(directory):
            break
        else:
            print("\nInput existing directory, or leave blank if current directory.")
    
    while True:
        if already_exists is True:
            filename = input("\nFilename (leave blank if same file): ")
        else:
            filename = input("\nFilename: ")
        if filename != '':
            if '.txt' not in filename:
                filename = filename + ".txt"
            
            file_path = os.path.join(directory, filename)

            if os.path.exists(file_path):
                overwrite = input('\nFile already exists. Do you want to overwrite it y/[n]? ')
                if bool_yn(overwrite, default=False) == True:
                    return file_path 
            else:
                return file_path
        else:
            if already_exists is True:
                return existing_path
            else:
                print("\nFilename is required.")

# Define retrieve_history function
def retrieve_history():
    print("\nHistory of saved chats (from oldest to most recent):")
    i = 1
    for path in history:
        print(f"{i}. {path}")
        i += 1

    while True:
        try:
            if len(history) > 1:
                chosen_history = input(f"\nFile number (1-{len(history)}): ")
            else:
                chosen_history = history[0]
                print("\nMost recent saved chat chosen. No other saved chats available.")
                break
            if chosen_history.strip() == "":
                print("\nMost recent saved chat chosen.")
                chosen_history = history[len(history) - 1]
                break
            else:
                chosen_history = history[int(chosen_history) - 1]
                break
        except:
            print(f"\nPlease input a valid number from 1 to {len(history)}, or leave it blank to use the most recent history.")

    settings = []

    messages = []

    with open(chosen_history, "r") as fp:
        for line in fp.readlines()[0:4]:
            x = ast.literal_eval(line[:-1])
            settings.append(x)
    with open(chosen_history, "r") as fp:
        for line in fp.readlines()[4:]:
            x = ast.literal_eval(line[:-1])
            messages.append(x)

    return settings, messages, chosen_history

# Create models dictionary
models = {
        '1': 'gpt-4-1106-preview',
        '2': 'gpt-4-vision-preview',
        '3': 'gpt-4',
        '4': 'gpt-4-32k',
        '5': 'gpt-3.5-turbo-1106',
        '6': 'gpt-3.5-turbo',
        '7': 'gpt-3.5-turbo-16k'
}

# Give introduction
print("""
=============\n
INTRODUCTION\n
=============\n
Welcome to ConsoleGPT!\n
Here, you can:\n
(1) Design your own GPT-based bot (or just choose the defaults),\n
(2) Chat with it through your terminal, and\n
(3) Save your chat history and settings for next time.\n
\n================\n
DESIGN YOUR BOT\n
================\n
Note: If you want the defaults, just keep pressing <Enter>.\n""")

# Create Chatbot instance
bot = Chatbot()

# Go to part 0 (load history if chosen and offer to skip customization)
print("""------------------------------------\n
(OPTIONAL) PART 0: LOAD CHAT HISTORY\n
------------------------------------""")

while True:
    history_choice = bool_yn(input("\nRetrieve chat history y/[n]? "), default=False)
    if isinstance(history_choice, bool):
        break

if history_choice is True:
    history = []
    with open("path_memory.txt", "r") as fp:
        for line in fp:
            x = line[:-1]
            history.append(x)
    if len(history) != 0:
        settings, context, file_path = retrieve_history()
        bot.model = settings[0]['model']
        bot.custom_instructions = settings[1]['custom_instructions']
        bot.chatbot_name = settings[2]['chatbot_name']
        bot.temperature = float(settings[3]['temperature'])
        bot.context = context
        skip_customization = offer_presets()
    else:
        print("\nNo saved chats found.")
        history_choice = False
        skip_customization = offer_presets()
else:
    print("\nNew chat will be created.")
    skip_customization = offer_presets()

if skip_customization is False:
    # Go to part 1 (choose your model)
    print("""\n-------------------------\n
PART 1: CHOOSE YOUR MODEL\n
-------------------------\n
Choose wisely! Advanced models are more capable but cost more.\n
See https://platform.openai.com/docs/models for more details.\n""")

    # Ask for model number
    print("""The available models are:\n
        1. gpt-4-1106-preview (GPT-4 Turbo)\n
        2. gpt-4-vision-preview (GPT-4 Turbo with vision)\n
        3. gpt-4\n
        4. gpt-4-32k\n
        5. gpt-3.5-turbo-1106 (default if new chat)\n
        6. gpt-3.5-turbo\n
        7. gpt-3.5-turbo-16k\n""")

    while True:
        try:
            model_choice = input("\nModel number (1-7): ")
            if model_choice.strip() == "":
                if history_choice is True:
                    print(f"\nPast model ({bot.model}) kept.")
                else:
                    print(f"\nDefault model ({bot.model}) chosen.")
                break
            else:
                model_choice = int(model_choice)
                bot.model = models[str(model_choice)]
                break
        except (KeyboardInterrupt, EOFError):
            raise
        except:
            print("\nPlease input a valid number from 1 to 7, or leave it blank to use the default.")

    # Go to part 2 (customize your bot)
    print("""\n--------------------------\n
PART 2: CUSTOMIZE YOUR BOT\n
--------------------------\n
If you loaded a history file, the defaults are past parameters.\n""")

    # Ask for custom instructions
    custom_instructions = input("\nCustom instructions (optional): ")

    if custom_instructions.strip() == "":
        print("\n" + bot.custom_instructions)
    else:
        bot.custom_instructions = custom_instructions

    # Ask for chatbot name
    chatbot_name = input("\nChatbot name (optional): ")

    if chatbot_name.strip() == "":
        print("\n" + bot.chatbot_name)
    else:
        bot.chatbot_name = chatbot_name

    # Ask for temperature within valid range
    temperature = -1

    while True:
        temperature = input("\nTemperature [0.0 to 1.0, higher ≈ more creative] (optional): ")
        try:
            if temperature.strip() == "":
                print("\n" + str(bot.temperature))
                break
            elif float(temperature) < 0 or float(temperature) > 1:
                raise ValueError
            else:
                bot.temperature = float(temperature)
                break
        except (KeyboardInterrupt, EOFError):
            raise
        except:
            print("\nInput number within range.")
else:
    if history_choice is True:
        print("\n\n\nLoading previous parameters...\n\n")
    else:
        print("\n\n\nChoosing default parameters...\n\n")

# Go to part 3 (summary of parameters)
print(f"""\n-----------------------------\n
PART 3: SUMMARY OF PARAMETERS\n
-----------------------------\n
Model: {bot.model}\n
Custom instructions: {bot.custom_instructions}\n
Chatbot name: {bot.chatbot_name}\n
Temperature: {bot.temperature}\n
Chat history: {"N/A" if not history_choice else file_path}""")

# Transition to chat proper
print(f"""\n\n====================\n
CHAT WITH {bot.chatbot_name.upper()}\n
====================\n
If you want to end the chat at any point, type \"/end\" then <Enter>.\n""")

if bot.model == "gpt-4-vision-preview":
    print("To upload an image, use \"/img\"; \"/cancel\" to abort.\n")

# Chat until user inputs "/end"
if history_choice is True:
    for message in bot.context[1:]:
        if message['role'] == "user":
            print(f"\nUser: {message['content']}")
        if message['role'] == "assistant":
            print(f"\n{bot.chatbot_name}: {message['content']}")

while True:
    prompt = input("\nUser: ")
    if prompt.strip() == '/img':
        while True:
            url = input("\n    Image URL: ")
            if validators.url(url) is True:
                img_prompt = input("\n    Prompt: ")
                if img_prompt == '/cancel':
                    break
                else:
                    bot.chat_image(img_prompt, url)
                    break
            elif url == '/cancel':
                break
            else:
                print("\n    Enter valid URL.")
    elif prompt.strip() != '/end':
        bot.chat(prompt)
    else:
        break

# Ask to save chat history
print("""\n\n==================\n
SAVE CHAT HISTORY\n
==================""")

while True:
    save_choice = bool_yn(input("\nDo you want to save your chat [y]/n? "))
    if isinstance(save_choice, bool):
        break
    
if save_choice is True and history_choice is False:
    print("\nChat history will be saved as a text file.\n")
    file_path = get_file_path()
    bot.save(file_path)
elif save_choice is True and history_choice is True:
    print("\nChat history will be saved as a text file.\n")
    file_path = get_file_path(file_path, already_exists=True)
    bot.save(file_path)
else:
    print("\n\nChat history will not be saved.")

# Give outro
print("""\n\n===============\n
END OF SESSION\n
===============""")

print(f"\nThanks for chatting with {bot.chatbot_name}!\n")
