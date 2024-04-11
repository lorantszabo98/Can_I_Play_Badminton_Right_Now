from streamlit_js_eval import get_geolocation


def get_my_location():

    location = get_geolocation()
    return location['coords']['latitude'], location['coords']['longitude']
