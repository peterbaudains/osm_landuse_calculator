from shapely.geometry import Point

def overpass_lu_calculator(data):

    for way in [i for i in data['elements'] if i['type'] == 'way']:

        print([Point(i['lat'], i['lon']) for i in data['elements'] if i['id'] in way['nodes']])

    


if __name__=="__main__":
    
    import json

    with open('/Users/pete/Desktop/data_mini.json', 'r') as f:
        data = json.load(f)

    overpass_lu_calculator(data)
