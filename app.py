from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def entry():
    return 'Hello world!'

@app.route('/blogs', methods=['GET'])
def uploadBlog():
    return send_from_directory('blog')

if __name__ == "__main__":
    app.run()