import requests
import json

overpass_url = "http://overpass-api.de/api/interpreter"

overpass_query = """
[timeout:25][out:json];
( way(around:500,51.5,-0.1)(if:is_closed()==1)[landuse];
  way(around:500,51.5,-0.1)(if:is_closed()==1)[leisure];
  way(around:500,51.5,-0.1)(if:is_closed()==1)[natural];
  way(around:500,51.5,-0.1)(if:is_closed()==1)[tourism];
  way(around:500,51.5,-0.1)(if:is_closed()==1)[waterway];  
  relation(around:500,51.5,-0.1)(if:is_closed()==1)[landuse];
  relation(around:500,51.5,-0.1)(if:is_closed()==1)[leisure];
  relation(around:500,51.5,-0.1)(if:is_closed()==1)[natural];
  relation(around:500,51.5,-0.1)(if:is_closed()==1)[tourism];
  relation(around:500,51.5,-0.1)(if:is_closed()==1)[waterway];  
);  
(._;>;);
out body;
"""

response = requests.get(overpass_url, 
                        params={'data': overpass_query})
data = response.json()

with open('/Users/pete/Desktop/data.json', 'w') as f:
    json.dump(data, f)