from flask import Flask, request, jsonify,render_template
import openai
from dotenv import load_dotenv
import os
app = Flask(__name__)   

import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

model_name = "gpt-4o"
deployment = "gpt-4o"

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY") 
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatapi", methods=["POST"])
def chatapi():
    user_input = request.json.get("user_input")
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        max_tokens=4096,
        temperature=0.1,
        top_p=1.0,
        model=deployment
    )
    
    # print( response.choices[0].message.content)   
    return jsonify({"response": response.choices[0].message.content})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)  