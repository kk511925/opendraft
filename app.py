import sys
import os

# 关键：把 engine 目录加入 Python 搜索路径，解决所有内部导入问题
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'engine'))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine.draft_generator import DraftGenerator
import uvicorn

app = FastAPI(title="OpenDraft API")

class DraftRequest(BaseModel):
    topic: str
    paper_type: str = "master"
    language: str = "en"

class DraftResponse(BaseModel):
    content: str

@app.post("/generate")
def generate_draft(req: DraftRequest):
    try:
        generator = DraftGenerator()
        draft = generator.generate(
            topic=req.topic,
            paper_type=req.paper_type,
            language=req.language
        )
        return DraftResponse(content=str(draft))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
