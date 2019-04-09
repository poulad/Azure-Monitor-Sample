import logging
import sys
import ulid

import flask
import structlog.processors

logging.basicConfig(
    format="%(message)s", stream=sys.stdout, level=logging.INFO
)
structlog.configure(
    processors=[structlog.processors.JSONRenderer()],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
)
logger = structlog.get_logger()
app = flask.Flask(__name__)


@app.route("/login", methods=["POST", "GET"])
def some_route():
    log = logger.new(request_id=str(ulid.new()))
    # do something
    # ...
    log.info("user logged in", user="test-user")
    # gives you:
    # event='user logged in' request_id='ffcdc44f-b952-4b5f-95e6-0f1f3a9ee5fd' user='test-user'
    # ...
    # some_function()
    # ...
    return "logged in!"


if __name__ == "__main__":
    app.run()
