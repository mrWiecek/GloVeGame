import motor.motor_asyncio

# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://root:rootpassword@src_mongodb_1/samples?retryWrites=true&w=majority&authSource=admin')
# client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:rootpassword@localhost:27017')
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:rootpassword@mongo:27017')
db = client.samples

analogies_collection = db.get_collection("analogiess_collection")