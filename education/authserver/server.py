from education.authserver import create_app
from config import FlaskConfig, DB_NAME

app = create_app(FlaskConfig)

if __name__ == '__main__':
    app.run(debug=True)
