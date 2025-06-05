from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
import time
from fastapi.background import BackgroundTasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3001'], 
    allow_methods=['*'],
    allow_headers=['*'] 
)

redis=get_redis_connection(
    host="redis-12285.c278.us-east-1-4.ec2.cloud.redislabs.com",
    port=12285,
    password='36A77GBpN7TwQ16HNVi2QlaWD8nIcFye',
    decode_responses=True
)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str #pending, completed, refunded

    class Meta:
        database=redis


@app.get('/orders/{pk}')
def get(pk: str):
    return Order.get(pk)
    
@app.post("/orders")
async def create(request: Request, backgroud_tasks:BackgroundTasks): #id, quantity
    body=await request.json()
    req=requests.get("http://localhost:8000/products/%s" % body['id'])
    product=req.json()

    order=Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2*product['price'],
        total=1.2*product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    backgroud_tasks.add_task(order_completed, order)
    
    return order

def order_completed(order: Order):
    time.sleep(5)
    order.status='completed'
    order.save()
    redis.xadd('order_completed', order.dict(), '*') # auto generated id : '*'




