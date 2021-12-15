import os
from src import app

from src.config import APPLICATION_PORT, APPLICATION_URL

if __name__ == '__main__':
    port = int(os.environ.get("PORT", APPLICATION_PORT))
    app.run(APPLICATION_URL, port=port)
