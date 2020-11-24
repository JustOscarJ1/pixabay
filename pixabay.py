import requests
import warnings

def add_param(request_url, param, data):
    return request_url + '&' + param + '=' + data

def create_url(request_url, params):
    # converts params to lower
    params = dict((k.lower() if isinstance(k, str) else k, v.lower() if isinstance(v, str) else v) for k, v in params.items())

    for param in params.keys():
        if param == 'q':
            if len(params['q']) > 100:
                warnings.warn('Param "q" cannot exceed 100, defaulting to "api".')
                request_url = add_param(request_url, 'q', 'api')
            else:
                request_url = add_param(request_url, 'q', params['q'].replace(' ', '+'))

        elif param == 'lang':
            if params['lang'] in ['cs', 'da', 'de', 'en', 'es', 'fr', 'id', 'it', 'hu', 'nl', 'no', 'pl', 'pt', 'ro',
                                  'sk', 'fi', 'sv', 'tr', 'vi', 'th', 'bg', 'ru', 'el', 'ja', 'ko', 'zh']:
                request_url = add_param(request_url, param, params['lang'])
            else:
                warnings.warn(
                    'Invalid language selected, use ".languages" on your image object for a list of available languages.')

        elif param == 'id':
            request_url = add_param(request_url, param, str(params['id']))

        elif param == 'image_type' or param == 'video_type':
            if param == 'image_type':
                if params['image_type'] in ['all', 'photo', 'illustration', 'vector']:
                    request_url = add_param(request_url, param, params['image_type'])
            else:
                if params['video_type'] in ["all", "film", "animation"]:
                    request_url = add_param(request_url, param, params['video_type'])

        elif param == 'orientation':
            if params['orientation'] in ['all', 'horizontal', 'vertical']:
                request_url = add_param(request_url, param, params['orientation'])

        elif param == 'category':
            if params['category'] in ['backgrounds', 'fashion', 'nature', 'science', 'education', 'feelings', 'health',
                                      'people', 'religion', 'places', 'animals', 'industry', 'computer', 'food',
                                      'sports', 'transportation', 'travel', 'buildings', 'business', 'music']:
                request_url = add_param(request_url, param, params['category'])

        elif param == 'mid_width':
            if isinstance(params['min_width'], int):
                request_url = add_param(request_url, param, str(params['min_width']))

            elif isinstance(params['min_width'], str):
                try:
                    int(params['min_width'])
                    request_url = add_param(request_url, param, params['min_width'])
                except ValueError:
                    warnings.warn('A non-integer character has been found in "min_width", defaulting to 0.')


        elif param == 'mid_width':
            if isinstance(params['min_height'], int):
                request_url = add_param(request_url, param, str(params['min_width']))

            elif isinstance(params['min_height'], str):
                try:
                    int(params['min_height'])
                    request_url = add_param(request_url, param, params['min_height'])
                except ValueError:
                    warnings.warn('A non-integer character has been found in "min_height", defaulting to 0.')

        elif param == 'colors':
            if isinstance(params['colors'], list):
                param_text = ''
                for i in params['colors']:
                    if i in ["grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue",
                             "lilac", "pink", "white", "gray", "black", "brown"]:
                        param_text += i + ','
                request_url = add_param(request_url, param, param_text[:-1])
            elif isinstance(params['colors'], str):
                clear = True
                for i in params['colors'].split(','):
                    if i not in ["grayscale", "transparent", "red", "orange", "yellow", "green", "turquoise", "blue",
                                 "lilac", "pink", "white", "gray", "black", "brown"]:
                        clear = False
                        break

                if clear:
                    request_url = add_param(request_url, param, params['colors'])

        elif param == 'editors_choice':
            if isinstance(params['editors_choice'], bool):
                if params['editors_choice']:
                    request_url = add_param(request_url, param, 'true')
                else:
                    request_url = add_param(request_url, param, 'false')

            elif isinstance(params['editors_choice'], str):
                if params['editors_choice'] == 'true':
                    request_url = add_param(request_url, param, 'true')
                elif params['editors_choice'] == 'false':
                    request_url = add_param(request_url, param, 'false')

        elif param == 'safesearch':
            if isinstance(params['safesearch'], bool):
                if params['safesearch']:
                    request_url = add_param(request_url, param, 'true')
                else:
                    request_url = add_param(request_url, param, 'false')

            elif isinstance(params['safesearch'], str):
                if params['safesearch'] == 'true':
                    request_url = add_param(request_url, param, 'true')
                elif params['safesearch'] == 'false':
                    request_url = add_param(request_url, param, 'false')

        elif param == 'order':
            if params['order'] == 'popular':
                request_url = add_param(request_url, param, 'popular')
            elif params['order'] == 'latest':
                request_url = add_param(request_url, param, 'latest')

        elif param == 'page':
            if isinstance(params['page'], int):
                request_url = add_param(request_url, param, str(params['page']))

            elif isinstance(params['page'], str):
                try:
                    int(params['page'])
                    request_url = add_param(request_url, param, params['page'])
                except ValueError:
                    warnings.warn('A non-integer character has been found in "page", defaulting to 1.')


        elif param == 'per_page':
            if isinstance(params['per_page'], int):
                if params['per_page'] < 3:
                    warnings.warn('Param "per_page" cannot be under 3, defaulting to 20.')
                else:
                    request_url = add_param(request_url, param, str(params['page']))

            elif isinstance(params['per_page'], str):
                try:
                    int(params['per_page'])
                    if int(params['per_page']) > 3:
                        warnings.warn('Param "per_page" cannot be under 3, defaulting to 20.')
                    else:
                        request_url = add_param(request_url, param, params['page'])
                except ValueError:
                    warnings.warn('A non-integer character has been found in "per_page", defaulting to 20.')

        elif param == 'callback':
            request_url = add_param(request_url, param, params['callback'])

        elif param == 'pretty':
            if isinstance(params['pretty'], bool):
                if params['pretty']:
                    request_url = add_param(request_url, param, 'true')
                else:
                    request_url = add_param(request_url, param, 'false')

            elif isinstance(params['pretty'], str):
                if params['pretty'] == 'true':
                    request_url = add_param(request_url, param, 'true')
                elif params['pretty'] == 'false':
                    request_url = add_param(request_url, param, 'false')

    return request_url

class Searcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def update_key(self, api_key):
        self.api_key = api_key

    def image_search(self, params):
        request_url = f'https://pixabay.com/api/?key={self.api_key}'
        request_url = create_url(request_url=request_url, params=params)
        return requests.get(request_url)

    def video_search(self, params):
        request_url = f'https://pixabay.com/api/videos/?key={self.api_key}'
        request_url = create_url(request_url=request_url, params=params)
        return requests.get(request_url)

    def docs(self):
        pass
