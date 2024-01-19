from app import app 


def test_ping_endpoint() -> None:
    client = app.test_client()
    actual = client.get("/ping")