# Pixabay API Wrapper.

**Version 1.0.0**

A easy-to-use Python API wrapper for [Pixabay](https://pixabay.com/api/docs/).

---

## Usage
The module uses the Searcher class to make quick, easy searches. Give it a dictionary with the params you want for your search.
Paramater names can be found on the official [Pixabay Docs](https://pixabay.com/api/docs/) or further down in these docs.

*Searching for images:*
```py
from pixabay import Searcher
import json

api_key = '123456'
image_searcher = Searcher(api_key)
json_data = json.loads(image_searcher.image_search(params={'q':'dog', 'editors_choice': True}).text)
```

*Searching for videos:*
```py
from pixabay import Searcher
import json

api_key = '123456'
image_searcher = Searcher(api_key)
json_data = json.loads(image_searcher.video_search(params={'q':'cat', 'video_type': 'animation'}).text)
```

