from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def entry():
    return 'Hi'

@app.route('/blogs', methods=['POST'])
def uploadBlog():
    print(request)

if __name__ == "__main__":
    app.run()