"""CurlUp Backend Server Script."""

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.v1.app.database.operations import lifespan
from backend.v1.app.routes import router as router


def create_app() -> FastAPI:
    app = FastAPI(title="CurlUp Backend",
                  version="1.0.0",
                  lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api")

    return app


app = create_app()
