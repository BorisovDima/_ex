from datetime import datetime
from calendar import timegm
from rest_framework_simplejwt.utils import aware_utcnow

print(timegm(datetime.utcnow().utctimetuple()))
print(datetime.utcnow().utctimetuple())