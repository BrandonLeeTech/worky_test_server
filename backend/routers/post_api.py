from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TestData(BaseModel):
    username: str

@router.post("/post-test")
async def post_test(data: TestData):
    result = f"用戶 {data.username} 執行測試！"
    return {"status": "success", "result": result}
