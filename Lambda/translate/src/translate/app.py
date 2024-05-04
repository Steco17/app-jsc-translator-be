import awsgi
from translate.run import app


def handler(event, context):
    return awsgi.response(app, event, context)


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()