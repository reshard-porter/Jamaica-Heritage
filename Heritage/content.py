"""
All the text for the Jamaican culture & heritage pages lives here.

To edit a page, change the text below. To add a whole new page, copy one of the
dictionaries in TOPICS, give it a new unique "slug" (used in the URL), and it
will appear in the navigation bar and on the heritage home page automatically.

Each topic has:
    slug     - the URL part, e.g. "music" -> /heritage/music/
    title    - page heading and nav label
    tagline  - one line shown under the heading
    summary  - short text for the card on the heritage home page
    intro    - opening paragraph
    sections - list of sections; each can have "paragraphs" and/or "entries"
               (name + text pairs, shown as cards). Don't name a key "items":
               Django templates would confuse it with Python's dict.items().
"""

TOPICS = [
    {
        'slug': 'history',
        'title': 'History & Heroes',
        'nav': 'History',
        'tagline': 'From Xaymaca to independence: the people who shaped the nation.',
        'summary': 'The Taíno, the Maroons, the long fight against slavery, and the '
                   'seven National Heroes honoured every October.',
        'intro': (
            "Jamaica's story is one of resistance and resilience. Long before Europeans "
            "arrived, the Taíno people called the island Xaymaca, often translated as "
            "\"land of wood and water.\" What followed was centuries of colonial rule and "
            "enslavement, and an equally long struggle for freedom that still shapes how "
            "Jamaicans see themselves today."
        ),
        'sections': [
            {
                'heading': 'Key moments',
                'entries': [
                    {'name': 'Before 1494',
                     'text': 'The Taíno live across the island, fishing, farming cassava and '
                             'making the flat cassava bread that survives today as bammy.'},
                    {'name': '1494',
                     'text': 'Christopher Columbus lands on the north coast. Spanish rule '
                             'follows, and the Taíno population is devastated by forced labour '
                             'and disease.'},
                    {'name': '1655',
                     'text': 'England captures Jamaica from Spain. Enslaved Africans flee to the '
                             'mountains and form free Maroon communities.'},
                    {'name': '1739-1740',
                     'text': 'After years of war, the British sign peace treaties with the '
                             'Leeward and Windward Maroons, recognising their land and freedom.'},
                    {'name': '1831-1832',
                     'text': 'Sam Sharpe leads the Christmas Rebellion, one of the largest '
                             'uprisings of enslaved people in the British Caribbean.'},
                    {'name': '1834 & 1838',
                     'text': 'Slavery is abolished on 1 August 1834, followed by a forced '
                             '"apprenticeship" period. Full freedom comes on 1 August 1838, now '
                             'celebrated as Emancipation Day.'},
                    {'name': '1865',
                     'text': 'The Morant Bay Rebellion, led by Paul Bogle, protests injustice '
                             'and poverty. It is brutally suppressed.'},
                    {'name': '1938',
                     'text': 'Labour unrest sweeps the island, giving rise to modern trade '
                             'unions and the two major political parties.'},
                    {'name': '6 August 1962',
                     'text': 'Jamaica becomes an independent nation. The black, green and gold '
                             'flag is raised for the first time.'},
                ],
            },
            {
                'heading': 'The seven National Heroes',
                'paragraphs': [
                    "The Order of National Hero is Jamaica's highest honour. The heroes are "
                    "celebrated on National Heroes Day, the third Monday in October, and many "
                    "are remembered at National Heroes Park in Kingston.",
                ],
                'entries': [
                    {'name': 'Nanny of the Maroons',
                     'text': 'Leader of the Windward Maroons in the Blue Mountains in the 1700s, '
                             'famed for her skill in guerrilla warfare against British forces. She '
                             'is the only woman among the National Heroes and appears on the '
                             '$500 note.'},
                    {'name': 'Sam Sharpe',
                     'text': 'A Baptist deacon who organised the 1831 Christmas Rebellion as a '
                             'peaceful strike that turned into a widespread uprising. He was '
                             'hanged in Montego Bay in 1832, and the rebellion helped speed the '
                             'end of slavery.'},
                    {'name': 'Paul Bogle',
                     'text': 'A Baptist deacon from Stony Gut, St Thomas, who led the 1865 '
                             'march on the Morant Bay courthouse demanding justice for poor '
                             'Jamaicans. He was executed for it.'},
                    {'name': 'George William Gordon',
                     'text': 'A landowner and legislator who spoke out against the treatment of '
                             'the poor. He was blamed for the Morant Bay Rebellion and hanged '
                             'under martial law.'},
                    {'name': 'Marcus Garvey',
                     'text': "Born in St Ann's Bay in 1887, he founded the Universal Negro "
                             'Improvement Association in 1914 and became one of the most '
                             'influential voices for Black pride and self-reliance worldwide.'},
                    {'name': 'Norman Manley',
                     'text': "A lawyer who founded the People's National Party in 1938 and "
                             'led the push for self-government and independence.'},
                    {'name': 'Sir Alexander Bustamante',
                     'text': 'A labour leader who founded the Bustamante Industrial Trade '
                             'Union and the Jamaica Labour Party, and became the first Prime '
                             'Minister of independent Jamaica in 1962.'},
                ],
            },
            {
                'heading': 'Maroon heritage today',
                'paragraphs': [
                    "Maroon communities still live in Jamaica today, in places such as "
                    "Accompong in St Elizabeth and Moore Town in Portland. Every 6 January, "
                    "the Accompong Maroons celebrate the 1739 peace treaty and the birthday of "
                    "their leader Cudjoe with drumming, the blowing of the abeng horn, "
                    "traditional food and a procession to the sacred Kindah tree.",
                ],
            },
        ],
    },
    {
        'slug': 'symbols',
        'title': 'National Symbols',
        'nav': 'Symbols',
        'tagline': 'Out of Many, One People.',
        'summary': 'The flag, the motto, the Doctor Bird, the Lignum Vitae and the other '
                   'symbols that represent the nation.',
        'intro': (
            "Jamaica's national motto, \"Out of Many, One People,\" reflects a nation built "
            "from African, European, Indian, Chinese, Middle Eastern and Taíno roots. The "
            "national symbols were chosen to represent the island's land, people and spirit."
        ),
        'sections': [
            {
                'heading': 'The flag',
                'paragraphs': [
                    "First raised on Independence Day, 6 August 1962, the flag has a gold "
                    "diagonal cross dividing it into green and black triangles. Its meaning is "
                    "often summed up in one line: \"The sun shineth, the land is green, and the "
                    "people are strong and creative.\" Gold stands for the sunlight and natural "
                    "wealth, green for the land and hope, and black for the strength and "
                    "creativity of the people.",
                ],
                'flag': True,
            },
            {
                'heading': 'Symbols of the nation',
                'entries': [
                    {'name': 'National Bird: the Doctor Bird',
                     'text': 'The red-billed streamertail hummingbird, found only in Jamaica. '
                             'The males have two long, flowing tail feathers.'},
                    {'name': 'National Flower: Lignum Vitae',
                     'text': 'Its small blue flowers bloom on a tree whose wood is one of the '
                             'hardest and heaviest in the world. The name means "wood of life."'},
                    {'name': 'National Tree: Blue Mahoe',
                     'text': 'A fast-growing native tree with blue-green streaked wood, prized '
                             'for furniture and carving.'},
                    {'name': 'National Fruit: Ackee',
                     'text': 'Brought from West Africa in the 18th century. Paired with '
                             'saltfish, it makes the national dish.'},
                    {'name': 'Coat of Arms',
                     'text': 'A Taíno man and woman stand either side of a shield with five '
                             'pineapples, beneath a crocodile crest and the national motto.'},
                    {'name': 'National Anthem',
                     'text': '"Jamaica, Land We Love," with words by Rev. Hugh Sherlock and '
                             'music by Robert Lightbourne.'},
                ],
            },
            {
                'heading': 'Natural heritage',
                'paragraphs': [
                    "The Blue and John Crow Mountains, home to the Windward Maroons and some of "
                    "the island's rarest plants and animals, were named a UNESCO World Heritage "
                    "Site in 2015 for both their natural and cultural value. The same mountains "
                    "grow the famous Blue Mountain coffee.",
                ],
            },
        ],
    },
    {
        'slug': 'music',
        'title': 'Music',
        'nav': 'Music',
        'tagline': 'A small island with a sound the whole world knows.',
        'summary': 'Mento, ska, rocksteady, reggae, dub and dancehall: how Jamaican music '
                   'went global.',
        'intro': (
            "Few countries of Jamaica's size have shaped world music so deeply. Its sounds "
            "grew out of African drumming traditions, church music, American rhythm and blues "
            "and the street-level energy of Kingston's sound systems. In 2015 Kingston was "
            "named a UNESCO Creative City of Music, and in 2018 UNESCO added reggae to its list "
            "of the world's Intangible Cultural Heritage."
        ),
        'sections': [
            {
                'heading': 'How the sound evolved',
                'entries': [
                    {'name': 'Mento',
                     'text': "Jamaica's rural folk music, played on banjo, guitar, hand drums "
                             'and the rumba box. Its playful, often cheeky lyrics are the root '
                             'of everything that followed.'},
                    {'name': 'Ska (late 1950s - early 1960s)',
                     'text': 'Fast, horn-driven and full of optimism, ska became the sound of '
                             'independence. The Skatalites defined it, and Millie Small\'s '
                             '"My Boy Lollipop" took it worldwide in 1964.'},
                    {'name': 'Rocksteady (mid-1960s)',
                     'text': 'The tempo slowed, the bass got heavier, and vocal harmony groups '
                             'took centre stage. Alton Ellis is often called its godfather.'},
                    {'name': 'Reggae (late 1960s onward)',
                     'text': 'Built on the "one drop" rhythm and often carrying messages of '
                             'faith, justice and unity. Bob Marley and the Wailers, Peter Tosh, '
                             'Toots and the Maytals and Jimmy Cliff brought it to the world.'},
                    {'name': 'Dub',
                     'text': 'Producers like King Tubby and Lee "Scratch" Perry stripped songs '
                             'down to drum and bass and added echo and reverb, inventing the '
                             'remix along the way.'},
                    {'name': 'Dancehall (late 1970s onward)',
                     'text': 'Faster, digital and built for the dance floor, with deejays '
                             'chatting over riddims. From Yellowman and Shabba Ranks to Beenie '
                             'Man and Spice, it remains the island\'s dominant sound.'},
                ],
            },
            {
                'heading': 'Sound system culture',
                'paragraphs': [
                    "Before Jamaican music filled the radio, it filled the yards and streets "
                    "through sound systems: huge home-built speaker stacks run by selectors "
                    "and deejays who talked, or \"toasted,\" over the records. Kingston-born DJ "
                    "Kool Herc carried that style to the Bronx in New York, where it became one "
                    "of the foundations of hip-hop.",
                ],
            },
            {
                'heading': 'Reggae, world heritage',
                'paragraphs': [
                    "In 2018 UNESCO inscribed \"Reggae music of Jamaica\" on its Representative "
                    "List of the Intangible Cultural Heritage of Humanity, recognising reggae's "
                    "role in giving a voice to the marginalised and in spreading messages of "
                    "social justice, resistance, love and humanity around the world.",
                ],
            },
        ],
    },
    {
        'slug': 'food',
        'title': 'Food',
        'nav': 'Food',
        'tagline': 'Bold spice, slow fire, and a history on every plate.',
        'summary': 'Ackee and saltfish, jerk, patties, rice and peas, and the stories '
                   'behind them.',
        'intro': (
            "Jamaican cooking tells the island's history. Taíno cassava, West African "
            "techniques, British baking, Indian curries and Chinese ingredients all meet in "
            "the same pot, brought together with scotch bonnet pepper, pimento (allspice) and "
            "fresh thyme."
        ),
        'sections': [
            {
                'heading': 'Dishes to know',
                'entries': [
                    {'name': 'Ackee and Saltfish',
                     'text': 'The national dish: buttery ackee sautéed with salted codfish, '
                             'onion, tomato and pepper. Usually served at breakfast with fried '
                             'dumplings, breadfruit or boiled green bananas.'},
                    {'name': 'Jerk',
                     'text': 'Chicken or pork rubbed with scotch bonnet, pimento and spices, '
                             'then slow-cooked over pimento wood. The technique is credited to '
                             'the Maroons, and Boston Bay in Portland is famous for it.'},
                    {'name': 'Rice and Peas',
                     'text': 'A Sunday dinner staple: rice cooked with kidney beans ("peas"), '
                             'coconut milk, thyme and a whole scotch bonnet.'},
                    {'name': 'Curry Goat',
                     'text': 'A legacy of Indian indentured workers who arrived from 1845. It '
                             'is a centrepiece at parties, weddings and celebrations.'},
                    {'name': 'Patties',
                     'text': 'Flaky golden pastry filled with spiced beef, chicken or '
                             'vegetables. Often eaten inside coco bread.'},
                    {'name': 'Escovitch Fish & Bammy',
                     'text': 'Fried fish topped with a tangy pickle of vinegar, onion, carrot '
                             'and pepper, served with bammy, the cassava bread inherited from '
                             'the Taíno.'},
                    {'name': 'Oxtail',
                     'text': 'Braised slowly until falling off the bone, with butter beans in '
                             'a rich, dark gravy.'},
                    {'name': 'Festival',
                     'text': 'A slightly sweet fried dumpling that is the classic partner for '
                             'jerk and fried fish.'},
                ],
            },
            {
                'heading': 'Seasonal favourites',
                'entries': [
                    {'name': 'Sorrel',
                     'text': 'A deep red Christmas drink made from hibiscus, ginger and '
                             'spices.'},
                    {'name': 'Bun and Cheese',
                     'text': 'Spiced Easter bun eaten with processed cheese, an Easter '
                             'tradition loved across the island.'},
                    {'name': 'Christmas Cake',
                     'text': 'Also called black cake: dried fruit soaked for weeks in rum and '
                             'wine, baked dark and rich.'},
                ],
            },
            {
                'heading': 'A note on ackee',
                'paragraphs': [
                    "Ackee must only be picked once its pod has opened naturally on the tree, "
                    "and only the cream-coloured flesh is eaten. Unripe ackee, and the seeds, "
                    "are poisonous. Jamaicans grow up knowing this rule, and it is worth "
                    "knowing before cooking it yourself.",
                ],
            },
        ],
    },
    {
        'slug': 'language',
        'title': 'Language & Patois',
        'nav': 'Language',
        'tagline': 'Wah gwaan? The voice of the people.',
        'summary': 'Jamaican Patois, everyday phrases, Anansi stories, and proverbs full of '
                   'wisdom.',
        'intro': (
            "English is Jamaica's official language, but the language of everyday life for "
            "most Jamaicans is Jamaican Patois (Patwa), also called Jamaican Creole. It grew "
            "from English mixed with West African languages, especially Akan, plus Spanish, "
            "Portuguese and other influences. Poet and folklorist Louise Bennett-Coverley, "
            "known as Miss Lou, spent her career showing that Patois is a full language worth "
            "celebrating, not \"broken English.\""
        ),
        'sections': [
            {
                'heading': 'Everyday phrases',
                'entries': [
                    {'name': 'Wah gwaan?', 'text': "What's going on? / How are you?"},
                    {'name': 'Mi deh yah', 'text': "I'm here / I'm doing alright."},
                    {'name': 'Irie', 'text': 'Good, fine, at peace.'},
                    {'name': 'Likkle more', 'text': 'See you later.'},
                    {'name': 'Soon come', 'text': "I'll be back soon (though maybe not that "
                                                  'soon).'},
                    {'name': 'Bless up', 'text': 'Best wishes; a warm goodbye.'},
                    {'name': 'Nuh worry yuhself', 'text': "Don't worry about it."},
                    {'name': 'Mi soon reach', 'text': "I'm almost there."},
                ],
            },
            {
                'heading': 'Proverbs',
                'paragraphs': [
                    "Jamaican proverbs pack a lot of wisdom into a few words. Grandparents use "
                    "them to teach, warn and tease.",
                ],
                'entries': [
                    {'name': 'One one coco full basket.',
                     'text': 'Little by little, the basket gets filled. Be patient.'},
                    {'name': 'Every mickle mek a muckle.',
                     'text': 'Small amounts add up to a lot.'},
                    {'name': 'Wanti wanti cyaan get it, an getti getti nuh want it.',
                     'text': "Those who want something can't get it, and those who have it "
                             "don't appreciate it."},
                    {'name': 'Tek kin teet kibba heart bun.',
                     'text': 'Use a smile to cover a heartache.'},
                    {'name': 'Wah sweet nanny goat a go run him belly.',
                     'text': 'What seems good now may cause trouble later.'},
                ],
            },
            {
                'heading': 'Anansi stories',
                'paragraphs': [
                    "Anansi the spider came to Jamaica with enslaved Akan people from West "
                    "Africa. He is a small trickster who outwits stronger animals with clever "
                    "schemes, and his stories were a way of keeping culture alive and quietly "
                    "celebrating the weak getting the better of the powerful. Many Anansi "
                    "stories end with the saying \"Jack Mandora, mi nuh choose none,\" meaning "
                    "the teller takes no responsibility for the tale.",
                ],
            },
        ],
    },
    {
        'slug': 'festivals',
        'title': 'Festivals & Traditions',
        'nav': 'Festivals',
        'tagline': 'Celebration, faith, and the spirit of the yard.',
        'summary': 'Jonkonnu, Emancipendence, Rastafari, Grand Market, and the island\'s love '
                   'of track and field.',
        'intro': (
            "Jamaica's calendar is full of celebrations that mix African traditions, Christian "
            "faith, and pride in the nation's history, all set to music."
        ),
        'sections': [
            {
                'heading': 'Celebrations through the year',
                'entries': [
                    {'name': 'Accompong Maroon Festival (6 January)',
                     'text': 'The Leeward Maroons of Accompong, St Elizabeth, mark the 1739 '
                             'peace treaty with drumming, the abeng horn, dancing and a '
                             'procession, drawing visitors from across the island and abroad.'},
                    {'name': 'Emancipendence (1-6 August)',
                     'text': 'Emancipation Day on 1 August and Independence Day on 6 August '
                             'are joined by a week of concerts, the Festival Song Competition '
                             'and the Grand Gala at the National Stadium.'},
                    {'name': 'National Heroes Day (October)',
                     'text': 'The third Monday in October honours the seven National Heroes '
                             'and others who have served the nation.'},
                    {'name': 'Jonkonnu (Christmas)',
                     'text': 'A masquerade of costumed dancers, including Pitchy-Patchy, Horse '
                             'Head, Cow Head and Belly Woman, parading to fife and drums. Its '
                             'roots go back to the days of slavery.'},
                    {'name': 'Grand Market (Christmas Eve)',
                     'text': 'Town centres stay open late into the night, packed with shoppers, '
                             'food stalls and music.'},
                    {'name': 'Easter',
                     'text': 'A time for church, family, bun and cheese, and fried fish on Good '
                             'Friday.'},
                ],
            },
            {
                'heading': 'Faith and spirit',
                'entries': [
                    {'name': 'Rastafari',
                     'text': 'A faith that began in Jamaica in the 1930s, inspired in part by '
                             "Marcus Garvey's teachings. Ethiopian Emperor Haile Selassie's "
                             'visit on 21 April 1966 is still marked as Grounation Day. '
                             'Rastafari shaped reggae, language and style around the world.'},
                    {'name': 'Revival and Kumina',
                     'text': 'Revival blends African and Christian worship with drumming and '
                             'trance. Kumina, with strong Central African (Kongo) roots, is '
                             'especially associated with St Thomas.'},
                ],
            },
            {
                'heading': 'Sport',
                'paragraphs': [
                    "Track and field is close to a national passion. The ISSA Boys' and Girls' "
                    "Athletics Championships, known simply as \"Champs\" and held since 1910, "
                    "fill the National Stadium every year and have launched stars like Usain "
                    "Bolt, Shelly-Ann Fraser-Pryce and Merlene Ottey. Jamaicans also love "
                    "cricket and football, and the 1988 bobsled team showed the world that a "
                    "tropical island could compete at the Winter Olympics.",
                ],
            },
        ],
    },
]

TOPICS_BY_SLUG = {topic['slug']: topic for topic in TOPICS}
