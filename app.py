import os
from flask import Flask, request, abort, json
from flask_cors import CORS, cross_origin

import hashlib

UPLOAD_FOLDER = '/data'

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
@cross_origin()
def upload_file():
    if 'application/json' not in request.content_type:
        abort(415, 'Invalid content type, "application/json" expected')

    json_content = request.get_json(force=True)
    if json_content is None:
        abort(415, 'Content is not valid, a valid json expected')

    sha1_hash = hashlib.sha1(json.dumps(json_content).encode("utf-8")).hexdigest()

    filename = os.path.join(
        app.config['UPLOAD_FOLDER'],
        sha1_hash + '.json'
    )

    with open(filename, 'w') as outfile:
        json.dump(json_content, outfile)

    data = {
        'filename': sha1_hash + '.json'
    }

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/<filename>', methods=['GET'])
@cross_origin()
def get_file(filename):
    file = os.path.join(
        app.config['UPLOAD_FOLDER'],
        filename
    )

    if not os.path.exists(file):
        abort(404, 'File with filename "{}" not found.'.format(filename))

    with open(file) as json_file:
        data = json.load(json_file)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.secret_key = '2349978342978342907889709154089438989043049835891'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.debug = True

    app.run(debug=True, host='0.0.0.0')
