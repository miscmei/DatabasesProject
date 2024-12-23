import random
import datetime
import mariadb

# characters to insert and genres
# each character name is unqiue, so can be used as a dictionary key
characters = {
    'Gandalf':'Fantasy',
    'Frodo':'Fantasy',
    'Ron Weasley':'Fantasy',
    'A Rock':'Object',
    'Gushers':'Object',
    'Noble 6':'Fantasy',
    'Expo Marker':'Object',
    'Anand Basu':'Real Person',
    'Maddy Fung':'Real Person',
    'Moby Dick Hardcover':'Object',
    'Batman':'Fantasy',
    'Spider-Man':'Fantasy',
    'Captain America':'Fantasy',
    'Black Panther':'Fantasy',
    'Pine Tree':'Object',
    'Birch Tree':'Object',
    'Grandfather Clock':'Object',
    'Jude Bellingham':'Real Person',
    'Ace of Spades':'Object',
    'Erling Haaland':'Real Person',
    'Lewis Hamilton':'Real Person',
    'Michael Schumacher':'Real Person',
    'Abraham Lincoln':'Historical Figure',
    'Geroge Washington':'Historical Figure',
    'Gandhi':'Historical Figure',
    'Socrates':'Historical Figure',
    'Plato':'Historical Figure',
    'Renault R26':'Object',
    'RB19':'Object',
    'Dacia Sandero':'Object',
    'Large Hadron Collider':'Object',
    'Mt. Fuji':'Object',
    'Mt. Everest':'Object',
    'Subaru WRX STI':'Object',
    'Subaru Forester':'Object',
    'Subaru Outback':'Object',
    'Subaru Legacy':'Object',
    'Honda Odyssey':'Object',
    'Honda Civic':'Object',
    'Honda CRV':'Object',
    'Honda HRV':'Object',
    'Barack Obama':'Real Person',
    'Joe Biden':'Real Person',
    'Hillary Clinton':'Real Person',
    'Kamala Harris':'Real Person',
    'Vladimir Putin':'Real Person',
    'Donald Trump':'Real Person',
    'Bill Clinton':'Real Person',
    'Greta Thunberg':'Real Person',
    'Nancy Pelosi':'Real Person',
    "Rishi Sunak": "Real Person",
	"Boris Johnson": "Real Person",
	"Liz Truss": "Real Person",
	"Emmanuel Macron": "Real Person",
	"Angela Merkel": "Real Person",
	"Olaf Scholz": "Real Person",
	"Justin Trudeau": "Real Person",
	"Andrés Manuel López Obrador": "Real Person",
	"Luiz Inácio Lula da Silva": "Real Person",
	"Jair Bolsonaro": "Real Person",
	"Narendra Modi": "Real Person",
	"Xi Jinping": "Real Person",
	"Yoon Suk-yeol": "Real Person",
	"Fumio Kishida": "Real Person",
	"Volodymyr Zelenskyy": "Real Person",
	"Vladimir Putin": "Real Person",
	"Giorgia Meloni": "Real Person",
	"Recep Tayyip Erdogan": "Real Person",
	"Benjamin Netanyahu": "Real Person",
	"Jacinda Ardern": "Real Person",
	"John Howard": "Real Person",
	"Cyril Ramaphosa": "Real Person",
	"Robert F. Kennedy Jr.": "Real Person",
    'Gabriel Jesus':'Real Person',
    'Gabriel Martinelli':'Real Person',
    'Bukayo Saka':'Real Person',
    'Martin Odegaard':'Real Person',
    'Kai Havertz':'Real Person',
    'Declan Rice':'Real Person',
    'Thomas Partey':'Real Person',
    'Ethan Nwaneri':'Real Person',
    'Gabriel Magalhaes':'Real Person',
    'William Saliba':'Real Person',
    'Ben White':'Real Person',
    'Jurrien Timber':'Real Person',
    'Takehiro Tomiyasu':'Real Person',
    'Olexander Zinchenko':'Real Person',
    'Ricciardo Calafiori':'Real Person',
    'Jakub Kiwior':'Real Person',
    'Raheem Sterling':'Real Person',
    'Reiss Nelson':'Real Person',
    'David Raya':'Real Person',
    'Tommy Setford':'Real Person',
    'Neto':'Real Person',
    'Mikel Arteta':'Real Person',
    'Jorginho':'Real Person',
    'Myles Lewis-Skelley':'Real Person',
    'Emile Smith-Rowe':'Real Person',
    'Kevin DeBruyne':'Real Person',
    'Ederson':'Real Person',
    'Mohammad Salah':'Real Person',
    'Jack Grealish':'Real Person',
    'Nathan Ake':'Real Person',
    'Ruben Dias':'Real Person',
    'Josko Gvardiol':'Real Person',
    'Pep Guardiola':'Real Person',
    'Arne Slot':'Real Person',
    'Jurgen Klopp':'Real Person',
    'Lamine Yamal':'Real Person',
    'Raphina':'Real Person',
    'Dani Olmo':'Real Person',
    'Kylian Mbappe':'Real Person',
    'Jude Bellingham':'Real Person',
    "Table": "Object",
	"Lamp": "Object",
	"Pen": "Object",
	"Notebook": "Object",
	"Backpack": "Object",
	"Coffee mug": "Object",
	"Water bottle": "Object",
	"Television": "Object",
	"Smartphone": "Object",
	"Keyboard": "Object",
	"Mouse": "Object",
	"Book": "Object",
	"Clock": "Object",
	"Blanket": "Object",
	"Pillow": "Object",
	"Door": "Object",
	"Window": "Object",
	"Mirror": "Object",
	"Carpet": "Object",
	"Vase": "Object",
	"Candle": "Object",
	"Picture frame": "Object",
	"Guitar": "Object",
	"Refrigerator": "Object",
	"Washing machine": "Object",
	"Bicycle": "Object",
	"Umbrella": "Object",
	"Headphones": "Object",
	"Toaster": "Object",
    "Eragon": "Fantasy",
	"Saphira": "Fantasy",
	"Ged": "Fantasy",
	"Elric of Melniboné": "Fantasy",
	"Morgana le Fay": "Fantasy",
	"Drizzt Do'Urden": "Fantasy",
	"Ciri": "Fantasy",
	"Geralt of Rivia": "Fantasy",
	"Kvothe": "Fantasy",
	"Aelin Galathynius": "Fantasy",
	"FitzChivalry Farseer": "Fantasy",
	"Nighteyes": "Fantasy",
	"Pug": "Fantasy",
	"Raistlin Majere": "Fantasy",
	"Tasslehoff Burrfoot": "Fantasy",
	"Polgara the Sorceress": "Fantasy",
	"Belgarath the Sorcerer": "Fantasy",
	"Althea Vestrit": "Fantasy",
	"Paragon": "Fantasy",
	"Severian": "Fantasy",
	"Shadowthrone": "Fantasy",
	"Anomander Rake": "Fantasy",
	"Karsa Orlong": "Fantasy",
	"Vin": "Fantasy",
	"Kelsier": "Fantasy",
	"Shallan Davar": "Fantasy",
	"Kaladin Stormblessed": "Fantasy",
	"Dalinar Kholin": "Fantasy",
	"Moiraine Damodred": "Fantasy",
	"Rand al'Thor": "Fantasy",
    "Egwene al'Vere": "Fantasy",
	"Mat Cauthon": "Fantasy",
	"Perrin Aybara": "Fantasy",
	"Thom Merrilin": "Fantasy",
	"Lan Mandragoran": "Fantasy",
	"Lyra Silvertongue": "Fantasy",
	"Iorek Byrnison": "Fantasy",
	"Will Parry": "Fantasy",
	"Asriel Belacqua": "Fantasy",
	"Mrs. Coulter": "Fantasy",
	"Sabriel": "Fantasy",
	"Mogget": "Fantasy",
	"Lirael": "Fantasy",
	"Sameth": "Fantasy",
	"Garion": "Fantasy",
	"Ce'Nedra": "Fantasy",
	"Zeddicus Zu'l Zorander": "Fantasy",
	"Richard Rahl": "Fantasy",
	"Kahlan Amnell": "Fantasy",
	"Cara Mason": "Fantasy",
	"Rincewind": "Fantasy",
	"Granny Weatherwax": "Fantasy",
	"Nanny Ogg": "Fantasy",
	"Samuel Vimes": "Fantasy",
	"Tiffany Aching": "Fantasy",
	"Death": "Fantasy",
	"Corwin of Amber": "Fantasy",
	"Benedict of Amber": "Fantasy",
	"Fiona of Amber": "Fantasy",
	"Random of Amber": "Fantasy",
    "Hammurabi": "Historical Figure",
	"Catherine the Great": "Historical Figure",
	"Elizabeth II": "Historical Figure",
	"Simon Bolivar": "Historical Figure",
	"William Shakespeare": "Historical Figure",
	"Ludwig van Beethoven": "Historical Figure",
	"Wolfgang Amadeus Mozart": "Historical Figure",
	"Vincent van Gogh": "Historical Figure",
	"Frida Kahlo": "Historical Figure",
	"Diego Rivera": "Historical Figure",
	"Pablo Picasso": "Historical Figure",
	"Theodore Roosevelt": "Historical Figure",
	"Franklin D. Roosevelt": "Historical Figure",
	"John F. Kennedy": "Historical Figure",
	"The Dalai Lama (14th)": "Historical Figure",
	"Nelson Mandela": "Historical Figure",
	"Desmond Tutu": "Historical Figure",
	"Mother Teresa": "Historical Figure",
	"Malcolm X": "Historical Figure",
	"John Locke": "Historical Figure",
	"Jean-Jacques Rousseau": "Historical Figure",
	"Voltaire": "Historical Figure",
	"Karl Marx": "Historical Figure",
	"Friedrich Nietzsche": "Historical Figure",
	"Ada Lovelace": "Historical Figure",
	"Alan Turing": "Historical Figure",
	"Jane Austen": "Historical Figure",
	"Charlotte Brontë": "Historical Figure",
	"Emily Dickinson": "Historical Figure",
	"Susan B. Anthony": "Historical Figure",
    "Babe Ruth": "Real Person",
	"Willie Mays": "Real Person",
	"Hank Aaron": "Real Person",
	"Ted Williams": "Real Person",
	"Jackie Robinson": "Real Person",
	"Derek Jeter": "Real Person",
	"Mickey Mantle": "Real Person",
	"Ken Griffey Jr.": "Real Person",
	"Barry Bonds": "Real Person",
	"Mike Trout": "Real Person",
	"Clayton Kershaw": "Real Person",
	"Randy Johnson": "Real Person",
	"Pedro Martinez": "Real Person",
	"Greg Maddux": "Real Person",
	"Ichiro Suzuki": "Real Person",
	"Albert Pujols": "Real Person",
	"Shohei Ohtani": "Real Person",
	"Nolan Ryan": "Real Person",
	"Cal Ripken Jr.": "Real Person",
	"Chipper Jones": "Real Person",
	"Frank Thomas": "Real Person",
	"Tom Seaver": "Real Person",
	"Sandy Koufax": "Real Person",
	"Yogi Berra": "Real Person",
	"Joe DiMaggio": "Real Person",
	"Roger Clemens": "Real Person",
	"David Ortiz": "Real Person",
	"Mariano Rivera": "Real Person",
	"Alex Rodriguez": "Real Person",
	"Tony Gwynn": "Real Person",
	"Roberto Clemente": "Real Person",
	"Lou Gehrig": "Real Person",
	"Stan Musial": "Real Person",
	"Carl Yastrzemski": "Real Person",
	"Ryne Sandberg": "Real Person",
	"Johnny Bench": "Real Person",
	"Ozzie Smith": "Real Person",
	"Eddie Murray": "Real Person",
	"Paul Molitor": "Real Person",
	"George Brett": "Real Person",
	"Harmon Killebrew": "Real Person",
	"Brooks Robinson": "Real Person",
	"Bob Gibson": "Real Person",
	"Fergie Jenkins": "Real Person",
	"Wade Boggs": "Real Person",
	"Reggie Jackson": "Real Person",
	"Jim Thome": "Real Person",
	"Mike Piazza": "Real Person",
	"Ricky Henderson": "Real Person",
	"Tim Lincecum": "Real Person",
    "Bryce Harper": "Real Person",
	"Fernando Tatis Jr.": "Real Person",
	"Vladimir Guerrero Jr.": "Real Person",
	"Ronald Acuña Jr.": "Real Person",
	"Mookie Betts": "Real Person",
	"Aaron Judge": "Real Person",
	"Gerrit Cole": "Real Person",
	"Jacob deGrom": "Real Person",
	"Max Scherzer": "Real Person",
	"Justin Verlander": "Real Person",
	"Francisco Lindor": "Real Person",
	"Corey Seager": "Real Person",
	"Freddie Freeman": "Real Person",
	"Joey Votto": "Real Person",
	"Manny Machado": "Real Person",
	"Jose Altuve": "Real Person",
	"Carlos Correa": "Real Person",
	"Trea Turner": "Real Person",
	"Matt Olson": "Real Person",
	"Nolan Arenado": "Real Person",
	"Paul Goldschmidt": "Real Person",
	"Yordan Alvarez": "Real Person",
	"Kyle Tucker": "Real Person",
	"Julio Rodríguez": "Real Person",
	"Adley Rutschman": "Real Person",
	"Austin Riley": "Real Person",
	"Dansby Swanson": "Real Person",
	"Rafael Devers": "Real Person",
	"Xander Bogaerts": "Real Person",
	"Josh Hader": "Real Person",
	"Craig Kimbrel": "Real Person",
	"Zack Greinke": "Real Person",
	"Stephen Strasburg": "Real Person",
	"Blake Snell": "Real Person",
	"Shane Bieber": "Real Person",
	"Christian Yelich": "Real Person",
	"Kris Bryant": "Real Person",
	"Anthony Rizzo": "Real Person",
	"Javier Báez": "Real Person",
	"Andrew McCutchen": "Real Person",
	"Buster Posey": "Real Person",
	"Hunter Pence": "Real Person",
	"Cody Bellinger": "Real Person",
	"Trevor Bauer": "Real Person",
	"Josh Donaldson": "Real Person",
	"Jose Ramirez": "Real Person",
	"Salvador Perez": "Real Person",
	"Eloy Jimenez": "Real Person",
	"Luis Robert": "Real Person",
	"Shane McClanahan": "Real Person",
    "Jorge":'Fantasy',
    'Emile':'Fantasy',
    'Cortana':'Fantasy',
    "Notebook": "Object",
	"Pen": "Object",
	"Pencil": "Object",
	"Eraser": "Object",
	"Sharpener": "Object",
	"Ruler": "Object",
	"Backpack": "Object",
	"Folder": "Object",
	"Binder": "Object",
	"Highlighter": "Object",
	"Glue Stick": "Object",
	"Scissors": "Object",
	"Calculator": "Object",
	"Whiteboard Marker": "Object",
	"Index Cards": "Object",
	"Sticky Notes": "Object",
	"Stapler": "Object",
	"Paper Clips": "Object",
	"Printer Paper": "Object",
	"Laptop": "Object",
	"Tablet": "Object",
	"USB Drive": "Object",
	"Desk": "Object",
	"Chair": "Object",
	"Compass": "Object",
	"Protractor": "Object",
	"Textbook": "Object",
	"School Planner": "Object",
	"Lunchbox": "Object",
    "Football": "Object",
	"Basketball": "Object",
	"Soccer Ball": "Object",
	"Tennis Racket": "Object",
	"Baseball Bat": "Object",
	"Baseball Glove": "Object",
	"Hockey Stick": "Object",
	"Ice Skates": "Object",
	"Cricket Bat": "Object",
	"Golf Club": "Object",
	"Golf Ball": "Object",
	"Badminton Racket": "Object",
	"Ping Pong Paddle": "Object",
	"Volleyball": "Object",
	"Rugby Ball": "Object",
	"Swimming Goggles": "Object",
	"Swimming Cap": "Object",
	"Boxing Gloves": "Object",
	"Boxing Ring": "Object",
	"Football Helmet": "Object",
	"Basketball Hoop": "Object",
	"Tennis Net": "Object",
	"Soccer Cleats": "Object",
	"Skateboard": "Object",
	"Skis": "Object",
	"Snowboard": "Object",
	"Surfboard": "Object",
	"Tennis Balls": "Object",
	"Basketball Shoes": "Object",
	"Track Spikes": "Object",
	"Hurdles": "Object",
	"Gymnastic Rings": "Object",
	"Jump Rope": "Object",
	"Bicycle": "Object",
	"Cycling Helmet": "Object",
	"Soccer Shin Guards": "Object",
	"Hockey Puck": "Object",
	"Tennis Shoes": "Object",
	"Archery Bow": "Object",
	"Archery Arrows": "Object",
	"Kettlebell": "Object",
	"Dumbbell": "Object",
	"Barbell": "Object",
	"Resistance Bands": "Object",
	"Exercise Ball": "Object",
	"Yoga Mat": "Object",
	"Baseball Cleats": "Object",
	"Football Pads": "Object",
	"Wrestling Mat": "Object",
	"Paddleboard": "Object",
    "Zeus": "God",
	"Hera": "God",
	"Poseidon": "God",
	"Hades": "God",
	"Apollo": "God",
	"Artemis": "God",
	"Athena": "God",
	"Ares": "God",
	"Demeter": "God",
	"Hermes": "God",
	"Dionysus": "God",
	"Hephaestus": "God",
	"Apollo": "God",
	"Osiris": "God",
	"Ra": "God",
	"Horus": "God",
	"Anubis": "God",
	"Bastet": "God",
	"Isis": "God",
	"Thor": "God",
	"Odin": "God",
	"Freya": "God",
	"Loki": "God",
	"Brahma": "God",
	"Vishnu": "God",
	"Shiva": "God",
	"Lakshmi": "God",
	"Durga": "God",
	"Ganesh": "God",
	"Quetzalcoatl": "God",
    "Amun": "God",
	"Neith": "God",
	"Sekhmet": "God",
	"Ptah": "God",
	"Tefnut": "God",
	"Thoth": "God",
	"Geb": "God",
	"Shu": "God",
	"Nut": "God",
	"Hathor": "God",
	"Osiris": "God",
	"Bast": "God",
	"Anubis": "God",
	"Chac": "God",
	"Ix Chel": "God",
	"Tezcatlipoca": "God",
	"Xipe Totec": "God",
	"Tlaloc": "God",
	"Quetzalcoatl": "God",
	"Huitzilopochtli": "God",
	"Tonatiuh": "God",
	"Ometeotl": "God",
	"Xolotl": "God",
	"Pachamama": "God",
	"Inti": "God",
	"Viracocha": "God",
	"Atahualpa": "God",
	"Tupan": "God",
	"Nanahuatzin": "God",
	"Wakan Tanka": "God",
	"Taweret": "God",
	"Ishtar": "God",
	"Marduk": "God",
	"Enlil": "God",
	"Enki": "God",
	"Ashur": "God",
	"Baal": "God",
	"Dagon": "God",
	"Melqart": "God",
	"Cernunnos": "God",
	"Brigid": "God",
	"Lugh": "God",
	"The Dagda": "God",
	"Scathach": "God",
	"Hecate": "God",
	"Epona": "God",
	"Veles": "God",
	"Perun": "God",
	"Svarog": "God",
	"Mokosh": "God",
    "Apple": "Object",
	"Banana": "Object",
	"Carrot": "Object",
	"Tomato": "Object",
	"Cucumber": "Object",
	"Lettuce": "Object",
	"Spinach": "Object",
	"Potato": "Object",
	"Onion": "Object",
	"Garlic": "Object",
	"Broccoli": "Object",
	"Cauliflower": "Object",
	"Peas": "Object",
	"Corn": "Object",
	"Cabbage": "Object",
	"Eggplant": "Object",
	"Zucchini": "Object",
	"Bell Pepper": "Object",
	"Mushroom": "Object",
	"Avocado": "Object",
	"Asparagus": "Object",
	"Brussels Sprouts": "Object",
	"Sweet Potato": "Object",
	"Pumpkin": "Object",
	"Radish": "Object",
	"Chili Pepper": "Object",
	"Cantaloupe": "Object",
	"Watermelon": "Object",
	"Pineapple": "Object",
	"Mango": "Object",
	"Strawberry": "Object",
	"Blueberry": "Object",
	"Raspberry": "Object",
	"Blackberry": "Object",
	"Peach": "Object",
	"Plum": "Object",
	"Grapes": "Object",
	"Orange": "Object",
	"Lemon": "Object",
	"Lime": "Object",
	"Cherry": "Object",
	"Kiwi": "Object",
	"Papaya": "Object",
	"Figs": "Object",
	"Dates": "Object",
	"Pomegranate": "Object",
	"Melon": "Object",
	"Almond": "Object",
	"Cashew": "Object",
	"Walnut": "Object",
	"Pistachio": "Object",
	"Peanut": "Object",
	"Sunflower Seeds": "Object",
	"Sesame Seeds": "Object",
	"Chia Seeds": "Object",
	"Flax Seeds": "Object",
	"Oats": "Object",
	"Quinoa": "Object",
	"Rice": "Object",
	"Barley": "Object",
	"Wheat": "Object",
	"Spaghetti": "Object",
	"Macaroni": "Object",
	"Ravioli": "Object",
	"Lasagna": "Object",
	"Pizza": "Object",
	"Bread": "Object",
	"Bagel": "Object",
	"Croissant": "Object",
	"Donut": "Object",
	"Muffin": "Object",
	"Pancake": "Object",
	"Waffle": "Object",
	"French Toast": "Object",
	"Cheese": "Object",
	"Butter": "Object",
	"Yogurt": "Object",
	"Milk": "Object",
	"Cream": "Object",
	"Ice Cream": "Object",
	"Chocolate": "Object",
	"Candy": "Object",
	"Cookie": "Object",
	"Cake": "Object",
	"Pie": "Object",
	"Brownie": "Object",
	"Cupcake": "Object",
	"Tart": "Object",
	"Mousse": "Object",
	"Gelato": "Object",
	"Sushi": "Object",
	"Taco": "Object",
	"Burrito": "Object",
	"Sandwich": "Object",
	"Hot Dog": "Object",
	"Burger": "Object",
	"Steak": "Object",
	"Chicken": "Object",
	"Pork": "Object",
	"Fish": "Object",
	"Shrimp": "Object",
	"Lobster": "Object",
	"Crab": "Object",
	"Egg": "Object",
	"Tofu": "Object",
	"Tempeh": "Object",
	"Seitan": "Object",
	"Falafel": "Object",
	"Hummus": "Object",
	"Guacamole": "Object",
	"Salsa": "Object",
    'David Villa':'Real Person',
    'Lionel Messi':'Real Person',
    'R9':'Real Person',
    'Viktor Gyokeres':'Real Person',
    'Zlatan Ibrahimovic':'Real Person',
    'Alexander Isak':'Real Person',
    'Harry Kane':'Real Person',
    'Antoine Griezmann':'Real Person',
    'Rodrigo DePaul':'Real Person',
    'Lionel Scaloni':'Real Person',
    'Aurelian Tchouameni':'Real Person',
    'Eduardo Camavinga':'Real Person',
    'Cody Gakpo':'Real Person',
    'Diogo Jota':'Real Person',
    'Luis Diaz':'Real Person',
    "Rose": "Object",
	"Tulip": "Object",
	"Sunflower": "Object",
	"Lily": "Object",
	"Daisy": "Object",
	"Orchid": "Object",
	"Cactus": "Object",
	"Lavender": "Object",
	"Iris": "Object",
	"Violet": "Object",
	"Daffodil": "Object",
	"Chrysanthemum": "Object",
	"Marigold": "Object",
	"Jasmine": "Object",
	"Geranium": "Object",
	"Begonia": "Object",
	"Pansy": "Object",
	"Carnation": "Object",
	"Zinnia": "Object",
	"Azalea": "Object",
	"Camellia": "Object",
	"Magnolia": "Object",
	"Fuchsia": "Object",
	"Gardenia": "Object",
	"Amaryllis": "Object",
	"Gerbera Daisy": "Object",
	"Primrose": "Object",
	"Petunia": "Object",
	"Coleus": "Object",
	"Snapdragon": "Object",
	"Aster": "Object",
	"Lobelia": "Object",
	"Poppy": "Object",
	"Hibiscus": "Object",
	"Buttercup": "Object",
	"Ferns": "Object",
	"Hosta": "Object",
	"Dandelion": "Object",
	"Holly": "Object",
	"Juniper": "Object",
	"Ivy": "Object",
	"Cypress": "Object",
	"Pine": "Object",
	"Fir": "Object",
	"Spruce": "Object",
	"Redwood": "Object",
	"Willow": "Object",
	"Oak": "Object",
	"Maple": "Object",
	"Birch": "Object",
	"Aspen": "Object",
	"Sequoia": "Object",
	"Cedar": "Object",
	"Alder": "Object",
	"Elm": "Object",
	"Ash": "Object",
	"Sycamore": "Object",
	"Bamboo": "Object",
	"Moss": "Object",
	"Kale": "Object",
	"Spider Plant": "Object",
	"Peace Lily": "Object",
	"Fiddle Leaf Fig": "Object",
	"Succulent": "Object",
	"Aloe Vera": "Object",
	"Bonsai": "Object",
	"Monstera": "Object",
	"Philodendron": "Object",
	"Snake Plant": "Object",
	"Chinese Evergreen": "Object",
	"Pothos": "Object",
	"English Ivy": "Object",
	"African Violet": "Object",
	"Calatheas": "Object",
	"ZZ Plant": "Object",
	"Bird of Paradise": "Object",
	"Ginger Plant": "Object",
	"Bougainvillea": "Object",
	"Plumeria": "Object",
	"Hoya": "Object",
	"Ficus": "Object",
	"Kalanchoe": "Object",
	"Pilea": "Object",
	"Cyclamen": "Object",
	"Lemongrass": "Object",
	"Lavender": "Object",
	"Chili Pepper Plant": "Object",
	"Maranta": "Object",
	"Basil": "Object",
	"Sweet Pea": "Object",
	"Yarrow": "Object",
	"Heliconia": "Object",
	"Canna Lily": "Object",
	"Black-eyed Susan": "Object",
	"Butterfly Bush": "Object",
	"Coneflower": "Object",
	"Daylily": "Object",
	"Hens and Chicks": "Object",
	"Kalanchoe": "Object",
	"Golden Pothos": "Object",
	"Gerbera Daisy": "Object",
	"Chive": "Object",
	"Sage": "Object",
	"Lavender": "Object",
	"Mimosa": "Object",
	"Morning Glory": "Object",
	"Wisteria": "Object",
	"Trillium": "Object",
	"String of Pearls": "Object",
	"Katniss": "Object",
    "Katniss Everdeen": "Fantasy",
	"Peeta Mellark": "Fantasy",
	"Gale Hawthorne": "Fantasy",
	"Primrose Everdeen": "Fantasy",
	"Effie Trinket": "Fantasy",
	"Haymitch Abernathy": "Fantasy",
	"Cinna": "Fantasy",
	"Rue": "Fantasy",
	"Foxface": "Fantasy",
	"Thresh": "Fantasy",
	"Clove": "Fantasy",
	"Marvel": "Fantasy",
	"Glimmer": "Fantasy",
	"Brutus": "Fantasy",
	"Enobaria": "Fantasy",
	"Cato": "Fantasy",
	"Marvel": "Fantasy",
	"Portia": "Fantasy",
	"Tigris": "Fantasy",
	"President Snow": "Fantasy",
	"Plutarch Heavensbee": "Fantasy",
	"Annie Cresta": "Fantasy",
	"Johanna Mason": "Fantasy",
	"Finnick Odair": "Fantasy",
	"Mags": "Fantasy",
	"Delly Cartwright": "Fantasy",
	"Darius": "Fantasy",
	"Greasy Sae": "Fantasy",
	"Madge Undersee": "Fantasy",
    "Spider-Man": "Fantasy",
	"Hulk": "Fantasy",
	"Black Widow": "Fantasy",
	"Black Panther": "Fantasy",
	"Doctor Strange": "Fantasy",
	"Ant-Man": "Fantasy",
	"Hawkeye": "Fantasy",
	"Wolverine": "Fantasy",
	"Storm": "Fantasy",
	"Cyclops": "Fantasy",
	"Jean Grey": "Fantasy",
	"Professor X": "Fantasy",
	"Deadpool": "Fantasy",
	"Daredevil": "Fantasy",
	"Luke Cage": "Fantasy",
	"Jessica Jones": "Fantasy",
	"The Flash": "Fantasy",
	"Green Lantern": "Fantasy",
	"Wonder Woman": "Fantasy",
	"Aquaman": "Fantasy",
	"Superman": "Fantasy",
	"Batman": "Fantasy",
	"Green Arrow": "Fantasy",
	"Shazam": "Fantasy",
	"Martian Manhunter": "Fantasy",
	"The Atom": "Fantasy",
	"Raven": "Fantasy",
	"Beast Boy": "Fantasy",
	"Cyborg": "Fantasy",
	"Starfire": "Fantasy",
	"Nightwing": "Fantasy",
	"Batgirl": "Fantasy",
	"The Flash": "Fantasy",
	"Hawkwoman": "Fantasy",
	"Power Girl": "Fantasy",
	"Blue Beetle": "Fantasy",
	"The Spectre": "Fantasy",
	"Vixen": "Fantasy",
	"Doctor Fate": "Fantasy",
	"Mister Miracle": "Fantasy",
	"Zatanna": "Fantasy",
	"The Question": "Fantasy",
	"Captain Marvel": "Fantasy",
	"Ms. Marvel": "Fantasy",
	"Spider-Woman": "Fantasy",
	"Venom": "Fantasy",
	"She-Hulk": "Fantasy",
	"Ghost Rider": "Fantasy",
	"Moon Knight": "Fantasy",
    "Sébastien Loeb": "Real Person",
	"Sébastien Ogier": "Real Person",
	"Colin McRae": "Real Person",
	"Tommi Mäkinen": "Real Person",
	"Jari-Matti Latvala": "Real Person",
	"Carlos Sainz": "Real Person",
	"Mikko Hirvonen": "Real Person",
	"Petter Solberg": "Real Person",
	"Kimi Räikkönen": "Real Person",
	"Richard Burns": "Real Person",
	"Evgeny Novikov": "Real Person",
	"Thierry Neuville": "Real Person",
	"Ott Tänak": "Real Person",
	"Dani Sordo": "Real Person",
	"Craig Breen": "Real Person",
	"Elfyn Evans": "Real Person",
	"Andreas Mikkelsen": "Real Person",
	"Gus Greensmith": "Real Person",
	"Lorenzo Bertelli": "Real Person",
	"Andreucci Paolo": "Real Person",
	"Ken Block": "Real Person",
	"David Higgins": "Real Person",
	"Juho Hänninen": "Real Person",
	"Nasser Al-Attiyah": "Real Person",
	"Mads Østberg": "Real Person",
	"Jost Capito": "Real Person",
	"Marcus Grönholm": "Real Person",
	"Walter Röhrl": "Real Person",
	"Armin Schwarz": "Real Person",
	"Bryan Bouffier": "Real Person",
	"Kris Meeke": "Real Person",
	"Gigi Galli": "Real Person",
	"Henning Solberg": "Real Person",
	"Timo Salonen": "Real Person",
	"François Duval": "Real Person",
	"Patrick Snijers": "Real Person",
	"Guy Wilks": "Real Person",
	"Jari-Kari Latvala": "Real Person",
	"Daniel Elena": "Real Person",
	"Fabrizio Zanni": "Real Person",
	"Romain Dumas": "Real Person",
	"Sven Smeets": "Real Person",
	"Luc Alphalain": "Real Person",
	"Vladimir Vasilyev": "Real Person",
	"Jonas Andersson": "Real Person",
	"Gérard Marcy": "Real Person",
	"Alister McRae": "Real Person",
	"Nicolas Vouilloz": "Real Person",
	"Michael Park": "Real Person",
	"Mattias Ekström": "Real Person",
	"Hermann Gassner Jr.": "Real Person",
    "Engine": "Object",
	"Transmission": "Object",
	"Brakes": "Object",
	"Alternator": "Object",
	"Battery": "Object",
	"Radiator": "Object",
	"Exhaust": "Object",
	"Suspension": "Object",
	"Shock Absorber": "Object",
	"Steering Wheel": "Object",
	"Tires": "Object",
	"Wheels": "Object",
	"Headlights": "Object",
	"Taillights": "Object",
	"Turn Signal": "Object",
	"Windshield": "Object",
	"Windshield Wipers": "Object",
	"Side Mirrors": "Object",
	"Rearview Mirror": "Object",
	"Bumper": "Object",
	"Fenders": "Object",
	"Grille": "Object",
	"Hood": "Object",
	"Trunk": "Object",
	"Doors": "Object",
	"Seats": "Object",
	"Seatbelts": "Object",
	"Airbags": "Object",
	"Dashboard": "Object",
	"Instrument Cluster": "Object",
	"Speedometer": "Object",
	"Odometer": "Object",
	"Fuel Tank": "Object",
	"Fuel Pump": "Object",
	"Fuel Injector": "Object",
	"Timing Belt": "Object",
	"Camshaft": "Object",
	"Crankshaft": "Object",
	"Pistons": "Object",
	"Cylinder Head": "Object",
	"Oil Filter": "Object",
	"Oil Pan": "Object",
	"Clutch": "Object",
	"Flywheel": "Object",
	"Timing Chain": "Object",
	"Differential": "Object",
	"Axles": "Object",
	"CV Joint": "Object",
	"Wheel Bearings": "Object",
	"Suspension Springs": "Object",
	"Control Arms": "Object",
	"Ball Joints": "Object",
	"Tie Rods": "Object",
	"Struts": "Object",
	"Brake Pads": "Object",
	"Brake Discs": "Object",
	"Brake Calipers": "Object",
    'Turbocharger':'Object',
    'Supercharger':'Object',
    'Oscilloscope':'Object',
    'Function Generator':'Object',
    'Mecanum Wheels':'Object',
    'Arduino':'Object',
    'Raspberry PI':'Object',
    "Hammer": "Object",
	"Screwdriver": "Object",
	"Wrench": "Object",
	"Pliers": "Object",
	"Drill": "Object",
	"Saw": "Object",
	"Chisel": "Object",
	"Tape Measure": "Object",
	"Level": "Object",
	"Utility Knife": "Object",
	"Allen Wrench": "Object",
	"Ratchet": "Object",
	"Socket Set": "Object",
	"Clamps": "Object",
	"Vice": "Object",
	"Pry Bar": "Object",
	"Crowbar": "Object",
	"Files": "Object",
	"Hacksaw": "Object",
	"Jigsaw": "Object",
	"Circular Saw": "Object",
	"Angle Grinder": "Object",
	"Sander": "Object",
	"Multimeter": "Object",
	"Wire Strippers": "Object",
	"Crimping Tool": "Object",
	"Pipe Wrench": "Object",
	"Crescent Wrench": "Object",
	"Spanner": "Object",
	"Bolt Cutter": "Object",
	"Mallet": "Object",
	"Plane": "Object",
	"Trowel": "Object",
	"Shovel": "Object",
	"Hoe": "Object",
	"Pickaxe": "Object",
	"Axe": "Object",
	"Rake": "Object",
	"Taping Knife": "Object",
	"Putty Knife": "Object",
	"Ladder": "Object",
	"Hose": "Object",
	"Wheelbarrow": "Object",
	"Garden Fork": "Object",
	"Spade": "Object",
	"Pruning Shears": "Object",
	"Lawn Mower": "Object",
	"Edger": "Object",
	"String Trimmer": "Object",
	"Post Hole Digger": "Object",
	"Chainsaw": "Object",
	"Shovel": "Object",
	"Screw Gun": "Object",
	"Power Sander": "Object",
	"Heat Gun": "Object",
	"Impact Driver": "Object",
	"Angle Drill": "Object",
	"Orbital Sander": "Object",
	"Tile Cutter": "Object",
	"Staple Gun": "Object",
	"Wire Brush": "Object",
	"Lug Wrench": "Object",
	"Bolt Puller": "Object",
	"Laser Measure": "Object",
	"Stud Finder": "Object",
	"Cordless Drill": "Object",
	"Torque Wrench": "Object",
	"Tap and Die Set": "Object",
	"Caulking Gun": "Object",
	"Clamp": "Object",
	"Stapler": "Object",
	"Pipe Bender": "Object",
	"Hole Saw": "Object",
	"Cutter": "Object",
	"Hose Reel": "Object",
	"Sandpaper": "Object",
	"File": "Object",
	"Woodworking Vise": "Object",
	"Belt Sander": "Object",
	"Screw Extractor": "Object"

              }

