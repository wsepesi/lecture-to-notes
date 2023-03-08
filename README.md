# lecture-to-notes

Programmatic workflow to convert a recorded lecture to summarized notes, using Whisper, GPT3, and Langchain.

## Requirements

conda env with the following installed:\
- ffmpeg\
- openai\
- pydub\
- dotenv\

## Setup

Place your OpenAI API key in a `.env` file in the root directory, with the following format:\
`OAI_KEY = 'your-key-here'`

## Usage

`run.py` is the main script, taking an optional argument for the path to the lecture audio file. If not provided, it will instead sweep the `data/audio` directory for all previously untranscribed audio files.

This script operates on two modules, a `Transcriber` and a `Summarizer`, which can be exchanged for other implementations, seen in the project repo. This defaults to the `Naive` implementations.

## Current Transcribers

`Naive` - Uses OAI `whisper-1`, which uses the large-v2 model. By default the target language in the repo is French

## Current Summarizers

`Naive` - Splits the content by pages, then uses OAI `gpt-3.5-turbo` endpoint to summarize each page. Executive summary produced from a summary of those pages. The language remains in the target language.

## TODO:

- Support flags to specifiy transcriber and summarizer
- Support flag to target different languages
- Develop more advanced summarizer and transcriber