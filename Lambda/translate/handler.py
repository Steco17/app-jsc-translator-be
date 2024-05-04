from run import app

def lambda_handler(event, context):
    app.run(debug=True)