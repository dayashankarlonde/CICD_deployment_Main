from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert "Backend working successfully" in response.get_data(as_text=True)

def test_data():
    client = app.test_client()
    response = client.get("/api/data")

    assert response.status_code == 200
    data = response.get_json()

    assert isinstance(data, list)
    assert data[0]["name"] == "Aman"