from tornado.web import Application
from tornado.options import define, options

from tornado_sqlalchemy import make_session_factory
from handler import ChatHandler

define('PORT', type=int)
define('ALLOW_DOMAINS', type=list)
define('DB_URL')


class ChatApp(Application):
    def __init__(self):
        options.parse_config_file('settings.py')
        handlers = [('/', ChatHandler)]

        factory = make_session_factory(options.DB_URL)
        super().__init__(session_factory=factory, handlers=handlers, debug=True)

