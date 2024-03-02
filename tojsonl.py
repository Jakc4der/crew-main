import requests
from openai import OpenAI

client = OpenAI(api_key="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")
import json

# Set your OpenAI API key here

# Function to fetch the web page content
def fetch_web_page_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
    return response.text

# Function to process the content with OpenAI (placeholder, adjust as needed)
def process_content_with_openai(content):
    # Example: Extract or summarize the text using OpenAI's API
    # This is a placeholder; you may want to use specific models or parameters
    response = client.completions.create(engine="gpt-3.5-turbo-0125",
    prompt="Summarize the following text:\n\n" + content,
    max_tokens=100)
    return response.choices[0].text.strip()

# Function to convert to JSONL format and save to a file
def save_to_jsonl(data, filename="output.jsonl"):
    with open(filename, 'w') as f:
        for item in data:
            json_record = json.dumps(item, ensure_ascii=False)
            f.write(json_record + "\n")

# Main function to run the process
def main(url):
    content = fetch_web_page_content(url)
    processed_content = process_content_with_openai(content)
    # Assuming the processed content is a simple text, convert it into a list of dicts for JSONL
    data = [{"text": processed_content}]
    save_to_jsonl(data)

# Replace 'url_to_process' with the actual URL you want to process
url_to_process = "https://example.com"
main(url_to_process)