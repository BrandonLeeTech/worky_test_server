""" 商家帳務設定 """

# pylint: disable = [unused-wildcard-import], [wildcard-import]
from fastapi import APIRouter
from pydantic import BaseModel
from web import *
from api import *

router = APIRouter()

class TestData(BaseModel):
    base_url: str
    e_phone: str

@router.post("/set_account")
def setting_employer_account(data: TestData):
    """
    登入商家 → 信用卡網址 → 設定發票 → 設定退款帳戶 → 開啟金流 web 設定
    """
    try:
        # 1. 登入商家
        worky_103.e_login(data.base_url, data.e_phone)
        # 2. 驗證碼驗證
        worky_104.e_login_confirm(data.base_url, data.e_phone)
        # 3. 信用卡網址
        worky_161.e_credit_card_bind(data.base_url)
        # 4. 設定發票
        worky_171.e_invoice_update(data.base_url)
        # 5. 設定退款帳戶
        worky_173.e_bank_account_update(data.base_url)
        # 6. 開啟金流 web 設定
        credit_card_bind()

        return {"status": "success", "msg": f"{data.e_phone} 商家設定帳務流程完成 ✅"}

    except Exception as e:
        return {"status": "error", "msg": str(e)}
