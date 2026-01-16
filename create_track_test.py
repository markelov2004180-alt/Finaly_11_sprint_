# Маркелов Виталя, 39-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_number():

    order_response = sender_stand_request.post_new_orders()
    order_data = order_response.json()
    track_number = order_data["track"]
    
    response = sender_stand_request.get_track_orders(track_number)
    assert response.status_code == 200


