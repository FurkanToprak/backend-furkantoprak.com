allowedExtensions = ['md', 'txt']
def isAllowed(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowedExtensions