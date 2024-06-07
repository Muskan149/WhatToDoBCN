import streamlit as st
from google_maps_embed_helper import generate_google_maps_embed
import random

barcelona_activities = [
    "🏰 Visit Sagrada Família",
    "🌳 Explore Park Güell",
    "🚶 Walk down La Rambla",
    "🏖️ Enjoy the beach at Barceloneta",
    "🏠 Visit Casa Batlló",
    "🏰 Wander through the Gothic Quarter",
    "🖼️ Discover the Picasso Museum",
    "🚠 Take a cable car to Montjuïc",
    "💃 Watch a flamenco show",
    "⛲ Visit the Magic Fountain of Montjuïc",
    "🛍️ Explore the Mercat de Sant Josep de la Boqueria",
    "🍽️ Enjoy tapas in El Born",
    "⛪ Visit the Barcelona Cathedral",
    "🚴 Take a bike tour around the city",
    "🏛️ Explore the Poble Espanyol",
    "🐠 Visit the Barcelona Aquarium",
    "⚽ Watch a FC Barcelona match at Camp Nou",
    "🏔️ Take a day trip to Montserrat",
    "🌄 Enjoy panoramic views from Tibidabo",
    "🏙️ Explore the Raval neighborhood",
    "🎨 Visit the Joan Miró Foundation",
    "🍳 Take a cooking class",
    "⚓ Explore the Maritime Museum",
    "🔬 Visit the CosmoCaixa Science Museum",
    "🍷 Take a wine tasting tour in Penedès",
    "🎨 Visit the National Art Museum of Catalonia (MNAC)",
    "🎨 Go on a street art tour in El Raval",
    "🏘️ Explore the Gràcia neighborhood",
    "🏞️ Visit the Park of the Ciutadella",
    "🚤 Take a boat tour along the coastline",
    "🏛️ Explore the Museu d'Història de Barcelona (MUHBA)",
    "🌇 Enjoy the views from Bunkers del Carmel",
    "🎭 Visit the Liceu Opera House",
    "🏛️ Explore the El Born Cultural Center",
    "🎨 Visit the Gaudí Exhibition Center",
    "🚁 Take a helicopter tour of Barcelona",
    "🌿 Explore the Barcelona Botanical Garden",
    "🦁 Visit the Barcelona Zoo",
    "🏰 Take a day trip to Girona",
    "🛍️ Explore the Mercat de Sant Antoni",
    "🎵 Enjoy a concert at Palau de la Música Catalana",
    "🖼️ Visit the Museu Nacional d'Art de Catalunya (MNAC)",
    "🛴 Take a Segway tour around the city",
    "🏅 Explore the Olympic Park",
    "🎨 Visit the Fundació Joan Miró"
]

barcelona_places = [
    "Sagrada Família",
    "Park Güell",
    "La Rambla",
    "Barceloneta Beach",
    "Casa Batlló",
    "Gothic Quarter",
    "Picasso Museum",
    "Montjuïc",
    "Various venues",
    "Magic Fountain of Montjuïc",
    "Mercat de Sant Josep de la Boqueria",
    "El Born",
    "Barcelona Cathedral",
    "Various routes around the city",
    "Poble Espanyol",
    "Barcelona Aquarium",
    "Camp Nou",
    "Montserrat",
    "Tibidabo",
    "Raval neighborhood",
    "Joan Miró Foundation",
    "Various venues",
    "Maritime Museum",
    "CosmoCaixa Science Museum",
    "Penedès",
    "National Art Museum of Catalonia (MNAC)",
    "El Raval",
    "Gràcia neighborhood",
    "Park of the Ciutadella",
    "Barcelona coastline",
    "Museu d'Història de Barcelona (MUHBA)",
    "Bunkers del Carmel",
    "Liceu Opera House",
    "El Born Cultural Center",
    "Gaudí Exhibition Center",
    "Various routes around the city",
    "Barcelona Botanical Garden",
    "Barcelona Zoo",
    "Girona",
    "Mercat de Sant Antoni",
    "Palau de la Música Catalana",
    "Museu Nacional d'Art de Catalunya (MNAC)",
    "Various routes around the city",
    "Olympic Park",
    "Fundació Joan Miró"
]

