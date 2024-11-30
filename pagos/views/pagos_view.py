from fastapi import APIRouter, status, Body
import logic.pagos_logic as pagos_service
from models import Pago, PagoOut, PagoCollection

router = APIRouter()
ENDPOINT_NAME = "/pagos"

@router.get(
    "/",
    response_description="List all pagos",
    response_model=PagoCollection,
    status_code=status.HTTP_200_OK,
)
async def get_places():
    return await pagos_service.get_pagos()

@router.post(
    "/",
    response_description="Create a new pago",
    response_model=PagoOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_place(pago: Pago = Body(...)):
    return await pagos_service.create_pago(pago)
