import os

def get_status():
    env = os.getenv("APP_ENV", "development")
    return {"status": "ok", "env": env, "version": "0.1.0"}

if __name__ == "__main__":
    print(get_status())
