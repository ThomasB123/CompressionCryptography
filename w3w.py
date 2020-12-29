import what3words
from os import environ

geocoder = what3words.Geocoder("YYA7IRI8")

autosuggest = geocoder.autosuggest('freshen.overlook.clo', \
    clip_to_country="FR", \
    focus=what3words.Coordinates(48.856618, 2.3522411), \
    n_results=1, \
)

if 'error' in autosuggest: # An error has been returned from the API
    code = autosuggest['error']['code']
    message = autosuggest['error']['message']

    print (code, message)
else:
    # Obtains the one, and only result from the returned list of suggestions
    words = autosuggest['suggestions'][0]['words']
    print("Top 3 word address match: {}".format(words))

    # Use the `convert_to_coordinates` API to convert the returned 3 word address into coordinates
    convert_to_coordinates = geocoder.convert_to_coordinates(words)

    print("WGS84 Coordinates: {}, {}".format( \
        convert_to_coordinates['coordinates']['lat'], \
        convert_to_coordinates['coordinates']['lng']))
    print("Nearest Place: {}".format(convert_to_coordinates['nearestPlace']))
