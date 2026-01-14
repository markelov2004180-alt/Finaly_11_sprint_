# Маркелов Виталя, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

track_number = sender_stand_request.response_data["track"]

def test_create_number():
    response = sender_stand_request.get_track_orders(track_number)
    assert response.status_code == 200