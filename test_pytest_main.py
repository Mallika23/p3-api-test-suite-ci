import pytest
from fastapi.testclient import TestClient
from pytest_main import app, todo_items


client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_todo_items():
    print("provide a fresh instance of class and cleans up after the test completes")
    yield
    todo_items.clear()

def test_read_todos_empty():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.parametrize("todo_data", [
    {"id": 1, "title": "groceries", "completed": False},
    {"id": 2, "title": "laundry", "completed": True},
    {"id": 3, "title": "cleaning", "completed": False},  ])
def test_create_todo(todo_data):
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_data

def test_read_todo():
    todo_data = {"id": 1, "title": "groceries", "completed": False}
    client.post("/todos", json=todo_data)
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == todo_data

def mock_test_read_todo(mocker):
    mocker.patch('pytest_main.request.read_todo')
    todo_data = {"id": 1, "title": "groceries", "completed": False}
    mock_read_todo = mocker.patch('pytest_main.request.read_todo')
    mock_read_todo.return_value.status_code = 200
    mock_read_todo.return_value.json.return_value = {"id": 1, "title": "groceries", "completed": False} 
    response = client.read_todo("/todos/1")
    assert response.status_code == 200
    assert response.json() == todo_data
    mock_read_todo.assert_called_once_with("/todos/1")

def test_update_todo():
    todo_data = {"id": 1, "title": "groceries", "completed": False}
    client.post("/todos", json=todo_data)
    updated_todo_data = {"id": 1, "title": "groceries", "completed": True}
    response = client.put("/todos/1", json=updated_todo_data)
    assert response.status_code == 200
    assert response.json() == updated_todo_data

def test_delete_todo():
    todo_data = {"id": 1, "title": "groceries", "completed": False}
    client.post("/todos", json=todo_data)
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == todo_data
    response = client.get("/todos/1")
    assert response.status_code == 404