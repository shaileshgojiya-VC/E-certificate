import logging

from fastapi import Depends, FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
#from apps.api.v1.RBAC.middleware import RBACMiddleware



# from core.config import config
from config import LoggingConfig
from core import CustomException
from core.utils import constant_variable
#from middleware import S3PathMiddleware

# from apps.api.api.client.view import router as client_router
# from apps.api.api.role.view import router as role_router
# from apps.api.api.permission.view import router as permission_router
#from apps.api.v1.role.view import router as role_router



def init_routers(app_: FastAPI) -> None:
    pass
    # app_.include_router(user_router)
    # app_.include_router(client_router,prefix="/api/v1")
    #app_.include_router(role_router,prefix="/api/v1")
    # app_.include_router(permission_router,prefix="/api/v1")


def init_listeners(app_: FastAPI) -> None:
    # Exception handler
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        content = {"status": exc.status, "data": exc.data, "message": exc.message}
        return JSONResponse(
            status_code=exc.status,
            content=content,
        )

"""
def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=constant_variable.STATUS_TRUE,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        #Middleware(
            #S3PathMiddleware, config_path=f"{project_path.S3_ROOT}/s3_paths_config.json"
        #),
    ]
    return middleware
"""
def make_middleware() -> list:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=constant_variable.STATUS_TRUE,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        #Middleware(RBACMiddleware),
        # If you uncomment this, make sure you pass the correct class and parameters:
        # Middleware(S3PathMiddleware, config_path=f"{project_path.S3_ROOT}/s3_paths_config.json")
    ]
    return middleware

# TODO: Redis Cache Implement


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Eventify",
        description="Beyond Events – We Build Experiences That Last",
        version="1.0.0",
        redoc_url=None,
#        redoc_url="/redoc"
        #docs_url=None if config.ENV == "production" else "/docs",
        #redoc_url=None if config.ENV == "production" else "/redoc",
        dependencies=[Depends(LoggingConfig().get_config)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    # init_cache() # Redis Cache Implement
    return app_


app = create_app()
@app.get("/redoc", include_in_schema=False)
async def custom_redoc():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Event Ticketing API Docs</title>
        <link rel="icon" href="/static/logo.png" />
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #f0f4ff, #ffffff);
                color: #333;
            }

            .header {
                display: flex;
                align-items: center;
                padding: 2rem;
                background-color: #ffffff;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }

            .header img {
                height: 60px;
                margin-right: 20px;
            }

            .header-text h1 {
                margin: 0;
                font-size: 28px;
                color: #2c3e50;
            }

            .tagline {
                margin-top: 4px;
                font-size: 16px;
                color: #7f8c8d;
            }

            .redoc-wrapper {
                margin-top: 0;
                padding: 0;
            }

            redoc {
                display: block;
                height: 100vh;
            }

            @media (max-width: 768px) {
                .header {
                    flex-direction: column;
                    align-items: flex-start;
                }
                .header-text h1 {
                    font-size: 24px;
                }
                .tagline {
                    font-size: 14px;
                }
            }
        </style>
    </head>
    <body>
        <div class="header">
            <img src="/static/logo.png" alt="App Logo">
            <div class="header-text">
                <h1>Event Ticketing API</h1>
                <div class="tagline">Beyond Events – We Build Experiences That Last</div>
            </div>
        </div>
        <div class="redoc-wrapper">
            <redoc spec-url="/openapi.json"></redoc>
        </div>
        <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"> </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)
logger = logging.getLogger(__name__)
