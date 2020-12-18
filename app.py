from flask import Flask, request, send_from_directory
from os import listdir
from safety import isAllowed
import json
from dotenv import load_dotenv
from os import getenv
from os.path import join
from werkzeug.utils import secure_filename

# Load environment
load_dotenv()

uuid = getenv('FILE_POST_UUID')
blogPath = getenv('BLOG_PATH')
app = Flask(__name__)


@app.route('/')
def entry():
    return 'Hello world!'


@app.route('/blogs', methods=['GET'])
def downloadBlog():
    blogNum = request.args.get('blogNum')
    blogsList = list(filter(lambda fileName: fileName != '.keep', listdir(blogPath)))
    if blogNum is None:
        return 'INVALID'
    else:
        blogNum = int(blogNum)
    if blogNum == -1:
        return ', '.join(blogsList)
    elif blogNum >= len(blogsList):
        return 'INVALID'
    return send_from_directory(blogPath, blogsList[blogNum])


@app.route('/blogs', methods=['POST'])
def uploadBlog():
    uuidArg = request.args.get('id')
    if uuidArg is None or uuidArg != uuid:
        return ''
    file = request.files['file']
    if file == '':
        return ''
    if file and isAllowed(file.filename):
            fileName = secure_filename(file.filename)
            newFilePath = join(blogPath, fileName)
            file.save(newFilePath)
    return ''


if __name__ == "__main__":
    app.run()
