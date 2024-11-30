import uvicorn
from fastapi import FastAPI
import views
import database


def create_app():
    app = FastAPI(
        docs_url="/pagos/docs",
        openapi_url="/pagos/openapi.json",
        redoc_url=None,
    )

    @app.on_event("startup")
    async def on_startup():
        await database.set_places_db()

    app.include_router(views.router)

    return app


if __name__ == "__main__":
    app = create_app()
    # avoid redirects
    uvicorn.run(app, host="127.0.0.1", port=8080)