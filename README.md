# audio2md

## Description

audio2md is a command-line tool that transcribes audio files and generates Markdown files using OpenAI's GPT-3.5 Turbo model. It provides an easy way to convert audio content into text and incorporate it into Markdown documents.

## Installation
> git clone https://github.com/Wa-lead/audio2md.git

> pip install -r requirements.txt

## Usage
1. In terminal type:
   > export OPENAI_API_KEY= < your key >
3. In terminal type:
   > python audio2md.py -f < path to audio file >

### More flags
- -f, --file: Path to audio file
- -o, --output: name of the output file
- -p, --prompt: your prompt to GPT-3 
- -r, --refine: refine your prompt via prompting GPT-3 to refine it.


