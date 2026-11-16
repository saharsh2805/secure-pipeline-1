import os

def get_status():
    env = os.getenv("APP_ENV", "development")
    return {"status": "ok", "env": env}

if __name__ == "__main__":
    print(get_status())