activity_to_desc = {
    "🏰 Visit Sagrada Família": "Explore Gaudí's unfinished masterpiece! Marvel at the intricate facades and colorful stained glass. A blend of Gothic and Art Nouveau, this basilica's grandeur and detail will leave you in awe. Don't miss the stunning views from the towers!",
    "🌳 Explore Park Güell": "Step into a whimsical wonderland at Park Güell! Gaudí’s imaginative designs, mosaic-covered benches, and playful architecture create a vibrant escape. Wander through lush gardens, spot colorful lizards, and enjoy breathtaking city views from this enchanting park.",
    "🚶 Walk down La Rambla": "Stroll down La Rambla, Barcelona's bustling boulevard! Enjoy street performers, vibrant flower stalls, and cozy cafés. This lively promenade connects you to local culture, historic sites, and endless entertainment. A must-see for first-time visitors!",
    "🏖️ Enjoy the beach at Barceloneta": "Soak up the sun at Barceloneta Beach! Swim in the Mediterranean, play beach volleyball, or simply relax on the golden sands. Nearby seafood restaurants and beach bars make it a perfect spot for a fun-filled day.",
    "🏠 Visit Casa Batlló": "Step inside Gaudí’s dreamlike Casa Batlló! With its wavy walls, colorful mosaics, and skeletal balconies, this modernist marvel feels alive. Explore the fantastical interior and rooftop terrace for a truly unique architectural experience.",
    "🏰 Wander through the Gothic Quarter": "Get lost in the Gothic Quarter's narrow, winding streets! Discover hidden squares, ancient cathedrals, and charming shops. This historic neighborhood is perfect for exploring medieval architecture and soaking in the old-world charm.",
    "🖼️ Discover the Picasso Museum": "Immerse yourself in Picasso's artistic journey at the Picasso Museum! Housed in medieval palaces, the collection showcases his early works, Blue Period, and groundbreaking pieces. A treasure trove for art lovers and history buffs.",
    "🚠 Take a cable car to Montjuïc": "Glide above the city on a cable car to Montjuïc! Enjoy panoramic views, explore historic sites, and visit cultural attractions like the Magic Fountain. It's an adventure that combines scenic beauty with rich history.",
    "💃 Watch a flamenco show": "Experience the passion of a flamenco show! Feel the rhythmic stomps, soulful singing, and fiery guitar strums. This traditional Spanish dance will captivate you with its intensity and emotion. A mesmerizing night out!",
    "⛲ Visit the Magic Fountain of Montjuïc": "Be enchanted by the Magic Fountain of Montjuïc! Watch the stunning water, light, and music show as colorful jets dance in sync. A magical spectacle that's perfect for an evening outing with friends or family.",
    "🛍️ Explore the Mercat de Sant Josep de la Boqueria": "Dive into the bustling Boqueria Market! Savor fresh seafood, exotic fruits, and local delicacies. This vibrant market is a feast for the senses and a great place to taste the flavors of Barcelona.",
    "🍽️ Enjoy tapas in El Born": "Indulge in tapas heaven in El Born! Sample a variety of small plates, from patatas bravas to jamón ibérico. This trendy neighborhood offers delicious bites and a lively atmosphere. Perfect for a foodie's night out!",
    "⛪ Visit the Barcelona Cathedral": "Admire the grandeur of Barcelona Cathedral! With its stunning Gothic architecture, intricate carvings, and serene cloisters, this historic church is a peaceful retreat in the heart of the city. Don't miss the rooftop views!",
    "🚴 Take a bike tour around the city": "Pedal your way through Barcelona on a bike tour! Discover iconic landmarks, hidden gems, and scenic routes. It's a fun and eco-friendly way to explore the city's diverse neighborhoods and vibrant culture.",
    "🏛️ Explore the Poble Espanyol": "Step into Spain's cultural mosaic at Poble Espanyol! This open-air museum features replicas of traditional buildings from across the country. Wander through charming streets, visit artisan shops, and enjoy live performances.",
    "🐠 Visit the Barcelona Aquarium": "Dive into the underwater world at Barcelona Aquarium! Walk through the shark tunnel, explore diverse marine habitats, and meet fascinating sea creatures. An exciting and educational adventure for all ages.",
    "⚽ Watch a FC Barcelona match at Camp Nou": "Cheer for FC Barcelona at Camp Nou! Experience the electric atmosphere, passionate fans, and world-class football. Whether you're a die-hard fan or a casual observer, a match here is unforgettable.",
    "🏔️ Take a day trip to Montserrat": "Escape to Montserrat's stunning mountain range! Hike scenic trails, visit the famous monastery, and enjoy breathtaking views. This serene and spiritual getaway offers a refreshing break from the city's hustle and bustle.",
    "🌄 Enjoy panoramic views from Tibidabo": "Reach new heights at Tibidabo! Take in panoramic views of Barcelona, visit the amusement park, and explore the beautiful church. A perfect spot for family fun and breathtaking scenery.",
    "🏙️ Explore the Raval neighborhood": "Discover the vibrant Raval neighborhood! Known for its eclectic mix of cultures, trendy boutiques, and artistic vibe, this area offers a dynamic experience. Wander through its lively streets and embrace the local creativity.",
    "🎨 Visit the Joan Miró Foundation": "Delve into the surreal world of Joan Miró! This foundation showcases the artist's bold, colorful works in a stunning modernist building. A must-visit for art enthusiasts and those seeking creative inspiration.",
    "🍳 Take a cooking class": "Unleash your inner chef with a Barcelona cooking class! Learn to prepare traditional dishes like paella and tapas, and enjoy a delicious meal you've created. A fun and tasty way to experience local cuisine.",
    "⚓ Explore the Maritime Museum": "Set sail through history at the Maritime Museum! Housed in a grand shipyard, this museum explores Barcelona's rich naval past with fascinating exhibits and life-sized replicas. A maritime adventure awaits!",
    "🔬 Visit the CosmoCaixa Science Museum": "Ignite your curiosity at CosmoCaixa Science Museum! Interactive exhibits, a planetarium, and a flooded forest make science fun for all ages. It's a hands-on experience that will leave you amazed and inspired.",
    "🍷 Take a wine tasting tour in Penedès": "Sip and savor on a wine tasting tour in Penedès! Explore picturesque vineyards, learn about winemaking, and enjoy delicious local wines. A delightful day trip for wine lovers and those seeking a scenic escape.",
    "🎨 Visit the National Art Museum of Catalonia (MNAC)": "Marvel at masterpieces in the MNAC! From Romanesque murals to modernist art, this museum offers a comprehensive look at Catalonia's artistic heritage. Housed in the stunning Palau Nacional, it's a visual feast.",
    "🎨 Go on a street art tour in El Raval": "Uncover urban art on a street art tour in El Raval! Discover vibrant murals, graffiti, and creative installations. This dynamic neighborhood is a canvas for artists, offering a unique and colorful experience.",
    "🏘️ Explore the Gràcia neighborhood": "Wander the bohemian streets of Gràcia! Known for its artistic spirit, quirky boutiques, and charming plazas, this neighborhood is perfect for a leisurely stroll. Experience the local vibe and enjoy a coffee at a cozy café.",
    "🏞️ Visit the Park of the Ciutadella": "Relax in the green oasis of Park of the Ciutadella! Paddle a boat on the lake, marvel at the grand fountain, and visit the zoo. This urban park is a perfect escape for nature lovers and families.",
    "🚤 Take a boat tour along the coastline": "Set sail on a boat tour along Barcelona's coastline! Enjoy the sea breeze, stunning views, and a new perspective of the city. It's a refreshing and scenic adventure perfect for a sunny day.",
    "🏛️ Explore the Museu d'Història de Barcelona (MUHBA)": "Travel back in time at the MUHBA! Explore ancient Roman ruins, medieval streets, and historic artifacts. This museum offers a fascinating journey through Barcelona's rich history, right in the heart of the Gothic Quarter.",
    "🌇 Enjoy the views from Bunkers del Carmel": "Soak in breathtaking views from Bunkers del Carmel! This former civil war bunker offers panoramic vistas of Barcelona. A perfect spot for a picnic, sunset watching, and capturing stunning photos.",
    "🎭 Visit the Liceu Opera House": "Experience elegance at the Liceu Opera House! With its opulent interior and world-class performances, this historic venue offers a taste of Barcelona's cultural richness. Enjoy a night of enchanting music and drama.",
    "🏛️ Explore the El Born Cultural Center": "Unveil history at the El Born Cultural Center! This archaeological site reveals medieval Barcelona, with fascinating exhibits and preserved ruins. A cultural gem that brings the past to life in the heart of the city.",
    "🎨 Visit the Gaudí Exhibition Center": "Discover Gaudí's genius at the Gaudí Exhibition Center! Learn about his innovative techniques, visionary designs, and iconic works. This interactive museum offers a deep dive into the mind of Barcelona's most famous architect.",
    "🚁 Take a helicopter tour of Barcelona": "Elevate your adventure with a helicopter tour! Soar above Barcelona's landmarks, coastline, and mountains. This thrilling experience offers unmatched aerial views and a unique perspective of the city's beauty.",
    "🌿 Explore the Barcelona Botanical Garden": "Wander through the lush Barcelona Botanical Garden! Discover diverse plant species from around the world. This serene haven is perfect for nature lovers seeking a peaceful escape in the heart of the city.",
    "🦁 Visit the Barcelona Zoo": "Meet exotic animals at the Barcelona Zoo! Home to over 400 species, including lions, elephants, and dolphins, this zoo offers a fun and educational experience for visitors of all ages.",
    "🏰 Take a day trip to Girona": "Escape to the medieval charm of Girona! Explore its narrow streets, visit the impressive cathedral, and stroll along the ancient city walls. A picturesque day trip filled with history and beauty.",
    "🛍️ Explore the Mercat de Sant Antoni": "Dive into the vibrant Mercat de Sant Antoni! This bustling market offers fresh produce, local delicacies, and unique finds. A lively spot for shopping and tasting the flavors of Barcelona.",
    "🎵 Enjoy a concert at Palau de la Música Catalana": "Experience the magic of a concert at Palau de la Música Catalana! This stunning modernist concert hall, with its ornate decor and exceptional acoustics, offers an unforgettable musical evening.",
    "🖼️ Visit the Museu Nacional d'Art de Catalunya (MNAC)": "Marvel at masterpieces in the MNAC! From Romanesque murals to modernist art, this museum offers a comprehensive look at Catalonia's artistic heritage. Housed in the stunning Palau Nacional, it's a visual feast.",
    "🛴 Take a Segway tour around the city": "Glide through Barcelona on a Segway tour! Discover iconic landmarks, hidden gems, and scenic routes effortlessly. It's a fun and unique way to explore the city's diverse neighborhoods and attractions.",
    "🏅 Explore the Olympic Park": "Relive the glory of the 1992 Olympics at the Olympic Park! Visit the impressive stadium, explore the Olympic Museum, and enjoy panoramic views. A dynamic destination for sports enthusiasts and history buffs.",
    "🎨 Visit the Fundació Joan Miró": "Delve into the surreal world of Joan Miró! This foundation showcases the artist's bold, colorful works in a stunning modernist building. A must-visit for art enthusiasts seeking creative inspiration."
    }


# Mapping places to activities
place_to_activity = dict(zip(barcelona_places, barcelona_activities))


def random_place():
    done_activities = []
    place = random.choice(barcelona_places)
    return place




# # HTML and CSS to center align content
# st.markdown("""
#     <style>
#     .center {
#         display: flex;
#         justify-content: center;
#         align-items: center;
#         flex-direction: column;
#     }
#     .container {
#         max-width: 600px;
#         margin: auto;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# Center align content
# st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)

st.set_page_config(
        page_title="BCN Move 🇪🇸",
        page_icon="🇪🇸"                  
        )

st.title("BCN Move 🇪🇸")
st.text(" \n")

if st.button("What's the Move?"):
    st.text(" \n")
    place = random_place()
    activity = place_to_activity[place]

    st.markdown(f"**{activity}**")
    st.write(activity_to_desc[activity])
    st.text(" \n")

    st.markdown(f"📍: {place}")

    iframe_html = generate_google_maps_embed(place)

    st.markdown(f'<div style="width:75%">{iframe_html}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)