from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from tools.vin_decoder import decode_vin
from tools.cost_estimator import estimate_cost
from tools.price_trend import price_trend_summary

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = [
    Tool(name="VIN Decoder", func=decode_vin, description="Decode a BMW VIN"),
    Tool(name="Repair Cost", func=lambda x: estimate_cost(eval(x)['parts'], eval(x)['region']),
         description="Estimate cost from parts and region"),
    Tool(name="Price Trend", func=price_trend_summary, description="Get price trend for a part ID"),
]

agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)
