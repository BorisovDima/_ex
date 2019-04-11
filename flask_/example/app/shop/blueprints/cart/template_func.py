from .utils import CartObj
from flask_ import session
from .routes import cart

@cart.app_template_global()
def cart_count():
    cart = CartObj(session)
    return cart.count


