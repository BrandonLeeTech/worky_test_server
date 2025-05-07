""" 註冊打工 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
from fastapi import APIRouter
from pydantic import BaseModel
from web import *
from api import *

router = APIRouter()

class TestData(BaseModel):
    base_url: str
    l_phone: str
    l_name: str

@router.post("/build_labor")
def register_labor(data: TestData):
    """
    註冊打工 → 驗證 → 建立 → 檢查驗證 → 審核通過
    """
    try:
        # 1. 打工註冊
        worky_201.l_register(data.base_url, data.l_phone)
        # 2. 驗證碼驗證
        worky_202.l_register_confirm(data.base_url, data.l_phone)
        # 3. 建立打工資料
        worky_205_1.l_update(data.base_url, data.l_name)
        worky_205_2.l_update_preference(data.base_url)
        # 4. 進入後台通過審核
        backend_url = data.base_url.replace("api", "backend", 1)
        labor_verify(backend_url, data.l_phone)

        return {"status": "success", "msg": f"{data.l_name} 打工註冊流程完成 ✅"}

    except Exception as e:
        return {"status": "error", "msg": str(e)}
