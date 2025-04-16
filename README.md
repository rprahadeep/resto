## Restaurant Name and Menu Generator

This is a simple Python project that uses **LangChain** and **Gemini 2.0** by Google Generative AI to:

- Generate a restaurant name based on a given cuisine
- Generate 10 matching menu items for that restaurant

---

### Technologies Used

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![LangChain](https://img.shields.io/badge/LangChain-%23008CFF.svg?style=for-the-badge&logo=LangChain&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

### How It Works

The app uses a two-step chain:

1. **Restaurant Name Generator** – Based on the cuisine, it asks Gemini to suggest a restaurant name.
2. **Menu Items Generator** – Using the generated restaurant name, it asks Gemini for 10 menu items.

---

### Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/rprahadeep/resto.git
   cd restaurant-generator
2. **Install dependencies:**
    ```bash
   pip install langchain langchain-google-genai
   pip install streamlit
3. **Create a file named secret_key.py:**
   ```bash
   gemini_api = "your_api_key_here"
4. **Run the app:**
   ```bash
   streamlit run main.py
