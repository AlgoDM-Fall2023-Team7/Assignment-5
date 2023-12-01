import base64
import requests
import json
import boto3
import openai
from snowflake.connector import connect, Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

