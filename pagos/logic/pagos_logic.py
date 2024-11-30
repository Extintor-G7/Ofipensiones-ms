from models import Pago, PagoCollection
from database import places_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException


async def get_pagos():
    """
    Get a list of places
    :return: A list of places
    """
    pagos = await places_collection.find().to_list(1000)
    return PagoCollection(pagos=pagos)


async def create_pago(pago: Pago):
    """
    Insert a new place record.
    """

    try:
        new_pago = await places_collection.insert_one(
            pago.model_dump(by_alias=True, exclude=["id"])
        )
        created_pago = await places_collection.find_one({"_id": new_pago.inserted_id})
        return created_pago

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Place with code {pago.code} already exists"
        )