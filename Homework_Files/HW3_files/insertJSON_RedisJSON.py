import json
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)
with open('json_test.json') as data_file:
    test_data = json.load(data_file)
r.set('test_json', test_data)
