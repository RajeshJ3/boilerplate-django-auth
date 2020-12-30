from rest_framework import response, status
from orders import models as orders_models
from organizers import models as organizers_models
from django.db.models import Q

def try_except(func):
    def exe(*args, **kwargs):
        request = args[1]
        try:
            return func(*args, **kwargs)

        except Exception as e:
            output = {
                "description": f"Error while processing {str(request.method)} request",
                "details": str(e)
            }
            return response.Response(output)
    return exe

##############################################
#               Validate Objects             #
##############################################
# def validate_match_entry(func):
#     def check(*args, **kwargs):

#         request = args[1]

#         if request.query_params.get('id', 0):
#             id = request.query_params.get('id', 0)
#         else:
#             id = request.data.get('id', 0)

#         if not id:
#             return response.Response({'details': ['id is not passed']}, status.HTTP_400_BAD_REQUEST)

#         entries = matches_models.MatchEntry.objects.filter(Q(id=id) & Q(is_active=True))

#         if not len(entries):
#             return response.Response({'details': ['Invalid id']}, status.HTTP_400_BAD_REQUEST)

#         kwargs.update({"entry": entries[0]})

#         return func(*args, **kwargs)
        
#     return check

def validate_organizer(func):
    def check(*args, **kwargs):

        request = args[1]

        if request.query_params.get('id', 0):
            id = request.query_params.get('id', 0)
        else:
            id = request.data.get('id', 0)

        if not id:
            return response.Response({'details': ['id is not passed']}, status.HTTP_400_BAD_REQUEST)

        organizers = organizers_models.Organizer.objects.filter(Q(id=id) & Q(is_active=True))

        if not len(organizers):
            return response.Response({'details': ['Invalid id']}, status.HTTP_400_BAD_REQUEST)

        kwargs.update({"organizer": organizers[0]})

        return func(*args, **kwargs)
        
    return check

def validate_paytm(func):
    def check(*args, **kwargs):

        request = args[1]

        if request.query_params.get('id', 0):
            id = request.query_params.get('id', 0)
        else:
            id = request.data.get('id', 0)

        if not id:
            return response.Response({'details': ['id is not passed']}, status.HTTP_400_BAD_REQUEST)

        paytms = organizers_models.PayTm.objects.filter(Q(id=id) & Q(is_active=True))

        if not len(paytms):
            return response.Response({'details': ['Invalid id']}, status.HTTP_400_BAD_REQUEST)

        kwargs.update({"paytm": paytms[0]})

        return func(*args, **kwargs)
        
    return check

def validate_order(func):
    def check(*args, **kwargs):

        request = args[1]

        if request.query_params.get('id', 0):
            id = request.query_params.get('id', 0)
        else:
            id = request.data.get('id', 0)

        if not id:
            return response.Response({'details': ['id is not passed']}, status.HTTP_400_BAD_REQUEST)

        orders = orders_models.Order.objects.filter(Q(id=int(id)) & Q(is_active=True))

        if not len(orders):
            return response.Response({'details': ['Invalid id']}, status.HTTP_400_BAD_REQUEST)

        kwargs.update({"order": orders[0]})

        return func(*args, **kwargs)
        
    return check


##############################################
#               Validate Users               #
##############################################
def validate_organizer_user(func):
    @validate_organizer
    def check(*args, **kwargs):

        request = args[1]
        user = request.user

        organizer = kwargs.get("organizer")

        if organizer.user == user:
            return func(*args, **kwargs)
        
        return response.Response({'details': ['Permission denied, invalid user']}, status.HTTP_400_BAD_REQUEST)

    return check

def validate_paytm_user(func):
    @validate_paytm
    def check(*args, **kwargs):

        request = args[1]
        user = request.user

        paytm = kwargs.get("paytm")

        if paytm.organizer.user == user:
            return func(*args, **kwargs)
        
        return response.Response({'details': ['Permission denied, invalid user']}, status.HTTP_400_BAD_REQUEST)

    return check

def validate_organizer_with_order_id(func):
    @validate_order
    def check(*args, **kwargs):

        request = args[1]
        user = request.user

        order = kwargs.get("order")

        if order.organizer.user == user:
            return func(*args, **kwargs)
        
        return response.Response({'details': ['Permission denied, invalid user']}, status.HTTP_400_BAD_REQUEST)

    return check

def validate_match_entry_player(func):
    @validate_match_entry
    def check(*args, **kwargs):

        request = args[1]
        user = request.user

        entry = kwargs.get("entry")

        if entry.player == user:
            return func(*args, **kwargs)
        
        return response.Response({'details': ['Permission denied, invalid user']}, status.HTTP_400_BAD_REQUEST)

    return check
