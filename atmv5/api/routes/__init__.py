from flask import Blueprint

cards_bp = Blueprint('cards', __name__)
creditCards_bp = Blueprint('creditCards', __name__)
debitCards_bp = Blueprint('debitCards', __name__)
partners_bp = Blueprint('partners', __name__)
partnersServices_bp = Blueprint('partnersServices', __name__)
partnersCredits_bp = Blueprint('partnersCredits', __name__)
transactions_bp = Blueprint('transactions', __name__)
services_bp = Blueprint('services', __name__)

from . import cards_bp , creditCards_bp , debitCards_bp , partners_bp, partnersServices_bp , partnersCredits_bp , transactions_bp, services_bp
