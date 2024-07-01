import requests

def get_images(query, per_page=10):
    """
    Fetch images from Unsplash based on a search query.

    Parameters:
    - query: The search term (e.g., 'Barcelona').
    - client_id: Your Unsplash API client ID.
    - per_page: Number of images to fetch per page (default is 10).

    Returns:
    - List of image URLs.
    """
    url = "https://api.unsplash.com/search/photos"
    client_id = 'vFoenFssCSTDzWqu3FR73QVaqm2h-gQihQpCW5Jeo-M'  # Replace with your Unsplash API key

    params = {
        'query': query,
        'client_id': client_id,
        'per_page': per_page
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        image_urls = [result['urls']['regular'] for result in data['results']]
        return image_urls
    else:
        print(f"Error fetching images: {response.status_code}")
        return []

# Example usage
# client_id = 'vFoenFssCSTDzWqu3FR73QVaqm2h-gQihQpCW5Jeo-M'  # Replace with your Unsplash API key
place = 'Parc Guell'
images = get_images(place, 2)

# Print the image URLs
for idx, img_url in enumerate(images):
    print(f"Image {idx + 1}: {img_url}")
