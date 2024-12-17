import uvicorn
from fastapi import FastAPI
from api import projects, analysis

app = FastAPI(title="SafeThisSpace Backend")

app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(analysis.router, prefix="/api/projects", tags=["Analysis"])


@app.get("/")
async def root():
    return {"message": "SafeThisSpace Backend is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
