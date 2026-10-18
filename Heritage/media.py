"""
Photos and videos for the heritage pages.

Photos come from Unsplash (free to use under the Unsplash License) and are
credited to their photographers. Videos are YouTube embeds from their official
publishers. Every photo's location was checked against its Unsplash page.

To change a photo:   find its Unsplash page, copy the "photo-XXXX" ID from the
                     image address, and update the photo(...) call below.
To change a video:   paste the 11-character ID from the YouTube URL
                     (youtube.com/watch?v=THIS_PART) into video(...).

Section photos/videos are matched to sections by their heading text in
content.py, so keep the headings in sync if you rename a section.
"""

UNSPLASH_URL = 'https://images.unsplash.com/photo-{id}?auto=format&fit=crop&w={width}&q=80'


def photo(image_id, alt, caption, photographer, page):
    return {
        'src': UNSPLASH_URL.format(id=image_id, width=1600),
        'srcset': ', '.join(
            f'{UNSPLASH_URL.format(id=image_id, width=w)} {w}w' for w in (640, 1024, 1600, 2400)
        ),
        'alt': alt,
        'caption': caption,
        'photographer': photographer,
        'credit_url': f'https://unsplash.com/photos/{page}',
    }


def video(youtube_id, title, publisher):
    return {
        'id': youtube_id,
        'title': title,
        'publisher': publisher,
        'thumb': f'https://i.ytimg.com/vi/{youtube_id}/hqdefault.jpg',
        'watch_url': f'https://www.youtube.com/watch?v={youtube_id}',
    }


# ----------------------------------------------------------------------------
# Photos (reused in a few places, so defined once)
# ----------------------------------------------------------------------------

TOWER_ISLE = photo(
    '1539223583194-b66100fa7273',
    'Turquoise water around a small island seen from above',
    "A small island just off Tower Isle on Jamaica's north coast.",
    'Andrew Bui', 'aerial-photography-of-islan-56TWPYobJeU')

DUNNS_RIVER = photo(
    '1530225029356-e301a685e6b1',
    'Palm trees and sand at the water’s edge',
    "The shoreline at Dunn's River Falls & Park, Ocho Rios.",
    'Lakeisha Bennett', 'photo-of-beach-during-daytime-WAP2_qkTe18')

MONTEGO_BAY = photo(
    '1662505475505-cc7396a70a0c',
    'Aerial view of a coastal city and harbour',
    'Montego Bay from the air.',
    'Tyrone Sanders', 'an-aerial-view-of-a-city-NTuSXzly-lc')

RIVER_BOATS = photo(
    '1557129604-0e50f1300fab',
    'Boats tied up on a calm river lined with trees',
    'Boats moored on a Jamaican river.',
    'Yves Alarie', 'boats-docked-beside-trees-on-river-jIk3I_e16uw')

BLUE_MOUNTAIN_FOREST = photo(
    '1557129603-ff35a0c70e5e',
    'Forested mountain slopes under a blue sky',
    'Forest on the slopes of Blue Mountain.',
    'Yves Alarie', 'green-mountain-under-blue-sky-BXk-N2fPLYo')

BLUE_MOUNTAIN_PEAKS = photo(
    '1527017200692-2feca35f864f',
    'Mist drifting over green mountain peaks',
    'Mist over the Blue Mountain peaks, seen from Kingston.',
    'Marc Babin', 'green-mountain-during-daytime-r1nmJA6sXF8')

HANOVER = photo(
    '1659416071137-1b0e73ce261f',
    'A historic building with a clock tower',
    'The Parish Council building in Hanover.',
    'Kemoi Brown', 'a-building-with-a-clock-tower-M6Yrvga15cU')

KINGSTON = photo(
    '1579578160888-5f4ef4425b4b',
    'Aerial view of city buildings under a blue sky',
    'Kingston, around Red Hills Road.',
    'Caidrro', 'aerial-view-of-city-buildings-under-blue-sky-and-white-clouds-during-daytime-_52iqVQKEsU')

HUMMINGBIRD = photo(
    '1601233594980-20e3c716af3c',
    'A hummingbird hovering beside a pink flower',
    'A hummingbird at Hope Gardens, Kingston.',
    'Noctix', 'pink-flower-with-green-leaves-Y2WM7f5ExOM')

MARLEY_CONCERT = photo(
    '1597216634616-7a26f806705b',
    'Black-and-white photo of a band performing on stage before a crowd',
    'Bob Marley in concert at Western Springs, Auckland, New Zealand, '
    '16 April 1979. Shot on 35mm film.',
    'Bill Fairs', 'grayscale-photo-of-band-performing-on-stage-dOYhZEUtTxU')

MARLEY_ARRIVING = photo(
    '1538598450935-581f6a5fa7e0',
    'Bob Marley standing outdoors beside a woman',
    'Bob Marley arriving at his hotel in Auckland during his 1979 tour. Shot on 35mm film.',
    'Bill Fairs', 'bob-marley-standing-beside-woman-during-daytime-fMHdkScVfeY')

