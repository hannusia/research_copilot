# research_copilot

# Installation
Clone repository with code
```
git clone https://github.com/hannusia/research_copilot.git
cd research_copilot
```

Install requirements, it's recommended to use virtual enviroment
```
python -m venv env
. ./env/bin/activate
pip install -r requirements.txt
```

# Configuration
Before running the program, you need to configure the language model and agent settings.
To do this edit `config.ini` file:
* select model provider: `openai` or `groq`
* select model (e.g., `gpt-4.1-mini`, `llama3-8b-8192`, etc.)
* add your API key for the selected provider
* set `verbose` to `True` if you want to see detailed agent output

# Usage
Run command-line python program with your question
```
python research_copilot.py "query"
```
