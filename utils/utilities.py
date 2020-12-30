from django.conf import settings
from discounts import models as discounts_models

def calculate_total_cost(qty: int, discount: discounts_models.Code = None) -> float:
    cost_dict = settings.COSTS
    
    for key, val in cost_dict.items():
        if qty >= key:
            cost_per_item = round(val/key, 2)
            break

    total = qty * cost_per_item

    if discount:
        total -= discount.amount if discount.amount >=1 else 0
        
    return round(total, 2)

def pop_from_data(pop_list, data):
    for _ in pop_list:
        if _ in data:
            data.pop(_)
    return data