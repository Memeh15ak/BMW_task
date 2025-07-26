from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os

# Load API key from .env (optional)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=GEMINI_API_KEY or "your_gemini_key_here",  # fallback if .env not used
    temperature=0
)

# MS SQL connection string (Trusted Windows Auth)
conn_str = (
    "mssql+pyodbc://MEHAK-PC/BMW_VIN"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Connect to SQL
db = SQLDatabase.from_uri(conn_str)

# Chain: LLM + SQL Agent
chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

# 🔍 Sample Query
query = "Show engine parts for 2023 X5 D M Sport"
result = chain.run(query)

print("\n🔍 QUERY RESULT:")
print(result)
