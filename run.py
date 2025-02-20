import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  # This tells Uvicorn to run the FastAPI app located in app.main
        host="0.0.0.0",  # Binding to all IP addresses
        port=8001,  # Setting the port
    )
