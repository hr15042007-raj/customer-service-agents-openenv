import uvicorn
from fastapi import FastAPI
from openenv_core.server import OpenEnvServer
from customer_service_env import CustomerServiceEnv

# Initialize the environment
env = CustomerServiceEnv()

# Initialize the OpenEnv server wrapper
app = OpenEnvServer(env).app

def main():
    """Main entry point for the OpenEnv server"""
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
