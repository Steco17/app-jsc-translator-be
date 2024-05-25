import serverless_wsgi

from translate.run import app

def lambda_handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
    # https://pypi.org/project/serverless-wsgi/

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
