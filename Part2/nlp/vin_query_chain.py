from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GEMINI_API_KEY,
    temperature=0
)

server = "MEHAK-PC"
database = "BMW_VIN"
driver = "ODBC Driver 17 for SQL Server"
conn_str = f"mssql+pyodbc://{server}/{database}?driver={urllib.parse.quote_plus(driver)}&trusted_connection=yes"

try:
    db = SQLDatabase.from_uri(conn_str)
    
    sql_prompt = PromptTemplate(
        input_variables=["input", "table_info", "dialect"],
        template="""Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.

Question: "Question here"
SQLQuery: SELECT ... (without any markdown formatting or code fences)
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:
{table_info}

Question: {input}"""
    )
    
    chain = SQLDatabaseChain.from_llm(
        llm=llm, 
        db=db, 
        verbose=False,
        return_intermediate_steps=False,
        prompt=sql_prompt
    )
    
    query = "Show engine parts for 2023 X5 D M Sport"
    result = chain.invoke({"query": query})
    print(result["result"])

except Exception as e:
    print(f"Error: {e}")