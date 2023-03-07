import openai
import csv

# Set up OpenAI API key
openai.api_key = ""

# Load the CSV file
with open('vulnerabilities.csv', 'r', encoding='cp1252') as file:
    reader = csv.reader(file)
    vulnerabilities = [row for row in reader]

# Define the prompt for GPT-3 to prioritize vulnerabilities
prompt = (f"Prioritize the following {len(vulnerabilities)} vulnerabilities:\n" 
          f"{', '.join([', '.join(row) for row in vulnerabilities])}")

# Set up the GPT-3 engine and parameters. 
# Temperature controls randomness or "creativity" in the generated text. Higher temperatures result in more diverse and unpredictable output. Conversely, lower temperatures result in more conservative and predictable output. 
# Tokens are the words
model_engine = "text-davinci-002"
temperature = 0.5
max_tokens = 60

# Generate the prioritized list of vulnerabilities using GPT-3
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    timeout=15,
)

# Print the prioritized list of vulnerabilities
print(response.choices[0].text.strip())
