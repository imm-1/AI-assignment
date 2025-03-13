from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from config import MODEL_ID, OLLAMA_SERVER

class AIResult(BaseModel):
    output: str

model_instance = OpenAIModel(
    model_name=MODEL_ID, provider=OpenAIProvider(base_url=OLLAMA_SERVER)
)

csv_helper = Agent(
    model=model_instance,
    result_type=AIResult,
    system_prompt="You are an AI assistant specializing in CSV data analysis. Help users extract insights and answer queries effectively."
)
