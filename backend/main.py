from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import *

app = FastAPI()


# 加入 CORS 中介層解決跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 掛載模組化路由
app.include_router(get_api.router)
app.include_router(post_api.router)
app.include_router(build_employer.router)
app.include_router(build_labor.router)
app.include_router(set_account.router)

# 預設轉跳到 /docs
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
