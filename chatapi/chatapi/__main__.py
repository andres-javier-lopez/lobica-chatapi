import uvicorn

from chatapi.api.app import app

uvicorn.run(app, host="localhost", port=8000)
