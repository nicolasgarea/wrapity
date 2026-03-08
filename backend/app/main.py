from fastapi import FastAPI

app = FastAPI(
    title="Wrapity",
    description="Music-based social network API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Wrapity API is running"}