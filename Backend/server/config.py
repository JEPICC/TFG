import os

setting = dict(
    host = os.getenv('MONGODB_HOST', 'localhost'),
    # username = os.getenv('MONGODB_USER', ''),
    # password = os.getenv('MONGODB_PASSWORD', ''),
    port = int(os.getenv('MONGODB_PORT', 27017))
)