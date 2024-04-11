from streamlit_js_eval import get_geolocation


def get_my_location():

    location = get_gelocation()

    if location is not None:

        return location['coords']['latitude'], location['coords']['longitude']

    else:
        return None, None