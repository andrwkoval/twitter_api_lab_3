from geopy import ArcGIS


def analysis(key, data):
    """

    :param key:
    :param data:
    :return:
    """

    keys = ["id", "name", "screen_name", "location","description",
            "followers_count", "friends_count", "created_at",
            "favorites_count", "time_zone", "lang"]
    result = []

    if key not in keys:
        print("Enter a correct key.")
        exit()

    for info in data['users']:
        if key == "name":
            result.append(info[key])
        elif key == "location":
            result.append((info["name"], loc_coords(info[key]),
                           info["profile_image_url"]))
        else:
            result.append((info[key], info["name"]))

    return result


def loc_coords(location):
    """
    (str) -> (float, float)
    Function finds coordinates of the specific location

    location: name of location to get
    map coordinates
    returns: tuple of latitude and longitude
    """

    if location:
        geolocator = ArcGIS(timeout=10)
        locat = geolocator.geocode(location)
        return locat.latitude, locat.longitude



