# research_copilot
Research Copilot is a command-line assistant powered by a large language model and web search tools. It performs web searches using DuckDuckGo, and returns answers with relevant links.

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

# Example
Here is example to illustrate how the program works and results provided by different models.
```
python research_copilot.py "What are seven wonders of the world?"  
```

* `gpt-4.1-mini`
```
There are two commonly referenced lists called the "Seven Wonders of the World":

1. **Seven Wonders of the Ancient World** (classical antiquity):
   - Great Pyramid of Giza (Egypt)
   - Hanging Gardens of Babylon (Iraq, disputed existence)
   - Statue of Zeus at Olympia (Greece)
   - Temple of Artemis at Ephesus (Turkey)
   - Mausoleum at Halicarnassus (Turkey)
   - Colossus of Rhodes (Greece)
   - Lighthouse of Alexandria (Egypt)

These wonders were remarkable constructions known to the ancient Mediterranean world, but only the Great Pyramid of Giza still exists today.

2. **New Seven Wonders of the World** (a modern list from a 2007 global poll organized by the New7Wonders Foundation):
   - Great Wall of China (China)
   - Petra (Jordan)
   - Christ the Redeemer (Brazil)
   - Machu Picchu (Peru)
   - Chichen Itza (Mexico)
   - Roman Colosseum (Italy)
   - Taj Mahal (India)

This modern list was created to represent monuments across different continents and cultures, selected based on worldwide voting.

Sources:
* https://www.britannica.com/topic/Seven-Wonders-of-the-World
* https://www.new7wonders.com/
```
  
* `gemma2-9b-it`
```
The Seven Wonders of the World are often categorized as either ancient or modern.

**Ancient Wonders:** Of the seven ancient wonders, only the Great Pyramid of Giza still stands today.  The others are:

* Hanging Gardens of Babylon
* Statue of Zeus at Olympia
* Temple of Artemis at Ephesus
* Mausoleum at Halicarnassus
* Colossus of Rhodes
* Lighthouse of Alexandria

**Modern Wonders (chosen in 2007 by global poll):**

* Great Wall of China
* Chichén Itzá
* Christ the Redeemer
* Colosseum
* Machu Picchu
* Petra
* Taj Mahal

Sources:
* https://www.thecollector.com/what-are-the-seven-wonders-of-the-world/
* https://www.worldatlas.com/places/7-wonders-of-the-world.html 
* https://www.discovermagazine.com/planet-earth/the-new-7-wonders-of-the-world-and-where-you-can-visit-them
* https://theplanetd.com/wonders-of-the-world/
```

* `llama3-70b-8192`
```
The seven wonders of the ancient world are the Great Pyramid of Giza, the Hanging Gardens of Babylon, the Statue of Zeus at Olympia, the Temple of Artemis at Ephesus, the Mausoleum at Halicarnassus, the Colossus of Rhodes, and the Lighthouse of Alexandria. The seven wonders of the modern world are the Great Wall of China, the Taj Mahal, Machu Picchu, Chichén Itzá, the Roman Colosseum, the Christ the Redeemer statue in Rio de Janeiro, and the Pyramids of Giza.

Sources:
* https://www.thecollector.com/what-are-the-seven-wonders-of-the-world/
* https://www.worldatlas.com/places/7-wonders-of-the-world.html
* https://theplanetd.com/wonders-of-the-world/
* https://www.discovermagazine.com/planet-earth/the-new-7-wonders-of-the-world-and-where-you-can-visit-them
* https://brilliantmaps.com/seven-wonders-of-the-ancient-world/
* https://www.thecollector.com/7-wonders-ancient-world/
``` 
