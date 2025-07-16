# Local Fitness AI Agent

A local fitness expert AI that analyzes your workout data and provides personalised advice using open-source LLMs and vector search. All data and models run locally—no cloud required.

## Features

- **Semantic search** over your workout history
- **Personalised fitness advice** powered by Ollama LLMs
- **Vector database** using Chroma for fast retrieval
- **Easy integration** with Hevy app CSV exports
- **Runs entirely on your machine** for privacy and speed

## How It Works

1. **Import your workout data** (CSV from Hevy app)
2. **Vectorise and store** your workouts using Chroma and Ollama embeddings
3. **Ask questions** about your progress, technique, or improvements
4. **Get expert feedback** from a local AI model

## Setup

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
- [Hevy app](https://www.hevy.com/) for workout tracking (optional, for data export)

### Installation

1. Clone this repo:
    ```
    git clone https://github.com/yourusername/local-ai-agent.git
    cd local-ai-agent
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Export your workout data from Hevy as `workouts.csv` and place it in the project folder.

### Usage

1. Start Ollama and make sure the required model (e.g. `llama3.2` and `mxbai-embed-large`) is available.
2. Run the app:
    ```
    python main.py
    ```
3. Ask questions about your workouts, progress, or fitness advice.

## File Structure

- `main.py` — User interface and LLM prompt logic
- `vector.py` — Loads, vectorizes, and retrieves workout data
- `workouts.csv` — Your exported workout data
- `requirements.txt` — Python dependencies

## Example Questions

- *How is my progressive overload working?*
- *Am I getting stronger?*
- *What can I improve and how?*
- *Show me my best bench press sets.*

## Customisation

- Change the LLM model in `main.py` and `vector.py` to use different Ollama models.
- Adjust the number of retrieved workouts in `vector.py` (`search_kwargs={"k": 30}`).

## Privacy

All data and AI models run locally. No data leaves your machine.

## License

MIT License

---

*Built with [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/)

