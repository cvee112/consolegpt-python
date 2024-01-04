# Sample Runs
This is a compilation of sample runs with ConsoleGPT (Python).

# Sample Run 1 (Defaults)

`````
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

```python
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
```

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
`````

# Sample Run 2 (Loading Past Chat)

`````
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

```python
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
```

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
`````

# Sample Run 3 (Customized: GPT-4 Turbo)

`````
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

Retrieve chat history y/[n]? 

New chat will be created.

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


Model number (1-7): 1

--------------------------

PART 2: CUSTOMIZE YOUR BOT

--------------------------

If you loaded a history file, the defaults are past parameters.


Custom instructions (optional): You are an expert Python coder who specializes in writing Python scripts requested by beginner coders. You ask questions when the request is unclear, and you explain at a beginner's level. Assume that all users making requests are beginners unless specified by the user to be otherwise.

Chatbot name (optional): PythonTutor

Temperature [0.0 to 1.0, higher ≈ more creative] (optional): 0.5

-----------------------------

PART 3: SUMMARY OF PARAMETERS

-----------------------------

Model: gpt-4-1106-preview

Custom instructions: You are an expert Python coder who specializes in writing Python scripts requested by beginner coders. You ask questions when  the request is unclear, and you explain at a beginner's level. Assume that all users making requests are beginners unless specified by the user to be otherwise.

Chatbot name: PythonTutor

Temperature: 0.5

Chat history: N/A


====================

CHAT WITH PYTHONTUTOR

====================

If you want to end the chat at any point, type "/end" then <Enter>.


User: Hi! How are you? Can you help me out with a coding problem? I need a Python script that transfers screenshots that I took today from my screenshots folder to another folder. Give me a script I can use.   

PythonTutor: Hello! I'm here to help you with your coding problem.

To create a Python script that moves today's screenshots from one folder to another, we need to:

1. Identify the screenshots folder.
2. Find out the destination folder where you want to transfer the screenshots.
3. Determine the format or naming convention of the screenshots (e.g., PNG, JPG, and how the filenames are structured).
4. Filter out the files based on today's date.
5. Move the files.

Here's a simple script that should do the job. Before running the script, make sure to replace `source_folder` and `destination_folder` with the actual paths to your folders. Also, ensure that the script has the correct permissions to read from the source folder and write to the destination folder.

```python
import os
import shutil
from datetime import datetime

# Replace these with your actual folder paths
source_folder = '/path/to/your/screenshots/folder'
destination_folder = '/path/to/your/destination/folder'

# Get today's date in the format that matches your screenshot filenames
today = datetime.now().strftime('%Y-%m-%d')

# List all files in the source folder
files = os.listdir(source_folder)

# Loop through all files
for file_name in files:
    # Construct full file path
    file_path = os.path.join(source_folder, file_name)
    
    # Check if the file is a screenshot taken today
    # This assumes your screenshots are named with the date in 'YYYY-MM-DD' format
    # Update the condition to match your screenshot naming convention
    if today in file_name and os.path.isfile(file_path):
        # Construct the destination file path
        destination_path = os.path.join(destination_folder, file_name)
        
        # Move the screenshot to the destination folder
        shutil.move(file_path, destination_path)
        print(f'Moved: {file_name}')

print('Done! All of today\'s screenshots have been moved.')
```

Make sure to run this script on the same day you took the screenshots, as it filters files based on the current date.

Remember to replace the date format in `today = datetime.now().strftime('%Y-%m-%d')` with the one that matches how the date is included in your screenshot filenames if it's different. This script assumes that the date is part of the filename.

If you have any questions or need further customization, feel free to ask!

User: /end


==================

SAVE CHAT HISTORY

==================

Do you want to save your chat [y]/n? 

Chat history will be saved as a text file.


Directory (optional): 

Filename: pythontutor


Chat history saved at /Users/cvee/Python/consolegpt/pythontutor.txt


===============

END OF SESSION

===============

Thanks for chatting with PythonTutor!
`````
