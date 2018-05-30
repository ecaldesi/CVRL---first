import os

from flask import Flask, render_template, request

from web.faces.controllers import faces

# Build app
app = Flask(__name__)
# Analytics(app)

# Defaults
app.config['DEBUG'] = True
# app.config['OWNER_AUTHOR_KEY'] = 'bjrichardwebster'
# app.config['ANALYTICS']['GOOGLE_UNIVERSAL_ANALYTICS']['ACCOUNT'] = 'UA-80482679-1'

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

app.register_blueprint(faces, url_prefix='/faces')
