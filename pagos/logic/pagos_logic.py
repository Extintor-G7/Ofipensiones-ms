from models import Pago, PagoCollection
from database import places_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
import httpx


async def get_pagos():
    """
    Get a list of places
    :return: A list of places
    """
    pagos = await places_collection.find().to_list(1000)
    return PagoCollection(pagos=pagos)


async def create_pago(pago: Pago):
    """
    Insert a new pago record and create a factura in another microservice.
    """
    try:
        # Insert the pago into the MongoDB collection
        new_pago = await places_collection.insert_one(
            pago.model_dump(by_alias=True, exclude=["id"])
        )
        created_pago = await places_collection.find_one({"_id": new_pago.inserted_id})

        # Send a request to create a factura in the Django microservice
        async with httpx.AsyncClient() as client:
            factura_data = {
                "tipo": "Pago",  # Define the correct 'tipo' value here
                "precio": pago.monto,
                "fechaPago": pago.fecha,  # Ensure it's formatted as string
                "idColegio": pago.idColegio,
            }
            response = await client.post("http://127.0.0.1:8002/facturaCreate/", json=factura_data)

            if response.status_code != 200:
                raise HTTPException(status_code=500, detail="Error creating factura")

        return created_pago

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail="Duplicate key error: Pago already exists"
        )

