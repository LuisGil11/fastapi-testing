from typing import Union
from fastapi import FastAPI

productos = [
    ["Laptop HP", 750.00, 10],
    ["Smartphone Samsung", 350.00, 20],
    ["Tablet Apple", 499.99, 15],
    ["Monitor Dell", 199.99, 8],
    ["Teclado Logitech", 49.99, 25],
    ["Ratón Microsoft", 29.99, 30],
    ["Impresora Canon", 89.99, 12],
    ["Auriculares Sony", 79.99, 18],
    ["Cámara Nikon", 450.00, 5],
    ["Disco Duro Seagate", 99.99, 22],
    ["Memoria USB Kingston", 19.99, 50],
    ["Router TP-Link", 59.99, 17],
    ["Smartwatch Fitbit", 149.99, 14],
    ["Altavoces Bose", 299.99, 6],
    ["Proyector Epson", 399.99, 7],
    ["Cargador Portátil Anker", 39.99, 28],
    ["Micrófono Blue Yeti", 129.99, 10],
    ["Webcam Logitech", 89.99, 9],
    ["Silla Gamer DXRacer", 299.99, 4],
    ["Mochila Targus", 79.99, 19],
    ["Memoria RAM Corsair", 129.99, 11],
    ["Tarjeta Gráfica NVIDIA", 499.99, 3],
    ["Fuente de Poder EVGA", 59.99, 21],
    ["Monitor ASUS", 179.99, 13],
    ["SSD Samsung", 149.99, 16]
]

app = FastAPI()


@app.get("/products")
def read_root():
    return productos


@app.get("/products/{product_id}")
def get_product(product_id: int):
    if (0 <= product_id < len(productos)):
        return productos[product_id]
    return f'product with id = {product_id} not found.'
