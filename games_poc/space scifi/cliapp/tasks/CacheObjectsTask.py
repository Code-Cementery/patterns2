import json
from time import time

from core.services import sunpy_api

planet_list = ['sun', 'venus', 'mars', 'mercury', 'jupiter', 'saturn', 'neptune', 'uranus', 'earth']

class CacheObjectsTask:

    def __init__(self, scheduler):
        self.sch = scheduler

    def run(self):
        now = time()

        objects = sunpy_api.get_objects(planet_list, t=now)

        with open('webapp/public/json/objects.json', 'w') as fh:
            json.dump(objects, fh)
