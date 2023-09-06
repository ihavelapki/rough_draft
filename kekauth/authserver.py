# print('start', __name__, __file__)
from src import create_app
# print('after import create_app', __name__, __file__)
from config import FlaskConfig
# print('after import config', __name__, __file__)
app = create_app(FlaskConfig)
# print('after app creation', __name__, __file__)
if __name__ == '__main__':
    app.run(debug=True)
