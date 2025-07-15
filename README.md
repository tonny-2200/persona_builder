


# 🧠 Reddit Persona Builder

**Reddit Persona Builder** is a Python-based script and web application that generates a detailed *persona* of any Reddit user based on their activity. By simply entering a Reddit profile URL, the system analyzes the user's posts and comments to create a personality profile saved as a `.txt` file.

This project includes:

* A **python script** to generate personas
* A **FastAPI web interface** for interactive use
* A **demo video**, **example outputs**, and a **clean UI**

---

## 🚀 Features

* 🔍 Analyze any Reddit user's profile
* 🤖 Generate personality summaries using **Mistral LLM**
* 🌐 Web app built with **FastAPI**
* 📄 Output saved as `.txt` persona files
* 🧠 Powered by **LangChain**, **Mistral API**, and **Reddit API**

---

---

## 🔧 Technologies Used

| Tool/Library    | Purpose                            |
| --------------- | ---------------------------------- |
| **FastAPI**     | Web framework for API and UI       |
| **LangChain**   | Orchestrates prompts and LLM calls |
| **Mistral API** | LLM used for persona generation    |
| **Reddit API**  | Fetches Reddit user data           |
| **dotenv**      | Securely loads API keys            |

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/reddit-persona-builder.git
   cd reddit-persona-builder
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory and add the following:

   ```env
   CLIENT_ID=your_reddit_client_id
   CLIENT_SECRET=your_reddit_client_secret
   MISTRAL_API_KEY=your_mistral_api_key
   ```

4. **Run the app.py:**

   ```bash
   python reddit_persona.py https://www.reddit.com/user/username/
   ```


---

## 🎥 Demo

> A demo video is included in the repo as `demo.mp4`. It showcases the FastAPI web interface and persona generation in action.

---

