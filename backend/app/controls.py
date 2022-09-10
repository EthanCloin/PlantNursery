"""entry point for running server"""
import uvicorn


def start_server():
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
    
if __name__ == '__main__':
    start_server()
        