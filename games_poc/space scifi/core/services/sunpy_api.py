from time import time

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.time import Time
from sunpy.coordinates import get_body_heliographic_stonyhurst, frames


def get_objects(objs, t=None):
    if t is None:
        t = time()
    obstime = Time(t, format='unix')

    objects = []

    for object in objs:
        coord = get_body_heliographic_stonyhurst(object, time=obstime)
        coord_rep = {
            "name": object.title(),

            "t": t,
            "x": coord.lon.rad,
            "y": coord.lat.rad,
            "r": coord.radius.value,
            "crs": type(coord).__name__
        }

        objects.append(coord_rep)

    return objects


def to_cart(obj):
    obstime = Time(obj['t'], format='unix')

    if 'crs' not in obj or obj['crs'] == 'HeliographicStonyhurst':
        coord = SkyCoord(obj['x']*u.rad, obj['y']*u.rad, obj['r']*u.au, frame=frames.HeliographicStonyhurst, obstime=obstime)
        coord2 = coord.transform_to(frames.Heliocentric)
    else:
        raise Exception("Wrong conversion {} -> {}".format(obj.get('crs'), 'Heliocentric'))

    return {
        "name": obj.get("name"),
        "x": coord2.x.value,
        "y": coord2.y.value,
        "z": coord2.z.value,
        "t": obj["t"],
        "crs": 'HelioCentric'
    }


def to_sphere(obj):
    obstime = Time(obj['t'], format='unix')

    if 'crs' not in obj or obj['crs'] == 'HelioCentric':
        coord = SkyCoord(obj['x']*u.km, obj['y']*u.km, obj['z']*u.km, frame=frames.Heliocentric, obstime=obstime)
        coord2 = coord.transform_to(frames.HeliographicStonyhurst)
    else:
        raise Exception("Wrong conversion {} -> {}".format(obj.get('crs'), 'HeliographicStonyhurst'))

    return {
        "name": obj.get("name"),
        "x": coord2.lon.rad,
        "y": coord2.lat.rad,
        "r": coord2.radius.to(u.au).value,
        "t": obj["t"],
        "crs": 'HeliographicStonyhurst'
    }
