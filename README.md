# Pixabay API Wrapper.

**Version 1.0.1**

A easy-to-use Python API wrapper for [Pixabay](https://pixabay.com/api/docs/).

---

## Usage
The module uses the Searcher class to make quick, easy searches. Give it a dictionary with the params you want for your search and it will return a ApiResponse object.
Paramater names can be found on the official [Pixabay Docs](https://pixabay.com/api/docs/) or further down in these docs.

*Searching for images:*

### Quickstart
```py
from pixabay import Searcher
import json

api_key = '123456' # Change value to Pixabay API Key
image_searcher = Searcher(api_key) # Initialize searcher object.
first_image = image_searcher.image_search(params={'q':'dog'}).image # Make an image search and use the .image method to retrieve the first image.
```

*Searching for videos:*
```py
from pixabay import Searcher
import json

api_key = '123456'
image_searcher = Searcher(api_key)
json_data = json.loads(image_searcher.video_search(params={'q':'cat', 'video_type': 'animation'}).text)
```
---
## Paramaters
The search system uses paramaters to narrow down results; the following are the available paramaters:

- **q** 
> The query to search for, length cannot exceed 100 characters. Expects a string.
Example: "maple syrup"

- **lang**
> Language code of the language to be searched in. Expects a string.
Accepted values: cs, da, de, en, es, fr, id, it, hu, nl, no, pl, pt, ro, sk, fi, sv, tr, vi, th, bg, ru, el, ja, ko, zh
Example: "fr"
*Default: 'en'*

- **id**
> Retrieve individual, specific, images by ID. Expects a string/int.
Example: "55555"

- **image_type**
> Filter results by image type.
Accepted values: all, photo, illustration, vector. Expects a string.
Example: "vector"
*Default: "all"*

- **video_type**
> Filter results by video type.
Accepted values: all, film, animation. Expects a string.
Example: "film"
*Default: "all"*

- **orientation**
> Whether an image is wider than it is tall, or taller than it is wide.
Accepted values: "all", "horizontal", "vertical". Expects a string.
Example: "vertical"
*Default: "all"*

- **category**
> Filter results by category.
Accepted values: backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
Example: "nature"
Expects a string.

- **min_width / min_height**
> Minimum width and height, separate parameters. Expects a str/int.
Example: "500" OR 500
Default: "0"

- **colors**
> Filter images by color properties. Expects a str/list
Accepted values: grayscale, transparent, red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown
Example: ['red', 'yellow'] OR 'red,yellow'

- **editors_choice**
> Select images that have received an Editor's Choice award. Expects a bool/str.
Accepted values: "true", "false", True, False
Example: "true" OR True
Default: "false"

- **safesearch**
> A flag indicating that only images suitable for all ages should be returned. Expects a bool/str.
Accepted values: "true", "false", True, False
Example: "true" OR True
Default: "false"

- **order**
> How the results should be ordered. Expects a str.
Accepted values: "popular", "latest"
Example: "latest"
Default: "popular"

- **page**
> Returned search results are paginated. Use this parameter to select the page number. Expects an int/str
Example: 5 OR "5"
Default: 1

- **per_page**
> Determine the number of results per page. Expects a str/int
Accepted values: 3 - 200
Example: 3 OR "3"
Default: 20

- **callback**
> JSONP callback function name. Expects a str.
Example: I really dunno.

- **pretty**
> Indent JSON output. This option should not be used in production. Expects a bool/str
Accepted values: "true", "false", True, False 
Example: False OR "false"
Default: "false"

---

## ApiResponse object/parsing data.
The ApiResponse object contains a large amount of class variables to easily get the data you need. You can also get the full dump of data easily!

**Methods**

- **index**
Returns a result with the specified index.

**Class variables.**

- **sort**
Contains "video" or "image" depending on what type of search created the object.

- **response**
Contains the response of the API call. If the response was previously cached and the content was taken from that it defaults to 200.

- **image**
Contains the first image only, will only exist if ApiResponse has a sort of "image".

- **images**
Contains all images excluding other data in the response, will only exist if ApiResponse has a sort of "image".

- **video(s)**
Same as image(s) except it will only exist if ApiResponse has a sort of "video".

- **amount**
Returns the total amount of images/videos .

**Dunders**

- **__len__**
Returns amount of results.

- **__getitem__**
Simply returns the image/video in the specified index for iteration.

- **__str__**
Returns content.

### Please report bugs or give suggestions. I will add whatever you want.
