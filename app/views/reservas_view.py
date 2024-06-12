def render_reservas_list(reservarants):
    return [
        {
            "id":reserva.id,
            "user_id":reserva.user_id,
            "restaurant_id":reserva.restaurant_id,
            "reservation_date":reserva.reservation_id,
            "num_guests":reserva.num_guests,
            "special_requests":reserva.desc,
            "status":reserva.status,
        }
        for reserva in reservarants
    ]
    
def render_reserva_detail(reserva):
    return {
            "id":reserva.id,
            "user_id":reserva.user_id,
            "restaurant_id":reserva.restaurant_id,
            "reservation_date":reserva.reservation_id,
            "num_guests":reserva.num_guests,
            "special_requests":reserva.desc,
            "status":reserva.status,
        }