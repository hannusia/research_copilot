import os
from dotenv import load_dotenv
import argparse
import configparser
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# read config file
config = configparser.ConfigParser()
config.read("config.ini")
provider = config.get("LLM", "provider")
model = config.get("LLM", "model")
api_key = config.get("LLM", "api_key")

# define search tool
search = DuckDuckGoSearchResults()

tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="Searches information on the internet. Use this when you need to find current or factual information.",
    )
]

# initialize llm model
if provider == "groq":
    llm = ChatGroq(
        temperature=0.7,
        model=model,
        api_key=api_key,
    )
elif provider == "openai":
    llm = ChatOpenAI(temperature=0.7, model=model, api_key=api_key)
else:
    pass

# define prompt
template = """
You are a Researcher based on a large language model that can use tools.
Researcher is designed to be able to find answers to different questions.
As a language model, Researcher is able to generate human-like text based on the input it receives and provide final answer with references ("SOURCES").

Researcher has access to the following tools: {tools}.

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response with sources here]
```

ALWAYS return a "SOURCES" part in your answer. "SOURCES" must be relevant links to websites with information.
Make sure that Final Answer has following structure:
```
[your response here]

Sources:
* [link №1]
* [link №2]
...
```

Begin!

New input: {input}
{agent_scratchpad}
"""

prompt = PromptTemplate(
    input_variables=["agent_scratchpad", "input"],
    partial_variables={
        "tools": [
            "duckduckgo-search: Search DuckDuckGo for results.",
            "answer-with-sources: Use this to answer a question and provide a source link.",
        ],
        "tool_names": ["duckduckgo-search"],
    },
    template=template,
)

# create agent and agent executor
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)


def ask_question(query: str) -> str:
    """
    Ask agent a question
    """
    try:
        response = agent_executor.invoke({"input": query})
        return response.get("output", "Sorry, I couldn't generate a response.")
    except Exception as e:
        return f"An error occurred: {str(e)}"


# parse command line input
parser = argparse.ArgumentParser("research_copilot")
parser.add_argument(
    "query", help="A question you want to find the answer for.", type=str
)
args = parser.parse_args()

print(ask_question(args.query))
