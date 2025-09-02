"""
Haochen Liu
hliu0010
540243105
"""
from service.service_1 import open_database
from service.service_2 import purchase_vip
from service.service_3 import statistics
from service.service_4 import rankings
from service.service_5 import comparing

def service(user: list, opt :int):
    """
    Execute the service corresponding to the selected option.
    """
    if opt == 1:
        open_database(user)
    elif opt == 2:
        purchase_vip(user)
    elif opt == 3:
        statistics(user)
    elif opt == 4:
        rankings(user)
    elif opt == 5:
        comparing(user)
    
if __name__ == "__main__":
    service()
