from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from main import app, usuarios
# import pytest

client = TestClient(app)

def test_get_all_users_route():
    response = client.get("/users")
    assert response.status_code == 200

def test_get_one_user_route():
    response = client.get("/users/0")
    assert response.status_code == 200

def test_get_all_users():
    response = client.get("/users")
    assert response.json() == usuarios

def test_get_one_user():
    response = client.get("/users/0")
    assert response.json() == ["Pedro Perez", 28, "pperez@prueba.com"]

def test_user_not_found():
    response = client.get("/users/100")
    assert response.json() == 'user with id = 100 not found.'