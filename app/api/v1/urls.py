from app.api.v1 import api as api_v1
from app.api.v1.repositories.factoriel import calculate_factorial_interface

api_v1.add_url_rule('/calculate/factorial', view_func=calculate_factorial_interface, methods=['POST'])
