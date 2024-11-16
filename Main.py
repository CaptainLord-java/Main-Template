from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Main Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f4f4f4;
                color: #333;
            }
            h1 {
                font-size: 2rem;
            }
            p {
                font-size: 1rem;
            }
            footer {
                margin-top: 20px;
                font-size: 0.8rem;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div>
            <h1>Welcome to the Main Page</h1>
            <p>This is a simple test to check if the site is working.</p>
            <footer>&copy; 2024 Your Name</footer>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
