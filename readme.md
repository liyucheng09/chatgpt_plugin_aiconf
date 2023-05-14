# ChatGPT Plugin - AI Conference Assistant

This is an example of ChatGPT plugin that allows ChatGPT to access information of upcoming AI conferences and allow users to star target conference and ask ChatGPT to provide an decent to-do plan.

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "Show me the 5 most recent AI conference." or "What are the upcoming NLP conferences?" 

You can also ask ChatGPT to star your target conference and provide a to-do list considering its submission deadline.