import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot With OPENAI"



## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant that determines if the user wants to create an Ishikawa diagram."),
        ("user", "Question: {question}")
    ]
)

# Function to generate response using OpenAI API via LangChain
def generate_response(question, api_key, engine, temperature, max_tokens):
    openai.api_key = api_key

    llm = ChatOpenAI(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    intent = answer['choices'][0]['message']['content'].strip().lower()
    return intent


# Title of the app
st.title("Enhanced Q&A Chatbot With OpenAI")

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# Select the OpenAI model
engine = st.sidebar.selectbox("Select OpenAI model", ["gpt-4", "gpt-4-turbo"])

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input and api_key:
    # First, determine if the user wants to create an Ishikawa diagram
    intent = generate_response(user_input, api_key, engine, temperature, max_tokens)

    if intent == "yes":
        # If the intent is to create an Ishikawa diagram, generate a response
        st.write("Generating Ishikawa Diagram...")
    elif intent == "no":
        st.write("Intent is not to create an Ishikawa diagram.")
    else:
        st.write("Error occurred while determining intent.")
elif user_input:
    st.warning("Please enter the OpenAI API Key in the sidebar.")
else:
    st.write("Please provide the user input.")