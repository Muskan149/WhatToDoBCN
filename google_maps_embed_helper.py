import urllib.parse

def generate_google_maps_embed(location):
    # Encode the location name to replace spaces and special characters
    encoded_location = urllib.parse.quote_plus(location)
    # Alternatively, you can use quote to replace spaces with %20
    # encoded_location = urllib.parse.quote(location, safe='')
    
    # Construct the URL for the Google Maps Embed API
    base_url = "https://www.google.com/maps/embed/v1/place"
    api_key = "AIzaSyBNytSQe1JJJuZtnoSdaruJBcPh1F-6C0s"  # Replace with your actual API key
    embed_url = f"{base_url}?key={api_key}&q={encoded_location}"
    iframe_html = f"""
        <iframe
        width="600"
        height="450"
        style="border:0"
        loading="lazy"
        allowfullscreen
        referrerpolicy="no-referrer-when-downgrade"
        src="{embed_url}">
        </iframe>
        """
    
    return iframe_html

# Example usage
# location = "1600 Amphitheatre Parkway, Mountain View, CA"
# embed_url = generate_google_maps_embed_url(location)
# print(embed_url)
