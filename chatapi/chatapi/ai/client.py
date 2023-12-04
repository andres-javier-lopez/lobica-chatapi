from langchain.chat_models import ChatOpenAI

from chatapi.settings import OPENAI_API_KEY


chat_model = ChatOpenAI(api_key=OPENAI_API_KEY)
