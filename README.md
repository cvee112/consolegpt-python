# ConsoleGPT (Python)

This is one way to implement a ChatGPT-like interface for your shell/console using Python.

## How to use

**Note**: This assumes you already have Python 3. Check the [official Python website](https://www.python.org/downloads/) if you don't.

0. If you haven't already done so, setup your OpenAI API key (see [OpenAI's Quickstart tutorial](https://platform.openai.com/docs/quickstart?context=python)). Note that you need to be a paying customer to access GPT-4. Also, install the OpenAI Python library and the validators package with `pip install --upgrade openai validators`.

1. Download the [script](chatbot.py) into your preferred location (or clone the repository to your local machine).

2. Open your terminal and navigate to the script directory or repository (e.g., `cd /path/to/script/directory` in Linux/macOS).

4. Input `python chatbot.py` to run the chatbot. See sample runs [here](sample-runs.md).

## This versus other ConsoleGPTs

When I decided on a name, I didn't realize there were other console versions out there named ConsoleGPT (or Console-GPT), but I stuck with the name despite redundancy as it still felt the most fitting. 

Some features of this implementation that may or may not be shared by other versions:
- The interface is on the structured side presentation-wise, mostly because of all the `print` statements.
- You can choose between the latest OpenAI models (assuming you have access), give custom instructions, name the chatbot, specify the model temperature (higher = more creative but less coherent), and save/load chat history files with their settings.
- The Python code reflects recent updates in how OpenAI models should be accessed (e.g., you should now be using `chat.completions.create` instead of `ChatCompletion.create`).

## Questions or feedback?

Feel free to message me (@cvee) through Discord or email me at [cvescobar112@protonmail.com](mailto:cvescobar112@protonmail.com).

## License

This work is licensed under the MIT License. See `LICENSE` for more details.
