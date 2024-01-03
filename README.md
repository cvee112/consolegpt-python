# ConsoleGPT (Python)

This is one way to implement a ChatGPT-like interface for your shell/console using Python.

## How to use

**Note**: This assumes you already have Python. Check the [official Python website](https://www.python.org/downloads/) if you don't have it.

0. If you haven't already, setup your OpenAI API key (see [OpenAI's Quickstart tutorial](https://platform.openai.com/docs/quickstart?context=python)). Note that you need to be a pay-as-you-go customer to access GPT-4.

1. Download the [script](chatbot.py) into your preferred location (or clone the repository to your local machine).

2. Open your terminal and navigate to the script directory or repository (e.g., `cd /path/to/script/directory` in Linux/macOS).
   
3. Input `python chatbot.py` to run the chatbot.

## This versus other ConsoleGPTs

When I decided on a name, I didn't realize there were other console versions out there named ConsoleGPT (or Console-GPT), but I stuck with the name despite redundancy as it still felt the most fitting. 

Some features of this implementation that may or may not be shared by other versions:
- The interface is a bit on the structured side in terms of presentation and guidance because of all the `print` statements.
- It provides extra customization --- you can choose between the latest OpenAI models, give custom instructions, specify the model temperature, and even name the chatbot.
- The Python code reflects recent updates in how OpenAI models should be accessed (e.g., you should now be using `chat.completions.create` instead of `ChatCompletion.create`).

Still, it's a work in progress, and I'm sure other versions do certain parts better.

## Questions or feedback?

Feel free to message me (@cvee) through Discord or email me at [cvescobar112@protonmail.com](mailto:cvescobar112@protonmail.com).

## License

This work is licensed under the MIT License. See `LICENSE` for more details.
