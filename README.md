## Implementation of recruitment task for the position of backend developer
### _Tech-stack: Python, Django, Django REST framework, Docker, docker-compose_

## Task objective

Design and implement a simple backend application for managing photos. Store photo title, album ID, width, height
and dominant color (as a hex code) in local database; the files should be stored in local filesystem.
Functionalities:
* Photos REST resource (list, create, update, delete)
* Output fields (list): ID, title, album ID, width, height, color (dominant color), URL (URL to
locally stored file)
* Input fields (create, update): title, album ID, URL
* Import photos from external API at https://jsonplaceholder.typicode.com/photos; via both
REST API and a CLI script
* Import photos from JSON file (expecting the same data format as the external API's); via
both REST API and a CLI script
