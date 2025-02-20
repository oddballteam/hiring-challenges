# AI/ML Engineer

## Credit Card Customer Behavior Analysis

### Background
Below is a link to a Kaggle dataset on credit card purchases:
https://www.kaggle.com/datasets/arjunbhasin2013/ccdata?resource=download 
The dataset includes various features such as balance, purchase patterns, cash advances, credit limits, and payment history.

### Task
Using unsupervised learning techniques, specifically clustering analysis, identify distinct customer segments and their characteristic behaviors from the provided credit card transaction data. Your analysis should help inform strategic business decisions.

### Data Description
The dataset contains the following features for each customer:
- Balance and balance frequency
- Different types of purchases (one-off vs. installments)
- Cash advance behavior
- Credit limit utilization
- Payment patterns
- Tenure information

### Requirements
1. Perform necessary data preprocessing and feature engineering
2. Implement and justify your choice of clustering algorithm(s)
3. Determine the optimal number of clusters using appropriate methods
4. Provide a detailed analysis of the identified customer segments

### Deliverables
- Prior to the interview, please submit a Jupyter notebook or similar document containing your code and analysis.
- During the interview, please be prepared to discuss:
  - Description of your methodology
  - Key findings about customer segments
  - Business recommendations based on your analysis
  - Discussion of potential limitations such as issues with the data
  - Areas for further investigation such as what additional columns would be helpful for augmenting the analysis (even through non-clustering solutions)

### Evaluation Criteria
Your submission will be evaluated based on:
- Technical implementation and code quality
- Depth of analysis and insights
- Business relevance of findings
- Clarity of communication
- Creative approach to feature engineering and pattern discovery

### Time Expectation
Please spend no more than 4 hours on this assignment. We value quality of analysis over quantity.

## AI Chatbot Code Review Exercise

### Background
Below is a Python script that interacts with Amazon Bedrock's AI model. This code will be deployed in production as part of a website's interactive help system. The chatbot will be implemented as a popup chat widget that allows users to ask questions about the content currently displayed on their screen.

### Current Implementation Context
- The chatbot will be accessed by multiple concurrent users
- Expected peak traffic: ~100 requests per minute
- The system needs to be production-ready and secure
- The chat widget appears on every page of the website
- Response time requirements: < 2 seconds per interaction

### Task
Please review the following code and:
1. Identify potential issues or vulnerabilities
2. Suggest improvements for production readiness
3. Consider scalability and security implications
4. Recommend best practices that should be implemented

```import json
import boto3
from botocore.exceptions import ClientError

# Hard-coded credentials (security issue!)
AWS_ACCESS_KEY = 'AKIA1234567890EXAMPLE'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

class BedrockChatbot:
    def __init__(self):
        """Initialize Bedrock client with hardcoded credentials"""
        self.bedrock_client = boto3.client(
            'bedrock-runtime',
            region_name='us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        
    def chat_with_bot(self, prompt: str) -> str:
        """Send a chat request to Amazon Bedrock."""
        # No rate limiting protection
        try:
            # Make multiple rapid requests without any delay
            for _ in range(5):  # Potential rate limiting issue
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
            # Basic error handling without retry logic
            print(f"Error: {str(e)}")
            return "Error occurred"

def process_user_input(user_message: str):
    """Process user input without any rate limiting or input validation"""
    chatbot = BedrockChatbot()
    
    # No input validation or sanitization
    responses = []
    
    # Multiple parallel requests without rate limiting
    for _ in range(10):  # Will likely trigger rate limits
        response = chatbot.chat_with_bot(user_message)
        responses.append(response)
    
    return responses

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        # No error handling around the main loop
        responses = process_user_input(user_input)
        for idx, response in enumerate(responses, 1):
            print(f"Response {idx}: {response}")

if __name__ == "__main__":
    main()```



