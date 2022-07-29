"""
    File to run API
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:FastAPIApplication.get_application", host="localhost", port=8000, reload=True)
