""" 商家端-同意上工 """
import logging
from tools.response_handler import handle_response
from tools.pre_request import fetch_response
from tools.socket_data_manager import SocketDataManager


def e_job_match_accept(base_url):
    """同意上工 API (POST)"""
    socket_manager = SocketDataManager()
    api_url = f"{base_url}/v1/employer/shop/job-match/accept"
    access_token = socket_manager.get_data("E_TOKEN")

    body = {
        "job_sn": socket_manager.get_data("JOB_SN"),
        "labor_id": int(socket_manager.get_data("L_labor_id"))
    }

    try:
        logging.info("📌 測試 API : 120-1")
        response = fetch_response(api_url, access_token, method="POST", data_1=body)
        handle_response(response)
    except Exception as e:
        raise e


if __name__ == "__main__":
    BASE_URL = "https://next-staging-v210x.api.staging.worky.com.tw"
    e_job_match_accept(BASE_URL)
