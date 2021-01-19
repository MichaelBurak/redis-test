#import redis
import redis
# init redis
r = redis.Redis()

# string set and get
print(r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"}))
print(r.get("Bahamas"))

# note: redis-py requires bytes, str, int, or float
