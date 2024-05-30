from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from main import app, productos
# import pytest

client = TestClient(app)

def test_get_all_products_route():
    response = client.get("/products")
    assert response.status_code == 200

def test_get_one_product_route():
    response = client.get("/products/0")
    assert response.status_code == 200

def test_get_all_products():
    response = client.get("/products")
    assert response.json() == productos

def test_get_one_product():
    response = client.get("/products/0")
    assert response.json() == ["Laptop HP", 750.00, 10]

def test_product_not_found():
    response = client.get("/products/100")
    assert response.json() == 'product with id = 100 not found.'