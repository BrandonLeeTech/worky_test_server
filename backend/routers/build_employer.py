""" 註冊商家 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
from fastapi import APIRouter
from pydantic import BaseModel
from web import *
from api import *

router = APIRouter()

class TestData(BaseModel):
    base_url: str
    e_phone: str
    e_name: str

@router.post("/build_employer")
def register_and_validation(data: TestData):
    """
    註冊商家 → 驗證 → 建立 → 檢查驗證 → 審核通過
    """
    try:
        # 1. 商家註冊
        worky_101.e_register(data.base_url, data.e_phone)
        # 2. 驗證碼驗證
        worky_102.e_register_confirm(data.base_url, data.e_phone)
        # 3. 建立商家資料
        worky_105_1.e_shop_create(data.base_url, data.e_name)
        # 4. 商家驗證查詢
        worky_105_3.e_shop_validation_request(data.base_url, data.e_name)
        # 5. 進入後台通過審核
        backend_url = data.base_url.replace("api", "backend", 1)
        shop_audit_passed_h(backend_url, data.e_phone)

        return {"status": "success", "msg": f"{data.e_name} 商家註冊流程完成 ✅"}

    except Exception as e:
        return {"status": "error", "msg": str(e)}
