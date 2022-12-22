import json
import os
import sys
import requests

# Read API_TOKEN from the environment
HUGGINGFACE_API_TOKEN = os.environ["HUGGINGFACE_API_TOKEN"]

# See here to get an API token: https://huggingface.co/docs/api-inference/quicktour#get-your-api-token
if HUGGINGFACE_API_TOKEN is None:
    raise ValueError("Please set the HUGGINGFACE_API_TOKEN environment variable. ex: `export HUGGINGFACE_API_TOKEN=hf_XXX`")

# Read filename from the command line arguments
# We try to support most formats (Flac, Wav, Mp3, Ogg etc...). 
# And we automatically rescale the sampling rate to the appropriate rate for the given model (usually 16KHz).
filename = sys.argv[1]

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-small"

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query(filename)

print(data['text'].strip())