MARLEY_MURAL = photo(
    '1764444218813-787695615596',
    'A green-toned painted portrait of Bob Marley on a wall',
    'A painted portrait of Bob Marley.',
    'Caroline Badran', 'green-portrait-of-bob-marley-on-wall-vYIXDZNv2Mg')

ACKEE_SALTFISH = photo(
    '1632859965308-d15227508c4b',
    'A plate of ackee and saltfish with fried dumplings beside a cup of coffee',
    'Ackee and saltfish with fried dumplings, Kingston.',
    'Gabre Cameron', 'a-blue-plate-topped-with-food-next-to-a-cup-of-coffee-W4vDQETfroY')

JERK = photo(
    '1658833608786-22c4b4a621de',
    'Chicken cooking on a smoky grill',
    'Jerk chicken on the grill.',
    'Jopopz Tallorin', 'a-grill-with-meat-on-it-ofXy_NRwyjI')

NEGRIL_CYCLIST = photo(
    '1605994543054-6ffbabbd8139',
    'A man riding a bicycle past palm trees',
    'Cycling through the West End, Negril.',
    'Rock Staar', 'man-in-black-shirt-riding-bicycle-near-palm-tree-during-daytime-gksePWvWcWc')

NEGRIL_SIGN = photo(
    '1588300437037-b40c3ab2f3b2',
    'A blue wooden sign among palm trees',
    'A wooden sign among the palms in Negril.',
    'Rock Staar', 'blue-wooden-signage-near-palm-trees-during-daytime-N-5koXBkcTk')

FALMOUTH_MARKET = photo(
    '1614529168796-cb235d6a2557',
    'People walking through a busy street market',
    'A local market on the outskirts of Falmouth, Trelawny.',
    'JR Harris', 'people-walking-on-street-during-daytime-afVzV0gvnpY')


# ----------------------------------------------------------------------------
# Videos
# ----------------------------------------------------------------------------

UNESCO_REGGAE = video('olYYISLYLiU', 'Reggae music of Jamaica', 'UNESCO')
ONE_LOVE = video('IN0KkGeEURw', 'Bob Marley & The Wailers – One Love / People Get Ready',
                 'Official video · BobMarleyVEVO')
TOOTS_LIVE = video('EStJv_wsrdg', 'Toots & the Maytals live at Winterland, San Francisco, 1975',
                   'Official · Toots & the Maytals')
BOURDAIN_JERK = video('gUJlLHf5I_E', 'Anthony Bourdain on jerk chicken (Parts Unknown: Jamaica)', 'CNN')
MISS_LOU = video('tT_9jm3hzVw', 'Miss Lou on the Jamaican language', 'Archive footage via YouTube')
ACCOMPONG = video('Kx0witw7cdo', 'Accompong Maroon Festival in St Elizabeth', 'The Jamaica Gleaner')
MAROON_FEST = video('41-rLTtCbUM', 'Maroon Fest, 285th anniversary', 'The Jamaica Gleaner')


# ----------------------------------------------------------------------------
# Where everything goes
# ----------------------------------------------------------------------------

HOME = {
    'hero': TOWER_ISLE,
    'gallery': [DUNNS_RIVER, BLUE_MOUNTAIN_PEAKS, MONTEGO_BAY, RIVER_BOATS],
    'video': UNESCO_REGGAE,
}

# slug -> {'hero': photo, 'sections': {section heading: {'photo': ..., 'video': ...}}}
TOPIC_MEDIA = {
    'history': {
        'hero': BLUE_MOUNTAIN_FOREST,
        'sections': {
            'Key moments': {'photo': HANOVER},
            'The seven National Heroes': {'photo': KINGSTON},
            'Maroon heritage today': {'video': ACCOMPONG},
        },
    },
    'symbols': {
        'hero': HUMMINGBIRD,
        'sections': {
            'Natural heritage': {'photo': BLUE_MOUNTAIN_PEAKS},
        },
    },
    'music': {
        'hero': MARLEY_CONCERT,
        'sections': {
            'How the sound evolved': {'video': ONE_LOVE},
            'Sound system culture': {'photo': MARLEY_ARRIVING, 'video': TOOTS_LIVE},
            'Reggae, world heritage': {'photo': MARLEY_MURAL, 'video': UNESCO_REGGAE},
        },
    },
    'food': {
        'hero': ACKEE_SALTFISH,
        'sections': {
            'Dishes to know': {'photo': JERK, 'video': BOURDAIN_JERK},
        },
    },
    'language': {
        'hero': NEGRIL_CYCLIST,
        'sections': {
            'Everyday phrases': {'video': MISS_LOU},
            'Proverbs': {'photo': NEGRIL_SIGN},
        },
    },
    'festivals': {
        'hero': FALMOUTH_MARKET,
        'sections': {
            'Celebrations through the year': {'video': MAROON_FEST},
        },
    },
}
