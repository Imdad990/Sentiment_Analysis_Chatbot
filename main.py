import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# API key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize LangChain Chat model with OpenRouter GPT-3.5 Turbo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.7,
)

# Prompt template for sentiment analysis chat
template = """
You are an advanced sentiment analysis assistant. Analyze the user's input text and provide the sentiment as Positive, Negative, or Neutral.
Also, explain your reasoning briefly.

Conversation history:
{history}

User input:
{input}

Sentiment analysis:
"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=template,
)

# Conversation memory to keep track of history
memory = ConversationBufferMemory(memory_key="history")

# Create the LLMChain with prompt and memory
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Streamlit app UI
st.title("🧠 Advanced Sentiment Analysis Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Text input from user
user_input = st.text_input("Enter your message for sentiment analysis:")

if st.button("Send") and user_input:
    # Run the chain with input and conversation history
    response = chain.run(input=user_input)

    # Update session state with messages
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display the conversation
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")

