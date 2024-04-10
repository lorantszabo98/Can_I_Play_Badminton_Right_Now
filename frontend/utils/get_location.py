import geocoder


def get_my_location():

    location = geocoder.ip('me')
    return location.latlng[0], location.latlng[1]
