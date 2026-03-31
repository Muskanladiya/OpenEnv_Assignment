import sys
import os

# Add current folder to Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import environment and models
from email_env_environment import EmailEnvironment
from models import EmailAction

# Initialize environment
env = EmailEnvironment()

# Reset environment
obs = env.reset()
print("Reset observation:", obs)

# Step example
action = EmailAction(message="Hello OpenEnv!")
obs = env.step(action)
print("Step observation:", obs)

# Step with another message
action = EmailAction(message="Testing 123")
obs = env.step(action)
print("Step observation:", obs)