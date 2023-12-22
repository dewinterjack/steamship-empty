from steamship.agents.functional import FunctionsBasedAgent
from steamship.agents.llms.openai import ChatOpenAI
from steamship.agents.service.agent_service import AgentService

SYSTEM_PROMPT = """You are Assistant, an assistant who helps the user in any way you can.

Who you are:
- You are a helpful robot
- You are kind and compassionate

Only use the functions you have been provided with."""

MODEL_NAME = "gpt-4-0613"
 
class MyAssistant(AgentService):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        agent = FunctionsBasedAgent(llm=ChatOpenAI(self.client, model_name=MODEL_NAME), tools=[])
        agent.PROMPT = SYSTEM_PROMPT
        self.set_default_agent(agent)