dbName = "proj_bf"

dbUser = "abasu"

dbPass = "pass3607"

print('connecting to db')
try:
	conn = mariadb.connect(
		user = dbUser,
		password = dbPass,
		host="cslab.skidmore.edu",
		port=3306,
		database=dbName
	)
except mariadb.Error as e:
	print(f'Error connecting to MariaDB: {e}')
	exit(1)

cur = conn.cursor()

# generate a list of users, assigning each a name and a value for points between 0 and 700
users = []
for i in range(6, 306):
    users.append([f'User{i}', random.randint(0, 700)])


# generate random vals for each characters stats
stats = []
for i in range(len(characters)):
    indiv_stats = []
    for j in range(7):
        indiv_stats.append(random.randint(0, 10))
    stats.append(indiv_stats)


# combine character and stats into a single tuple
i = 0
all_char = []
for char in characters:
    indiv_char = [char]
    for j in range(7):
        indiv_char.append(stats[i][j])
    indiv_char.append(characters[char])
    indiv_char = tuple(indiv_char)
    all_char.append(indiv_char)
    i += 1
    
# insert players into database
cur.executemany("INSERT INTO Player (pname, strength, intelligence, durabil, battle_iq, speed, tech, magic, genre) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", all_char)

conn.commit()


# copy character list
char_assign = all_char.copy()
#loop through users
for i in range(len(users)):
    # assign each user 3 players
	for j in range(3):
        # get a random player
		character = char_assign.pop(random.randint(0, len(char_assign) - 1))
        # add random player to associated user
		users[i].append(character[0])
