# Sentiment_Analysis_Chatbot
# 🧠 Advanced Sentiment Analysis Chatbot


An intelligent and conversational **Sentiment Analysis Chatbot** built using **LangChain**, **OpenRouter (GPT-3.5 Turbo)**, and **Streamlit**. It analyzes user input in real-time and provides sentiment as **Positive**, **Negative**, or **Neutral**, along with a brief reasoning.

---

## 🚀 Live Demo

> 🎯 Coming Soon!  
> You can run the app locally by following the steps below.

---

## 🌟 Features

- 💬 Real-time sentiment analysis through a conversational interface
- 🧠 Remembers conversation context using memory
- 🧾 Detailed reasoning for every sentiment classification
- 🌐 Uses OpenRouter GPT-3.5-turbo via LangChain
- 🛠 Built with Python + Streamlit UI

---

## 🖥️ Screenshot

![sentiment](https://github.com/user-attachments/assets/bede0e0e-ca51-4ce3-8392-365ae5bfe4dc)

---

## 🧰 Technologies Used

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenRouter GPT-3.5-turbo](https://openrouter.ai/)
- [Dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔧 Setup Instructions

### 1. Clone the Repository


git clone https://github.com/yourusername/sentiment-analysis-chatbot.git
cd sentiment-analysis-chatbot
2. Create & Activate Virtual Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root directory and add your OpenRouter API key:

OPENROUTER_API_KEY=your_openrouter_api_key_here
5. Run the App
streamlit run app.py
📂 Project Structure
📦sentiment-analysis-chatbot
 ┣ 📄app.py
 ┣ 📄.env
 ┣ 📄requirements.txt
 ┗ 📄README.md
🧠 How It Works
The chatbot uses a custom LangChain prompt template to:

Track conversation history

Accept user input

Respond with a sentiment analysis (Positive, Negative, Neutral)

Justify its decision in human-readable format

Memory is managed using ConversationBufferMemory for natural, flowing conversations.

💡 Future Improvements
Add emoji-based sentiment visualization 😊 😐 😠

Streamlit chat-style interface with st.chat_message

Export chat history to PDF

Deploy on HuggingFace or Streamlit Cloud

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

📝 License
This project is open-source and available under the MIT License.

🙋‍♂️ Author
Imdad Ullah Khan
“Building intelligent solutions using AI & ML.”
📬 Contact me | 🌐 LinkedIn


### ⚙️ Bonus: `requirements.txt`
streamlit
langchain
openai
python-dotenv
