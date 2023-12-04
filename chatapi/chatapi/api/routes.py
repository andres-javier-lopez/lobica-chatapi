from langserve import add_routes

from chatapi.ai.assistant import chain
from chatapi.api.app import app


add_routes(app, chain, path="/assistant")
