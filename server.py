from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller
from flask_app import app






if __name__ == "__main__":
    app.run(debug=True, port = 5001)