users = tuple(users)
cur.executemany("INSERT INTO User (uname, points, player1, player2, player3) VALUES (?, ?, ?, ?, ?)", users)
conn.commit()

# generate 100 random matches
curdate = datetime.datetime(2020, 1, 1, 8, 0, 0)
for i in range(5000):
    # select two random users
	user1 = random.randint(0, len(users) - 1)
	user2 = random.randint(0, len(users) - 1)
    # make sure users are different
	while(user2 == user1):
		user2 = random.randint(0, len(users))
        
	#select random player from each user
	player1 = random.randint(2, 4)
	player2 = random.randint(2, 4)

	# create tuple of match to insert
	to_insert = (8 + i, users[user1][player1], users[user2][player2], f'{curdate}')

	cur.execute("INSERT INTO Matches (match_id, challenger, opponent, time_stamp) VALUES (?, ?, ?, ?)", to_insert)
	conn.commit()
	
	#update date
	newhour = curdate.hour + 1
	newday = curdate.day
	newmonth = curdate.month
	newyear = curdate.year
	if(curdate.hour == 20):
		newhour = 8
		newday = curdate.day + 1
		if(curdate.day == 28):
			newday = 1
			newmonth = curdate.month + 1
			if(curdate.month == 12):
				newmonth = 1
				newyear = curdate.year + 1

	curdate = datetime.datetime(newyear, newmonth, newday, newhour)


# select 6 more matches to add to a tournament round of 16
i = 3
challengers = []
opponents = []
while(True):
	# select a random match to make a tournament match
	rand_match = random.randint(8, 107)
	cur.execute('SELECT challenger, opponent, match_id FROM Matches WHERE match_id = (?)', (rand_match,))
	# check if selected players are already in the tournament
	temp = list(tuple((cur))[0])
	p1 = temp[0]
	p2 = temp[1]
	match = temp[2]

	if p1 not in challengers and p1 not in opponents and p2 not in challengers and p2 not in opponents:
		challengers.append(p1)
		opponents.append(p2)
		cur.execute("INSERT INTO Tournament (tournament_match_id, round_num, match_id) VALUES (?, ?, ?)", (i, 1, match))
		i += 1
		if i == 9:
			break

conn.commit()

print("Random data insertion succesful")

conn.close()