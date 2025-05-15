import os
import click
import uvicorn


from apps.server import app
from config.env_config import load_dotenv
from config import LoggingConfig

from core.utils import constant_variable

# Routers
from apps.v1.api.role_based_access_control.views.permission_views import router as permission_router
from apps.v1.api.role_based_access_control.views.role_permission_views import router as role_permission_router
from apps.v1.api.role_based_access_control.views.role_views import router as role_router
from apps.v1.api.auth.view import router as auth_router
from apps.v1.api.auth.view import admin_router as admin_router
from apps.v1.api.client.view import router as client_router
from apps.v1.api.staff.view import router as staff_router
from apps.v1.api.event.view import router as event_router
from apps.v1.api.ticket.view import router as ticket_router


load_dotenv()


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prod"], case_sensitive=False),
    default="local",
)
@click.option(
    "--debug",
    type=click.BOOL,
    is_flag=True,
    default=False,
)
def main(env: str, debug: bool):
    os.environ["ENV"] = env
    os.environ["DEBUG"] = str(debug)
    uvicorn.run(
        app="asgi:app",
        host=str(os.environ.get("SERVER_HOST", "localhost")),
        port=int(os.environ.get("SERVER_PORT", 8000)),
        reload=bool(os.environ.get("SERVER_DEBUG", constant_variable.STATUS_FALSE)),
        workers=1,
        log_config=LoggingConfig().get_config(),
    )


# Include all routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(admin_router)
app.include_router(client_router, prefix="/api/v1/client", tags=["Client"])
app.include_router(staff_router,prefix="/api/v1/staff",tags=["Staff"])
app.include_router(role_router)
app.include_router(permission_router)
app.include_router(role_permission_router)
app.include_router(event_router)
app.include_router(ticket_router)


if __name__ == "__main__":
    main()
