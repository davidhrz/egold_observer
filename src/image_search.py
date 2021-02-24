from utils import google_cx, google_dev_key
from google_images_search import GoogleImagesSearch
from io import BytesIO
from imghdr import what as img_extension

img_search = GoogleImagesSearch(google_dev_key, google_cx, validate_images=False)

# Returns a BytesIO that contains image data and its extension
def get_image_raw(query):
    # Look for 'query' on Google Images
    print(f'searching: "{query}"...', end=' ')
    img_search.search({'q': query, 'num': 1, 'imgSize': 'LARGE'})
    result = img_search.results()[0]
    print(f'Found image! URL tail: {result.url[-5:]}')

    # Copy image raw data into BytesIO
    b_io = BytesIO()
    b_io.seek(0)
    result.copy_to(b_io)
    b_io.seek(0)

    return b_io, img_extension(b_io)
