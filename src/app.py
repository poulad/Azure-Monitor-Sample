import os
import time

import flask
import structlog
import ulid
from flask import request

from src.configurations import configure_logger

configure_logger()
logger = structlog.get_logger(module=__name__)
app = flask.Flask(__name__)


@app.route('/books/<title>')
def get_book_by_title(title: str):
    request_id = request.headers.get('Request-Id', str(ulid.new()))
    log = logger.new(request_id=request_id)
    log.info("Looking up the book {title}.", data={'title': title})
    time.sleep(2)
    log.info("We have {numCopy} copies of the book {title}.", data={'title': title, 'numCopy': 4})
    return flask.jsonify({'requestId': request_id, 'book': title})


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=os.getenv('PORT', 5000)
    )
