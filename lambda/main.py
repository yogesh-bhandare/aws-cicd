def handler(event, context):
    response_body = {
        "message": "Hello CI-CD",
        "version": 1.0
    }
    return {"statusCode": 200, "body": response_body}
