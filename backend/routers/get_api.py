from fastapi import APIRouter

router = APIRouter()

@router.get("/get-test")
def get_test():
    return {"message": "你好，這是你的新 API！"}
