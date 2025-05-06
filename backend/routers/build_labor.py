""" 註冊打工 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
from fastapi import APIRouter
from pydantic import BaseModel
from web import *
from api import *
from tools.socket_data_manager import SocketDataManager

router = APIRouter()

class TestData(BaseModel):
    base_url: str
    l_phone: str
    l_name: str

@router.post("/build_labor")
def register_and_validation(data: TestData):
    """
    註冊打工 → 驗證 → 建立 → 檢查驗證 → 審核通過
    """
    socket_data = SocketDataManager()
    try:
        # 1. 打工註冊
        worky_201.l_register(data.base_url, data.l_phone)
        # 2. 驗證碼驗證
        worky_202.l_register_confirm(data.base_url, data.l_phone)
        # 3. 建立打工資料
        worky_303_l.upload_l(data.base_url, "labor_profile_image", "labor_1")
        img = socket_data.get_data("labor_1")
        worky_205_1.l_update(img, data.l_name)
        worky_205_2.l_update_preference(data.base_url)
        # 4. 進入後台通過審核
        backend_url = data.base_url.replace("api", "backend", 1)
        labor_verify(backend_url, data.l_phone)

        return {"status": "success", "msg": f"{data.l_name} 打工註冊流程完成 ✅"}

    except Exception as e:
        return {"status": "error", "msg": str(e)}
