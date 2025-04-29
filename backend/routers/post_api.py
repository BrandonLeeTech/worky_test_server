from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TestData(BaseModel):
    username: str
    test_type: str

@router.post("/post-test")
async def post_test(data: TestData):
    result = f"用戶 {data.username} 執行了 {data.test_type} 測試！"
    return {"status": "success", "result": result}