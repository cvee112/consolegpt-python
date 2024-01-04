# Sample Runs
This is a compilation of sample runs with ConsoleGPT (Python).

# Sample Run 1 (Defaults)

```
=============

INTRODUCTION

=============

Welcome to ConsoleGPT!

Here, you can:

(1) Design your own GPT-based bot (or just choose the defaults),

(2) Chat with it through your terminal, and

(3) Save your chat history and settings for next time.


================

DESIGN YOUR BOT

================

Note: If you want the defaults, just keep pressing <Enter>.

------------------------------------

(OPTIONAL) PART 0: LOAD CHAT HISTORY

------------------------------------

Retrieve chat history y/[n]? y

No saved chats found.

-------------------------

PART 1: CHOOSE YOUR MODEL

-------------------------

Choose wisely! Advanced models are more capable but cost more.

See https://platform.openai.com/docs/models for more details.

The available models are:

        1. gpt-4-1106-preview (GPT-4 Turbo)

        2. gpt-4-vision-preview (GPT-4 Turbo with vision; pending support)

        3. gpt-4

        4. gpt-4-32k

        5. gpt-3.5-turbo-1106 (default if new chat)

        6. gpt-3.5-turbo

        7. gpt-3.5-turbo-16k


Model number (1-7):  

Default model (gpt-3.5-turbo-1106) chosen.

--------------------------

PART 2: CUSTOMIZE YOUR BOT

--------------------------

If you loaded a history file, the defaults are past parameters.


Custom instructions (optional): 

You are a helpful assistant.

Chatbot name (optional): 

Assistant

Temperature [0.0 to 1.0, higher ≈ more creative] (optional): 

0.7

-----------------------------

PART 3: SUMMARY OF PARAMETERS

-----------------------------

Model: gpt-3.5-turbo-1106

Custom instructions: You are a helpful assistant.

Chatbot name: Assistant

Temperature: 0.7

Chat history: N/A


====================

CHAT WITH ASSISTANT

====================

If you want to end the chat at any point, type "/end" then <Enter>.


User: Hi! How are you? Can you help me out with a coding problem? I need a Python script that transfers screenshots that I took today from my screenshots folder to another folder. Give me a script I can use.        

Assistant: Certainly! Here's a simple Python script that does just that using the `shutil` module to move files from one folder to another:

\```python
import os
import shutil
import datetime

# Define source and destination folders
source_folder = '/path/to/source/screenshots/folder'
destination_folder = '/path/to/destination/folder'

# Get today's date
today = datetime.date.today()

# Iterate through the files in the source folder
for file_name in os.listdir(source_folder):
    # Check if the file was modified today
    file_path = os.path.join(source_folder, file_name)
    modified_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
    if modified_date == today:
        # Move the file to the destination folder
        shutil.move(file_path, destination_folder)
        print(f"Moved {file_name} to {destination_folder}")
\```

Replace `'/path/to/source/screenshots/folder'` and `'/path/to/destination/folder'` with the actual paths to your source and destination folders. When you run this script, it will move all the screenshots you took today from the source folder to the destination folder.

User: /end  


==================

SAVE CHAT HISTORY

==================

Do you want to save your chat [y]/n? 

Chat history will be saved as a text file.


Directory (optional): 

Filename: 

Filename is required.

Filename: hello-world

File already exists. Do you want to overwrite it y/[n]? y


Chat history saved at /Users/cvee/Python/consolegpt/hello-world.txt


===============

END OF SESSION

===============

Thanks for chatting with Assistant!
```

# Sample Run 2 (Loading Previous Chat)

```
=============

INTRODUCTION

=============

Welcome to ConsoleGPT!

Here, you can:

(1) Design your own GPT-based bot (or just choose the defaults),

(2) Chat with it through your terminal, and

(3) Save your chat history and settings for next time.


================

DESIGN YOUR BOT

================

Note: If you want the defaults, just keep pressing <Enter>.

------------------------------------

(OPTIONAL) PART 0: LOAD CHAT HISTORY

------------------------------------

Retrieve chat history y/[n]? y

Note: this overwrites any custom instructions above.

History of saved chats (from oldest to most recent):
1. /Users/cvee/Python/consolegpt/hello-world.txt

Most recent saved chat chosen. No other saved chats available.

-------------------------

PART 1: CHOOSE YOUR MODEL

-------------------------

Choose wisely! Advanced models are more capable but cost more.

See https://platform.openai.com/docs/models for more details.

The available models are:

        1. gpt-4-1106-preview (GPT-4 Turbo)

        2. gpt-4-vision-preview (GPT-4 Turbo with vision; pending support)

        3. gpt-4

        4. gpt-4-32k

        5. gpt-3.5-turbo-1106 (default if new chat)

        6. gpt-3.5-turbo

        7. gpt-3.5-turbo-16k


Model number (1-7): 

Past model (gpt-3.5-turbo-1106) kept.

--------------------------

PART 2: CUSTOMIZE YOUR BOT

--------------------------

If you loaded a history file, the defaults are past parameters.


Custom instructions (optional): 

You are a helpful assistant.

Chatbot name (optional): 

Assistant

Temperature [0.0 to 1.0, higher ≈ more creative] (optional): 

0.7

-----------------------------

PART 3: SUMMARY OF PARAMETERS

-----------------------------

Model: gpt-3.5-turbo-1106

Custom instructions: You are a helpful assistant.

Chatbot name: Assistant

Temperature: 0.7

Chat history: /Users/cvee/Python/consolegpt/hello-world.txt


====================

CHAT WITH ASSISTANT

====================

If you want to end the chat at any point, type "/end" then <Enter>.


User: Hi! How are you? Can you help me out with a coding problem?  I need a Python script that transfers screenshots that I took today from my screenshots folder to another folder. Give me a script I can use.

Assistant: Certainly! Here's a simple Python script that does just that using the `shutil` module to move files from one folder to another:

\```python
import os
import shutil
import datetime

# Define source and destination folders
source_folder = '/path/to/source/screenshots/folder'
destination_folder = '/path/to/destination/folder'

# Get today's date
today = datetime.date.today()

# Iterate through the files in the source folder
for file_name in os.listdir(source_folder):
    # Check if the file was modified today
    file_path = os.path.join(source_folder, file_name)
    modified_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
    if modified_date == today:
        # Move the file to the destination folder
        shutil.move(file_path, destination_folder)
        print(f"Moved {file_name} to {destination_folder}")
\```

Replace `'/path/to/source/screenshots/folder'` and `'/path/to/destination/folder'` with the actual paths to your source and destination folders. When you run this script, it will move all the screenshots you took today from the source folder to the destination folder.

User: Hi, what was my very first message to you?                

Assistant: Your first message to me was "Hi! How are you? Can you help me out with a coding problem?  I need a Python script that transfers screenshots that I took today from my screenshots folder to another folder. Give me a script I can use."

User: /end


==================

SAVE CHAT HISTORY

==================

Do you want to save your chat [y]/n? 

Chat history will be saved as a text file.


Directory (optional): 

Filename (leave blank if same file): 


Chat history saved at /Users/cvee/Python/consolegpt/hello-world.txt


===============

END OF SESSION

===============

Thanks for chatting with Assistant!
```
