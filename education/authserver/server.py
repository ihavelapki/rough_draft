from education.authserver import create_app
from config import FlaskConfig

app = create_app(FlaskConfig)

if __name__ == '__main__':
    app.run(debug=True)
