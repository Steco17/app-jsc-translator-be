import serverless_wsgi
import json
from translate.run import app

def lambda_handler(event, context):
    print("event:", event)
    # response = {
    #     "statusCode": 200,
    #     # Modify the CORS settings below to match your specific requirements
    #     "headers": {
    #         "Access-Control-Allow-Origin": "*",  # Restrict this to domains you trust
    #         "Access-Control-Allow-Headers": "Content-Type",  # Specify only the headers you need to allow
    #     },
    # }
    # Use serverless_wsgi to handle the request
    wsgi_response = serverless_wsgi.handle_request(app, event, context)

    # Merge CORS headers with the WSGI response headers
    # wsgi_response['headers'].update(response['headers'])

    return wsgi_response
    # https://pypi.org/project/serverless-wsgi/

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
