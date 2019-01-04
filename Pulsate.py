import requests

response = requests.get("https://iam.virginpulse.com/auth/realms/virginpulse/protocol/openid-connect/auth?client_id=genesis-ui&redirect_uri=https%3A%2F%2Fapp.member.virginpulse.com%2F&state=02e8f125-19c0-47bc-adfc-b9a5428332b9&nonce=8ec39bb4-ac4f-4c45-8df2-51cf1c0957a8&response_mode=fragment&response_type=code&scope=openid")
print("yolo")
