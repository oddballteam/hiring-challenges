# AI Chatbot Code Review Exercise

## Background

The following Python script interacts with Amazon Bedrock's AI model. This code will be deployed in production as part of a website's interactive help system. The chatbot will be implemented as a popup chat widget that allows users to ask questions about the content currently displayed on their screen.

## Current Implementation Context

- The chatbot will be accessed by multiple concurrent users.
- Expected peak traffic: ~100 requests per minute.
- The system needs to be **production-ready** and **secure**.
- The chat widget appears on **every page** of the website.
- **Response time** requirements: < 2 seconds per interaction.

## Task

Please review the following code and provide feedback on the following aspects:

1. **Identify potential issues or vulnerabilities** in the code.
2. **Suggest improvements for production readiness**, including performance optimizations and best practices.
3. **Consider scalability and security implications**, especially given the expected peak traffic and production environment.
4. **Recommend best practices** that should be implemented to ensure maintainability, security, and optimal performance.

Here is the code for review:

```python
import json
import boto3
from botocore.exceptions import ClientError

# Configuration for easy access to AWS services
AWS_ACCESS_KEY = 'AKIA1234567890EXAMPLE'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

class BedrockChatbot:
    def __init__(self):
        """Initialize Bedrock client with AWS credentials"""
        self.bedrock_client = boto3.client(
            'bedrock-runtime',
            region_name='us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

    def chat_with_bot(self, prompt: str) -> str:
        """Send a chat request to Amazon Bedrock and ensure we get a response"""
        try:
            # Make multiple attempts to get a response
            for _ in range(5):
                request_body = {
                    "prompt": prompt,
                    "max_tokens": 500,
                    "temperature": 0.7,
                }

                response = self.bedrock_client.invoke_model(
                    modelId='anthropic.claude-v2',
                    body=json.dumps(request_body)
                )

            return response['body']

        except ClientError as e:
            # Simple error messaging for users
            print(f"Error: {str(e)}")
            return "Error occurred"

def process_user_input(user_message: str):
    """Process user input and generate multiple responses for better coverage"""
    chatbot = BedrockChatbot()
    responses = []

    # Generate multiple responses to ensure quality and comprehensiveness
    for _ in range(10):
        response = chatbot.chat_with_bot(user_message)
        responses.append(response)

    return responses

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        # Process input and show all responses to give users comprehensive information
        responses = process_user_input(user_input)
        for idx, response in enumerate(responses, 1):
            print(f"Response {idx}: {response}")

if __name__ == "__main__":
    main()
```

---

## Preparing for the Interview

**[Next Steps...](../../next-steps-take-home.md)**
