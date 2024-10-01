from app import create_app
from app.config.config import Config

app = create_app()

app.run(port=Config.PORT, host=Config.HOST,
        debug=True if Config.DEVELOPMENT_MODE == "debug" else False)
