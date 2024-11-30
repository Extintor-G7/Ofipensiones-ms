import motor.motor_asyncio
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://localhost:27017"
)
db = client.get_database("ofipensiones_db")
places_collection = db.get_collection("pagos")


async def set_places_db():
    # Creates a unique index on the code field
    await places_collection.create_index("code", unique=True)


# Represents an ObjectId field in the database.
PyObjectId = Annotated[str, BeforeValidator(str)]
