import uvicorn

uvicorn.run("chatapi.api.app:app", host="localhost", port=8000, reload=True)
