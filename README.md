# 🍽️ GenAI Restaurant Name & Menu Generator

Welcome to the AI Restaurant Name & Menu Generator! This is a simple yet powerful web application that leverages the creative power of Generative AI to instantly generate a fancy restaurant name and a list of corresponding menu items based on a selected cuisine.

This project is a perfect demonstration of how to chain multiple Large Language Model (LLM) prompts together to perform a sequential, multi-step task.

---

## ✨ Features

-   **Interactive UI**: A clean and simple user interface built with Streamlit.
-   **Cuisine Selection**: Choose from a variety of cuisines (Indian, Italian, Mexican, American).
-   **Dynamic Generation**: Instantly get a unique, fancy restaurant name.
-   **Context-Aware Menus**: Receive a curated list of menu items that perfectly match the generated restaurant name and selected cuisine.
-   **Powered by LangChain & OpenAI**: Utilizes the latest in LLM technology for creative and relevant suggestions.

---

## 🚀 Core Concepts & Technology

This project is built on a stack designed for rapid AI application development.

-   **[Streamlit](https://streamlit.io/)**: Used to create the interactive web application front-end with just a few lines of Python. It's an open-source framework that turns data scripts into shareable web apps in minutes.

-   **[OpenAI](https://openai.com/)**: The core intelligence behind the application. We use one of OpenAI's powerful LLMs to generate creative text for both the restaurant name and menu items.

-   **[LangChain](https://www.langchain.com/)**: The framework that connects our logic with the OpenAI LLM. LangChain makes it easy to manage prompts, chain them together, and process the model's output.

### How It Works: The `SequentialChain`

The magic of this application lies in the **`SequentialChain`** from LangChain. Instead of making two separate, unrelated calls to the AI, we create a workflow where the output of the first task becomes the input for the second.

1.  **Chain 1: Generate Restaurant Name**
    -   **Input**: A cuisine (e.g., "Italian").
    -   **Prompt**: `"I want to open a restaurant for {cuisine} food. Suggest a fancy name for the same."`
    -   **Output**: A restaurant name (e.g., "The Gilded Olive").

2.  **Chain 2: Generate Menu Items**
    -   **Input**: The restaurant name from Chain 1 (e.g., "The Gilded Olive").
    -   **Prompt**: `"Suggest some menu items for {restaurant_name}. Return it as a comma separated string."`
    -   **Output**: A comma-separated list of menu items.

The `SequentialChain` orchestrates this entire process, ensuring a seamless flow of data from one prompt to the next, resulting in a coherent and contextually relevant final output.

---

## 📂 Project Structure

```
restaurant-name-generator/
│
├── main.py                 # Main Streamlit application script
├── langchain_helper.py     # Core LangChain logic and API calls
├── secret_key.py           # Stores the OpenAI API key
├── requirements.txt        # Project dependencies
└── README.md               # You are here!
```

---

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   An OpenAI API key.

### 2. Clone the Repository

```bash
git clone https://github.com/vrajshah5104/genai-restaurant-name-and-menu-generator.git
cd restaurant-name-generator
```

### 3. Create a Virtual Environment

It's highly recommended to use a virtual environment to keep project dependencies isolated.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

Create a `requirements.txt` file with the following content:

```txt
streamlit
openai
langchain
langchain-openai
```

Then, install the packages:

```bash
pip install -r requirements.txt
```

### 5. Set Up Your API Key

Create a file named `secret_key.py` in the root directory and add your OpenAI API key to it:

```python
# secret_key.py
openapi_key = "sk-YourSecretOpenAI_API_KeyGoesHere"
```
**Important**: Remember to add `secret_key.py` to your `.gitignore` file to prevent your key from being exposed on GitHub!

---

## ▶️ How to Run the Application

With your environment set up and dependencies installed, running the app is as simple as:

```bash
streamlit run main.py
```

Your web browser should automatically open to the application's local URL.

---

## 💡 Future Improvements

This project is a great starting point. Here are a few ideas for taking it to the next level:

-   [ ] **Add More Cuisines**: Expand the list of available cuisines in the sidebar.
-   [ ] **Generate Descriptions**: Add a third chain to generate a short, enticing description for each menu item.
-   [ ] **Include Pricing**: Enhance the menu generation prompt to suggest a price for each item.
-   [ ] **"Surprise Me!" Button**: Add a feature to generate a completely random cuisine and restaurant concept.
-   [ ] **Deploy to Cloud**: Deploy the application using Streamlit Community Cloud, Hugging Face Spaces, or another cloud service to make it publicly accessible.

---

## 🤝 Contact & Acknowledgments

Feel free to connect if you have any questions or suggestions!

-   **GitHub**: https://github.com/vrajshah5104
-   **LinkedIn**: https://www.linkedin.com/in/vraj-nilay-shah

This project was built as a learning exercise in the exciting field of Generative AI. Thanks for checking it out!

---

## License

MIT
