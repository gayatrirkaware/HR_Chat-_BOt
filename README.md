# HR_Chat-_BOt

---

```markdown
# Azure OpenAI Chatbot (Flask UI)

This project demonstrates a simple chatbot web interface built with **Flask** and connected to **Azure OpenAI (GPT-4o)** using the `openai` Python SDK. The frontend is written in basic HTML/CSS/JavaScript and interacts with a REST API endpoint for chat completion.

---

## 📁 Project Structure

```

project/
│
├── app.py                 # Flask backend with Azure OpenAI integration
├── .env                   # Environment variables (not committed to Git)
├── templates/
│   └── index.html         # HTML frontend UI
└── README.md              # Project documentation

````

---

## 🔧 Requirements

- Python 3.8+
- Azure OpenAI resource (endpoint + key)
- Dependencies:
  - `flask`
  - `openai`
  - `python-dotenv`

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <project-directory>
````

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory with the following:

   ```env
   AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
   AZURE_OPENAI_KEY=<your-azure-openai-key>
   AZURE_API_VERSION=2024-05-01-preview
   ```

---

## 🚀 Run the Application

```bash
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 📬 API Endpoint

### `POST /chatapi`

**Request JSON:**

```json
{
  "user_input": "Tell me a joke."
}
```

**Response JSON:**

```json
{
  "response": "Why did the chicken join a band? Because it had the drumsticks!"
}
```

---

## 💻 Frontend Features

* Textarea for user input
* Send button to submit message
* Displays response from the chatbot
* Styled with minimal CSS for simplicity

---



