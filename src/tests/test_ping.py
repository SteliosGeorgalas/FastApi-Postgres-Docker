def test(test_app):
    response = test_app.get("/test")
    assert response.status_code == 200
    assert response.json() == {"test": "success!"}
