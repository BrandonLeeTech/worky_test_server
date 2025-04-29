""" 商家端-通知打下班碼 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_send_end_code(base_url, job_sn):
    """打下班碼 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/labor/send-end-code"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "job_sn": str(job_sn),
        "labor_id": int(socket_manager.get_data("L_labor_id"))
    }

    try:
        logging.info("📌 測試 API : 123")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e
