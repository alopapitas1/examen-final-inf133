def render_restau_list(restaurants):
    return [
        {
            "id":restau.id,
            "name":restau.name,
            "adress":restau.adress,
            "city":restau.city,
            "phone":restau.phone,
            "desc":restau.desc,
            "rating":restau.rating,
        }
        for restau in restaurants
    ]
    
def render_restau_detail(restau):
    return {
            "id":restau.id,
            "name":restau.name,
            "adress":restau.adress,
            "city":restau.city,
            "phone":restau.phone,
            "desc":restau.desc,
            "rating":restau.rating,
        }