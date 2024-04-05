from flask import Flask
from routes.cards_routes import cards_bp
from routes.creditCards_routes import creditCards_bp
from routes.debitCards_routes import debitCards_bp
from routes.partners_routes import partners_bp
from routes.partnersServices_routes import partnersServices_bp
from routes.partnersCredits_routes import partnersCredits_bp
from routes.transactions_routes import transactions_bp
from routes.services_routes import services_bp
app = Flask(__name__)
app.register_blueprint(cards_bp)
app.register_blueprint(creditCards_bp)
app.register_blueprint(debitCards_bp)
app.register_blueprint(partners_bp)
app.register_blueprint(partnersServices_bp)
app.register_blueprint(partnersCredits_bp)
app.register_blueprint(transactions_bp)
app.register_blueprint(services_bp)

if __name__ == '__main__':
    app.run(debug=True)
