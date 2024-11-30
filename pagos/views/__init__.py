from fastapi import APIRouter

from views import pagos_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(pagos_view.router, prefix=pagos_view.ENDPOINT_NAME)