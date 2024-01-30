import googlemaps

gm = googlemaps.Client(key="AIzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g")

results = gm.places_nearby(
    location={'lat': 33.5902, 'lng': 130.4017},
    keyword='cafe',
    radius=25000,
    type='restaurant'
)

for i in results.get('results',[]):
    if float(i.get('rating')) > 4.4:
        print(i.get('name'))
        print(i.get('rating'))


