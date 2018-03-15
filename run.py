import os
from app import create_app

immogarantie_app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    immogarantie_app.run(host='0.0.0.0', port=port, debug=True)