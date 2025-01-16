import json

def lambda_handler(event, context):
    try:
        # Extract numbers from the event
        num1 = event.get('num1')
        num2 = event.get('num2')

        # Ensure numbers are provided
        if num1 is None or num2 is None:
            raise ValueError("Both num1 and num2 are required")

        # Calculate sum
        result = num1 + num2

        # Return the result
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
