import pygame
import pygame.locals as pl
import sys


class Wordbanks:
    vocab1stGrade = ('add', 'after', 'again', 'any', 'apart', 'apple', 'arm', 'baby', 'bake', 'bang', 'banana', 'bark', 'beat', 'been', 'being', 'belt', 'bent', 'best', 'bill', 'bike', 'bird', 'birth', 'bone', 'born', 'black', 'blew', 'block', 'father', 'fell', 'few', 'field', 'fill', 'fine', 'first', 'flag', 'flat', 'flew', 'flower', 'fog', 'fool', 'foot', 'fort', 'free', 'fresh', 'from', 'game', 'gang', 'gave', 'gift', 'girl', 'give', 'glad', 'going', 'golf', 'more', 'morning', 'mother', 'much', 'mule', 'must', 'nail', 'name', 'neat', 'neck', 'nest', 'never', 'next', 'new', 'nine', 'noon', 'nose', 'note', 'now', 'odd', 'old', 'once', 'open', 'orange', 'other', 'over', 'snow', 'snug', 'six', 'soda', 'sofa', 'sold', 'some', 'soon', 'spit', 'star', 'start', 'stay', 'step', 'stew', 'still', 'stir', 'stone', 'stool', 'stop', 'stove', 'straw', 'string', 'such', 'summer', 'sun', 'swing', 'table', 'blue', 'book', 'brag', 'bring', 'brook', 'brother', 'brown', 'bush', 'came', 'cane', 'card', 'cart', 'case', 'chain', 'chair', 'chalk', 'chat', 'chin', 'chop', 'clam', 'clan', 'clap', 'class', 'claw', 'clay', 'clean', 'clover', 'cloud', 'crayon', 'club', 'gone', 'grape', 'grass', 'gray', 'green', 'grew', 'grit', 'gull', 'had', 'hand', 'hang', 'happy', 'hard', 'harm', 'has', 'have', 'heat', 'heavy', 'help', 'here', 'hide', 'hill', 'hint', 'home', 'hope', 'horn', 'how', 'hush', 'ill', 'inside', 'pain', 'pants', 'part', 'pave', 'pear', 'pen', 'pencil', 'pets', 'pick', 'pink', 'plan', 'plant', 'play', 'poor', 'pretty', 'print', 'punch', 'purple', 'put', 'rain', 'rang', 'rank', 'read', 'ride', 'river', 'road', 'rock', 'rode', 'room', 'rope', 'tail', 'take', 'tale', 'tank', 'team', 'tell', 'ten', 'tent', 'test', 'thank', 'their', 'them', 'then', 'these', 'they', 'thick', 'thing', 'think', 'third', 'this', 'time', 'today', 'took', 'train', 'trip', 'truck', 'trust', 'try', 'twelve', 'thank', 'coat', 'come', 'cook', 'cool', 'corn', 'could', 'cram', 'crew', 'crib', 'crow', 'crowd', 'crown', 'cube', 'dark', 'deal', 'desk', 'dew', 'dime', 'dine', 'dirt', 'doll', 'door', 'draw', 'dress', 'drink', 'drop', 'dull', 'each', 'east', 'easy', 'into', 'jaw', 'joke', 'juice', 'jump', 'just', 'keep', 'king', 'kite', 'know', 'last', 'lake', 'late', 'like', 'lime', 'line', 'live', 'look', 'love', 'luck', 'made', 'maid', 'make', 'many', 'map', 'mask', 'may', 'meal', 'meat', 'meet', 'round', 'rub', 'rubber', 'sail', 'sale', 'same', 'sank', 'save', 'see', 'seed', 'seen', 'seep', 'sell', 'send', 'seven', 'shall', 'shape', 'sink', 'shake', 'shirt', 'ship', 'shoes', 'shop', 'show', 'shut', 'sick', 'side', 'size', 'sled', 'sleep', 'them', 'then', 'there', 'think', 'those', 'tree', 'under', 'upon', 'use', 'used', 'very', 'vest', 'vote', 'wait', 'walk', 'want', 'was', 'water', 'well', 'were', 'west', 'when', 'which', 'white', 'who', 'will', 'wing', 'winter', 'with', 'woman', 'eight', 'eleven', 'end', 'every', 'fang', 'farther', 'fast', 'men', 'mice', 'milk', 'mine', 'mint', 'mix', 'moon', 'slip', 'slow', 'sister', 'smell', 'snail', 'snap', 'snore', 'women', 'yell', 'zero', 'zone')
    vocab2ndGrade = ('across', 'after', 'ago', 'alarm', 'always', 'angry', 'animal', 'around', 'aunt', 'away', 'bait', 'ball', 'balloon', 'band', 'bang', 'barn', 'bath', 'bead', 'beam', 'bean', 'because', 'bedroom', 'been', 'before', 'believe', 'bend', 'dream', 'dress', 'drip', 'drive', 'drop', 'drove', 'drum', 'duck', 'dump', 'dust', 'dye', 'every', 'everyone', 'everywhere', 'eye', 'family', 'fast', 'father', 'fed', 'feed', 'fight', 'finch', 'first', 'fish', 'five', 'flake', 'flap', 'mother', 'myself', 'night', 'nobody', 'notes', 'notebook', 'number', 'our', 'out', 'outside', 'owl', 'pack', 'pail', 'pain', 'parent', 'park', 'path', 'pen', 'person', 'piece', 'pine', 'planet', 'plate', 'plot', 'plum', 'plus', 'pond', 'soon', 'sound', 'south', 'space', 'spark', 'space', 'speak', 'speech', 'speed', 'spin', 'spoke', 'spoon', 'spot', 'spy', 'stack', 'stain', 'stamp', 'state', 'steep', 'stick', 'stone', 'stood', 'store', 'straw', 'stuck', 'summer', 'swine', 'best', 'better', 'between', 'blast', 'blaze', 'blend', 'blimp', 'blink', 'blow', 'boat', 'boot', 'both', 'brag', 'brand', 'bread', 'brick', 'bride', 'bright', 'bring', 'broom', 'brother', 'bunch', 'busy', 'buy', 'call', 'camp', 'cannot', 'carry', 'cash', 'caught', 'flash', 'flaw', 'fleet', 'flesh', 'flight', 'flop', 'flung', 'food', 'found', 'friend', 'frog', 'front', 'glass', 'globe', 'gloss', 'goat', 'goes', 'goose', 'grade', 'grand', 'grandfather', 'grandmother', 'grape', 'grass', 'green', 'grin', 'grind', 'grow', 'happy', 'heard', 'pool', 'prime', 'prow', 'pull', 'push', 'rabbit', 'raise', 'rake', 'reach', 'read', 'rest', 'rich', 'right', 'robin', 'rock', 'row', 'rude', 'rust', 'sack', 'said', 'sail', 'sailboat', 'sand', 'said', 'says', 'scale', 'screw', 'sea', 'seal', 'seam', 'teach', 'tell', 'their', 'these', 'those', 'thrift', 'throb', 'tiger', 'tight', 'tip', 'toad', 'toast', 'tooth', 'town', 'trade', 'trail', 'tramp', 'tray', 'treat', 'tribe', 'trick', 'trim', 'trip', 'truth', 'ton', 'tow', 'tug', 'tune', 'twelve', 'twist', 'center', 'charge', 'chess', 'chest', 'chicken', 'child', 'children', 'choke', 'chore', 'clapped', 'clash', 'clean', 'clear', 'click', 'clock', 'cold', 'cookie', 'could', 'count', 'crank', 'crawl', 'crook', 'cross', 'crow', 'dash', 'dear', 'deep', 'deer', 'desk', 'die', 'hook', 'horse', 'house', 'hush', 'jail', 'jam', 'jump', 'kick', 'kind', 'kiss', 'kitten', 'lean', 'leave', 'light', 'limp', 'lion', 'list', 'live', 'loaf', 'lock', 'long', 'lost', 'loud', 'lump', 'lunch', 'lunchroom', 'made', 'many', 'maybe', 'meal', 'second', 'seem', 'send', 'sent', 'silly', 'seen', 'shame', 'shape', 'share', 'shark', 'sharp', 'sheep', 'shock', 'shook', 'shore', 'short', 'shut', 'sight', 'silly', 'sing', 'sister', 'slam', 'slant', 'sleek', 'sleep', 'sleet', 'slice', 'slick', 'slid', 'slide', 'uncle', 'under', 'upon', 'use', 'vase', 'very', 'wait', 'warm', 'winter', 'was', 'wash', 'water', 'weak', 'week', 'went', 'were', 'whale', 'what', 'wheel', 'where', 'which', 'while', 'who', 'why', 'wide', 'wind', 'wish', 'wool', 'work', 'would', 'dirt', 'dish', 'dock', 'doctor', 'does', "don't", 'downtown', 'mean', 'mess', 'met', 'might', 'minus', 'mitt', 'mitten', 'slip', 'slot', 'smart', 'snack', 'sneer', 'soap', 'song', 'yard', 'yellow', 'yesterday', 'yet', 'your', 'zebra')
    vocab3rdGrade = ('about', 'actor', 'agree', 'airplane', 'airport', 'alike', 'almost', 'alone', 'along', 'aloud', 'already', 'army', 'ate', 'awake', 'awhile', 'bare', 'baseball', 'beat', 'become', 'bedtime', 'beef', 'beet', 'began', 'begin', 'bench', 'bent', 'berry', 'dinner', "doesn't", 'done', "don't", 'dozen', 'draw', 'drink', 'dwell', 'early', 'earn', 'eggnog', 'eight', 'elbow', 'elsewhere', 'employ', 'enjoy', 'face', 'fall', 'far', 'fault', 'fill', 'fired', 'fireman', 'fit', 'flavor', 'flow', 'fray', 'kidnap', 'kind', 'ladybug', 'large', 'later', 'laugh', 'light', 'long', 'loss', 'lung', 'mailbox', 'mare', 'mark', 'milking', 'mopped', 'mouse', 'mouth', 'move', 'much', 'munch', 'myself', 'noontime', 'never', 'none', 'number', 'oatmeal', 'only', 'small', 'soft', 'someone', 'somewhere', 'sought', 'sow', 'spelling', 'spend', 'spent', 'squirt', 'start', 'stepped', 'stopped', 'strain', 'stray', 'stream', 'street', 'strike', 'studies', 'study', 'sugar', 'sunny', 'sure', 'surely', 'sweet', 'talk', 'taught', 'better', 'birthday', 'bless', 'boil', 'bought', 'boy', 'brand', 'brass', 'bring', 'bringing', 'brush', 'build', 'built', 'burn', 'bury', 'bushes', 'bushy', 'butter', 'cannot', "can't", 'carry', 'cast', 'cave', 'cent', 'cherries', 'cherry', 'chess', 'chest', 'chili', 'choose', 'frost', 'full', 'fulfill', 'gate', 'gift', 'glove', 'glue', 'goldfish', 'goose', 'got', 'grabbed', 'grain', 'greet', 'grow', 'guild', 'guilt', 'hair', 'haircut', 'half', 'halfway', 'hang', 'hare', 'hobbies', 'hobby', 'hold', 'holiday', 'hot', 'huge', 'hunt', 'hurry', 'own', 'pail', 'pale', 'pancake', 'past', 'pear', 'pest', 'pick', 'pinch', 'pint', 'pitch', 'please', 'point', 'popcorn', 'pound', 'pray', 'pretty', 'price', 'prize', 'pure', 'pushes', 'queen', 'queer', 'quick', 'quicksand', 'quiet', 'quilt', 'quit', 'rainstorm', 'rent', 'tear', 'tearful', 'ten', 'thirst', 'throne', 'throw', 'thrown', 'tipped', 'today', 'together', 'toothpaste', 'toy', 'try', 'turn', 'twig', 'underdog', 'visiting', 'voice', 'volleyball', 'walk', 'warm', 'whatever', 'when', 'whose', 'wire', "won'", 'wood', 'word', 'worm', 'worth', 'churn', 'clean', 'cobweb', 'coil', 'could', 'cracker', 'crazy', 'cure', 'curl', 'cut', 'daytime', 'hurt', "isn't", 'its', "it's", 'itself', 'jellyfish', 'join', 'jolly', 'joy', 'keep', 'role', 'round', 'scarecrow', 'scarf', 'search', 'seven', 'shall', 'should', 'show', 'six', 'slight', 'work', 'worker', 'worry', 'wrench', 'write', 'wrong', 'yourself', 'young', 'zipped')
    vocab4thGrade = ('above', 'account', 'across', 'addition', 'advice', 'against', 'ahead', 'alert', 'among', 'amount', 'anger', 'angry', 'annoy', 'annual', 'another', 'answer', 'apiece', 'apple', 'argue', 'arguing', 'arithmetic', 'arose', 'author', 'avenue', 'avoid', 'award', 'aware', 'crowd', 'crush', 'dainty', 'daily', 'daughter', 'deaf', 'death', 'decorator', 'destroy', 'device', 'direction', 'doctor', 'dollar', 'donkey', 'double', 'drank', 'drug', 'earthquake', 'enough', 'equal', 'evening', 'everybody', 'everyone', 'everything', 'excuse', 'exercise', 'explode', 'ivory', 'jeans', 'journal', 'judge', 'juggle', 'juice', 'kept', 'kitchen', 'lace', 'lack', 'laid', 'lame', 'lamp', 'laugh', 'least', 'lecture', 'ledge', 'lettuce', 'little', 'local', 'loyal', 'manage', 'marble', 'market', 'match', 'measles', 'mention', 'shallow', 'shave', 'shear', 'sheet', 'shrimp', 'sidewalk', 'sideways', 'simple', 'skate', 'skill', 'slain', 'slate', 'slave', 'sleet', 'sleeve', 'slept', 'smoke', 'sorry', 'stage', 'station', 'statue', 'steam', 'stockings', 'stole', 'strange', 'stretch', 'strong', 'badge', 'basic', 'basket', 'basketball', 'battle', 'beast', 'beetle', 'beggar', 'blame', 'blank', 'board', 'boast', 'borrow', 'bottle', 'brain', 'branch', 'brave', 'breath', 'bridge', 'bubble', 'bucket', 'burst', 'cactus', 'calm', 'canal', 'cannon', 'careless', 'cattle', 'caution', 'celery', 'fearless', 'feast', 'fifth', 'finger', 'flock', 'flour', 'flower', 'flute', 'foggy', 'follow', 'forget', 'forth', 'fraction', 'frame', 'freeze', 'freight', 'fried', 'frown', 'froze', 'funeral', 'furniture', 'gallery', 'garbage', 'gather', 'geese', 'general', 'genius', 'gentle', 'ghost', 'giraffe', 'middle', 'midnight', 'monkey', 'month', 'narrate', 'narrow', 'nation', 'naughty', 'newspaper', 'nineteen', 'noise', 'noisy', 'north', 'notion', 'ocean', 'offer', 'often', 'order', 'palm', 'patch', 'pebble', 'people', 'pillow', 'plane', 'playground', 'plight', 'poise', 'poison', 'porch', 'portion', 'stump', 'stung', 'sweat', 'swim', 'target', 'tenth', 'terrible', 'themselves', 'thirsty', 'thrill', 'throat', 'throne', 'ticket', 'time', 'timing', 'title', 'toils', 'tomorrow', 'toothbrush', 'torch', 'tough', 'trace', 'tried', 'trouble', 'turkey', 'turtle', 'twist', 'unable', 'understand', 'understood', 'cellar', 'center', 'central', 'century', 'charge', 'chase', 'chimney', 'chose', 'chute', 'circus', 'close', 'cloth', 'clothing', 'coach', 'coast', 'collar', 'come', 'coming', 'continue', 'cough', 'couple', 'court', 'cousin', 'crane', 'crash', 'crate', 'crawl', 'craze', 'cream', 'creation', 'glacier', 'glory', 'governor', 'gravy', 'grill', 'grind', 'grove', 'growl', 'guess', 'happen', 'hatch', 'height', 'helpless', 'hoist', 'hollow', 'honey', 'hope', 'hoping', 'hopeless', 'hydrant', 'icicle', 'ignore', 'image', 'inches', 'include', 'income', 'insist', 'invent', 'invite', 'island', 'position', 'praise', 'race', 'ranch', 'range', 'ready', 'recover', 'regular', 'remain', 'remark', 'remember', 'remind', 'remove', 'repair', 'report', 'return', 'riddle', 'rifle', 'roast', 'rough', 'royal', 'scale', 'scarce', 'scowl', 'scrap', 'scrape', 'scratch', 'scream', 'seashore', 'season', 'underwear', 'unhappy', 'unfair', 'unkind', 'unknown', 'unlikely', 'unload', 'unlock', 'unlucky', 'untie', 'until', 'unusual', 'unwilling', 'use', 'using', 'usual', 'vacation', 'value', 'vegetable', 'visitor', 'vocal', 'voyage', 'wander', 'weave', 'whenever', 'which', 'whole', 'width', 'wonder', 'year', 'cried ', 'issue ', 'serve')
    vocab5thGrade = ('able', 'achieve', 'acoustics', 'action', 'activity', 'advertisement', 'aftermath', 'afternoon', 'afterthought', 'anoint', 'apartment', 'apparel', 'appear', 'appliance', 'appoint', 'approve', 'attack', 'attend', 'awkward', 'baker', 'banker', 'beginner', 'believe', 'bomb', 'border', 'boundary', 'breakfast', 'delight', 'detrimental', 'devotion', 'dirty', 'disappear', 'discover', 'disguise', 'dishonest', 'distance', 'disuse', 'dominant', 'eager', 'education', 'eighth', 'empty', 'encourage', 'entertain', 'equal', 'exactly', 'excel', 'exert', 'exhale', 'exist', 'extravagant', 'facility', 'famous', 'faucet', 'lawyer', 'leather', 'level', 'linen', 'locket', 'lumber', 'magic', 'manageable', 'management', 'mayor', 'meanwhile', 'medallion', 'medicinal', 'melon', 'memorable', 'mention', 'metal', 'meter', 'mightily', 'minister', 'mitten', 'money', 'motor', 'mountain', 'music', 'nature', 'neither', 'reduce', 'reduction', 'reign', 'reply', 'retrieve', 'reward', 'route', 'sable', 'scene', 'scent', 'section', 'shoulder', 'significance', 'similar', 'simplicity', 'sleight', 'socket', 'soup', 'speedy', 'square', 'squirrel', 'staff', 'stolen', 'stranger', 'stroll', 'subject', 'suit', 'breathe', 'brightly', 'burglar', 'cabbage', 'cable', 'calculator', 'calendar', 'capital', 'caption', 'carpenter', 'ceiling', 'cemetery', 'channel', 'circle', 'climb', 'clothe', 'colony', 'comfort', 'comical', 'coming', 'competition', 'concern', 'condition', 'confirm', 'conscious', 'constant', 'construct', 'creator', 'creature', 'crouton', 'feather', 'feature', 'fertile', 'fiction', 'forever', 'fragile', 'friction', 'frugal', 'fruit', 'fuel', 'galley', 'grateful', 'group', 'guard', 'guardian', 'guest', 'guide', 'guitar', 'handle', 'health', 'heart', 'heavily', 'helmet', 'holy', 'hoping', 'household', 'idea', 'increase', 'industry', 'invention', 'nickel', 'option', 'overrule', 'pardon', 'partner', 'passenger', 'perfect', 'perhaps', 'personal', 'pickle', 'picture', 'plantation', 'plastic', 'pleasure', 'pocket', 'police', 'pollution', 'popular', 'precious', 'preferred', 'prejudice', 'prepay', 'preschool', 'proceed', 'produce', 'professor', 'pronounce', 'propel', 'property', 'protect', 'supply', 'supporter', 'sweater', 'teachable', 'televise', 'temper', 'territory', 'texture', 'theater', 'though', 'thread', 'tidal', 'total', 'toward', 'treachery', 'treatment', 'triple', 'useful', 'vacant', 'vain', 'valiant', 'veil', 'vein', 'victory', 'virtue', 'visual', 'volcano', 'wealth', 'weather', 'weird', 'currency', 'curtain', 'customer', 'cycle', 'damage', 'decay', 'decide', 'define', 'jealous', 'junction', 'junior', 'kindness', 'kitten', 'laborer', 'lamb', 'language', 'provide', 'quartet', 'railway', 'reason', 'receive', 'recess', 'recitation', 'record', 'wilderness', 'windy', 'wren', 'wring', 'wrist', 'writer')
    vocab6thGrade = ('abolish', 'absence', 'accident', 'adequate', 'admissible', 'adopt', 'advantage', 'adventure', 'adverb', 'advisor', 'ailment', 'alchemy', 'algebra', 'aluminum', 'ancient', 'appreciate', 'approval', 'arise', 'ascend', 'associate', 'athlete', 'attorney', 'audible', 'autumn', 'awful', 'bachelor', 'banjo', 'crept', 'crutch', 'crystal', 'crystallize', 'daylight', 'debris', 'decade', 'defeat', 'defender', 'delicate', 'delivery', 'deny', 'deposit', 'descent', 'desecration', 'desert', 'desire', 'dessert', 'destination', 'detach', 'detail', 'directory', 'disapprove', 'discuss', 'dismiss', 'display', 'division', 'imbalance', 'imitate', 'immigrant', 'immovable', 'immune', 'impatient', 'import', 'impossible', 'impress', 'infinite', 'innocent', 'inquire', 'instead', 'introduce', 'irresistible', 'janitor', 'jeopardy', 'judgment', 'knack', 'knead', 'knives', 'lacquer', 'larynx', 'limestone', 'manila', 'manufacturer', 'medicine', 'punish', 'pursue', 'quartet', 'quiver', 'raccoon', 'release', 'rely', 'requirement', 'research', 'resist', 'resource', 'salmon', 'saucer', 'saucy', 'sculptor', 'senator', 'sentence', 'serious', 'service', 'silhouette', 'skillet', 'sleuth', 'solo', 'solve', 'somersault', 'soprano', 'source', 'barbecue', 'baritone', 'basin', 'bauble', 'belittle', 'blanket', 'blonde', 'blouse', 'bonnet', 'button', 'buyer', 'cabinet', 'cafeteria', 'calligraphy', 'camouflage', 'carburetor', 'cement', 'centigram', 'character', 'civilian', 'clinch', 'coarse', 'coffee', 'colander', 'cologne', 'common', 'conscience', 'contemporary', 'contrary', 'copier', 'dormitory', 'duet', 'earnest', 'echo', 'edible', 'efficient', 'election', 'enormous', 'enterprise', 'escapade', 'establish', 'except', 'exchange', 'exhibit', 'expert', 'extra', 'factual', 'fasten', 'feasible', 'financial', 'flourish', 'foolish', 'fortress', 'fundamental', 'furious', 'ghetto', 'giant', 'government', 'halo', 'honorary', 'mercury', 'monotonous', 'naive', 'narrative', 'necessary', 'notify', 'obedience', 'oblige', 'operation', 'orchid', 'outfit', 'owner', 'packet', 'paradoxical', 'pastime', 'pavilion', 'perforated', 'periodical', 'perish', 'petition', 'poem', 'political', 'positive', 'possible', 'poultry', 'predict', 'prefer', 'preference', 'private', 'profit', 'steady', 'subdue', 'submarine', 'surgery', 'survey', 'swift', 'switch', 'taunt', 'technical', 'testimonial', 'their', 'there', "they're", 'touch', 'trousers', 'tuxedo', 'unaware', 'unnecessary', 'vary', 'vehicle', 'venom', 'verbal', 'verify', 'violence', 'voluntary', 'weevil', 'wholesale', 'wit', 'women', 'zero', 'covet', 'creditor', 'illustration', 'imaginary', 'prominent', 'promise')
    vocab7thGrade = ('abrupt', 'accede', 'accelerate', 'accidentally', 'accompanied', 'accost', 'accumulate', 'accuse', 'acquittal', 'adjourn', 'afterward', 'amphibian', 'anachronism', 'analysis', 'ancestry', 'angle', 'ankle', 'anywhere', 'arrival', 'artificial', 'aspect', 'attire', 'attractive', 'aversion', 'ballot', 'banana', 'banquet', 'elicit', 'eliminate', 'elliptical', 'embarrass', 'eminent', 'employee', 'emulate', 'enable', 'encode', 'encyclopedia', 'engineer', 'enslave', 'equipping', 'evanescent', 'evidently', 'exclude', 'exhale', 'eon', 'expediency', 'expedite', 'expenditure', 'extension', 'extract', 'extraordinary', 'exude', 'familiar', 'fastidious', 'jurist', 'kangaroo', 'kerosene', 'khaki', 'kindergarten', 'knowledge', 'labeling', 'laboratory', 'laborious', 'library', 'literature', 'logical', 'lovely', 'lying', 'lyric', 'maintenance', 'mammal', 'maneuver', 'manuscript', 'massive', 'materialism', 'menthol', 'mercurial', 'metallic', 'microbe', 'microcosm', 'mileage', 'prairie', 'predecessor', 'presage', 'pretzel', 'prostrate', 'protocol', 'puddle', 'putter', 'quandary', 'quantity', 'rabid', 'ransack', 'rapport', 'raucous', 'receipt', 'recline', 'recluse', 'recognize', 'recreation', 'recurring', 'rodeo', 'rotund', 'safety', 'salvation', 'saturate', 'savor', 'scholastic', 'battery', 'belie', 'belief', 'bondage', 'boycott', 'brochure', 'budgeting', 'buffalo', 'calendar', 'campaign', 'capitalization', 'cartage', 'cashier', 'ceiling', 'celebration', 'chair', 'chauffeur', 'cheddar', 'civil', 'civilize', 'civilization', 'classification', 'clientele', 'commitment', 'community', 'conceive', 'counterfeit', 'critic', 'criticize', 'cuddle', 'fiend', 'flamboyant', 'flexible', 'foreign', 'forfeit', 'foundation', 'fulfill', 'futurity', 'gaseous', 'gauge', 'genuine', 'graduate', 'grocery', 'grovel', 'guild', 'handkerchief', 'hearty', 'heavily', 'height', 'hosiery', 'hygiene', 'illegal', 'illiterate', 'imbecile', 'imitation', 'inaugural', 'incautious', 'index', 'induce', 'indulge', 'miniature', 'ministry', 'misfortune', 'mispronounce', 'mistreat', 'misunderstood', 'mobilize', 'monologue', 'moreover', 'mosquito', 'murmur', 'myth', 'necessarily', 'nickel', 'niece', 'nineteenth', 'ninety', 'ninth', 'nondescript', 'nonfiction', 'nucleus', 'obey', 'obligate', 'obnoxious', 'obscure', 'obstacle', 'occasion', 'occasionally', 'occur', 'odor', 'scissors', 'scrabble', 'secretarial', 'security', 'serviceable', 'shriek', 'shuffle', 'shutter', 'siege', 'skeptical', 'stereo', 'sticky', 'strenuous', 'strident', 'submission', 'surfeit', 'surmount', 'syllable', 'syrup', 'system', 'tailor', 'tangible', 'tariff', 'tendency', 'therefore', 'thoroughbred', 'throughout', 'tornado', 'triangle', 'turmoil', 'culprit', 'cylinder', 'deceive', 'dehydration', 'delegate', 'delinquent', 'demean', 'despoil', 'develop', 'development', 'diagnosis', 'didactic', 'difficulty', 'disposal', 'disposition', 'droll', 'duplicate', 'durable', 'infection', 'inferior', 'inflate', 'informal', 'injury', 'inscription', 'insecure', 'insinuate', 'institution', 'instrument', 'intelligible', 'interior', 'invalid', 'involved', 'irrefutable', 'jeopardize', 'jewelry', 'journey', 'offense', 'oneself', 'opossum', 'opponent', 'optimism', 'organization', 'organize', 'pageant', 'pamphlet', 'parse', 'particular', 'persist', 'persuade', 'perspire', 'pleat', 'plethora', 'policeman', 'potato', 'unique', 'usurp', 'vacuum', 'vagrant', 'varnish', 'vinegar', 'visible', 'visitor', 'void', 'waiver', 'warranty', 'weather', 'wholly', 'willful', 'yacht', 'yield', 'zenith', 'zoology')
    vocab8thGrade = ('abbreviate', 'absorbent', 'accept', 'access', 'accessible', 'accessory', 'acoustics', 'accumulate', 'acknowledgment', 'adjust', 'aerial', 'affects', 'alien', 'allotment', 'allotted', 'already', 'altercation', 'amass', 'amendment', 'amorous', 'ancestor', 'anecdote', 'angular', 'anonymous', 'antidote', 'antique', 'antiseptic', 'contiguous', 'corporal', 'council', 'counsel', 'country', 'creator', 'critique', 'customary', 'customer', 'daybreak', 'deceive', 'defendant', 'deficient', 'deficit', 'depreciation', 'desirable', 'desolate', 'detain', 'devour', 'diagnosis', 'diffidence', 'diminish', 'disappeared', 'disapproval', 'disbursement', 'discernible', 'discrepancy', 'gnawing', 'gorgeous', 'grotesque', 'gymnasium', 'handicapped', 'handling', 'handsome', 'haphazard', 'harness', 'hazardous', 'headquarters', 'homogenize', 'horrific', 'humidor', 'idiosyncrasy', 'impatience', 'impinge', 'incandescent', 'inconsolable', 'indelible', 'inept', 'influence', 'innocence', 'innumerable', 'insistent', 'insoluble', 'integrity', 'officious', 'opposite', 'optimism', 'oregano', 'overrate', 'pageant', 'parliament', 'passable', 'paucity', 'penalty', 'perseverance', 'personality', 'picnicking', 'plaintiff', 'poignancy', 'poignant', 'potential', 'preceding', 'precipice', 'preoccupy', 'prospectus', 'quest', 'questionnaire', 'quixotic', 'radioactive', 'rapacious', 'rayon', 'architect', 'arrangement', 'asphalt', 'assignment', 'asterisk', 'attorneys', 'audible', 'aviator', 'bachelor', 'bankruptcy', 'barbaric', 'bask', 'battery', 'behavior', 'benefited', 'berserk', 'besieged', 'bicycle', 'blanch', 'brilliance', 'budget', 'bulletin', 'business', 'cachet', 'callus', 'cancellation', 'canvas', 'canvass', 'capricious', 'carburetor', 'disinterested', 'disoblige', 'dissociate', 'distress', 'diurnal', 'divine', 'domestic', 'domesticate', 'dominance', 'easier', 'ecstasy', 'effect', 'eject', 'eligible', 'eliminate', 'encouragement', 'encyclopedia', 'epic', 'equilibrium', 'erroneous', 'especially', 'exceptional', 'excessive', 'existence', 'exotic', 'expression', 'extremity', 'extricate', 'facsimile', 'familiar', 'intensify', 'interrogative', 'invariable', 'irksome', 'irresistible', 'irrevocable', 'issuing', 'itemized', 'jewelry', 'judicious', 'juror', 'justifiable', 'landslide', 'legitimate', 'leisure', 'liaison', 'library', 'license', 'lieutenant', 'loophole', 'lunar', 'luncheon', 'magnify', 'malefactor', 'malicious', 'markup', 'mattress', 'mesmerize', 'meteor', 'metric', 'raze', 'recently', 'reconcile', 'relevant', 'relief', 'repulse', 'revive', 'rhyme', 'rhythm', 'roommate', 'roster', 'sanctuary', 'sandwich', 'scarcely', 'schedule', 'schism', 'scholar', 'schooner', 'sedition', 'semester', 'seminary', 'session', 'shrine', 'sieve', 'signal', 'sincerely', 'soccer', 'solitary', 'subvert', 'statutory', 'cashier', 'catastrophe', 'centripetal', 'characteristic', 'chaste', 'cinnamon', 'classic', 'collateral', 'colleague', 'college', 'comedy', 'commerce', 'commercial', 'committee', 'communicate', 'commuter', 'compel', 'compensation', 'competent', 'consider', 'fantastic', 'faulty', 'federal', 'feud', 'flexible', 'flout', 'fluorescent', 'folklore', 'forcible', 'fortunately', 'franchise', 'frivolous', 'frostbitten', 'further', 'galaxy', 'galling', 'genuine', 'gesture', 'geology', 'gigantic', 'mischievous', 'misgiving', 'modern', 'modicum', 'mystery', 'negligence', 'neon', 'neutral', 'newsstand', 'nineteenth', 'nonentity', 'noticeable', 'notoriety', 'nuisance', 'numerator', 'nylon', 'obesity', 'oblique', 'obstinate', 'obsolete', 'terrific', 'thieves', 'tragedy', 'transient', 'transmutation', 'turpitude', 'tyranny', 'unacceptable', 'unique', 'unmoved', 'usher', 'utopia', 'vengeance', 'vocal', 'voucher', 'withhold', 'wrestle', 'written')


#####################
#   Game Specifics  #
#####################
def quit_game():
    pygame.quit()
    sys.exit(0)

def play_music(game, music):
    music = pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    game.music_playing = True
    return

def update_seconds(game, delay):
    game.frame_tracker += 1
    if (game.frame_tracker == (game.max_FPS * delay)):
        game.frame_tracker = 0
        game.seconds += 1
        return True
    return False

def blink_text(game, screen, text, start_screen):
    if (game.update_seconds(game.text_blink_delay)):
        if (game.blinking):
            game.blinking = False
        else:
            game.blinking = True
    if (game.blinking):
        game.draw_blink_text(screen, text, start_screen)
    return

def update_player_input(game, events):
    if (game.words_moving):
        if (game.player_input_obj.update(events, game)):
            game.player_input = game.player_input_obj.get_text()
            game.player_input_obj.reset_input_text()
    return


#####################
#       Frames      #
#####################
def check_frame_count(game):
    if (game.frame_count >= game.max_FPS):
        game.frame_count = 0
        game.seconds += 1
        game.add_word_seconds += 1
    return

def check_quick_frame_count(game):
    max_FPS_fraction = game.max_FPS * game.add_word_delay
    if (game.quick_frame_count == max_FPS_fraction):
        game.quick_frame_count = 0
        return True
    game.quick_frame_count += 1
    return False


#####################
#    Title Events   #
#####################
def check_title_events(game):
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    quit_game()
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_RETURN):
                return True
    return False


#####################
#    Menu Events    #
#####################
def get_avg_word_length(wordbank):
    num_words = len(wordbank)
    total = 0
    for word in wordbank:
        total += len(word)
    avg_length = total / num_words
    return avg_length

def check_menu_mouse_position(game, mouse_position, button):
    if (button.is_over(mouse_position)):
        button.color = game.button_hover_color
        button.textColor = game.button_text_color
        button.hovering = True
        if (button.play_sound):
            game.button_hover_sound.play()
            button.play_sound = False
    else:
        button.color = game.button_color
        button.textColor = game.button_text_color
        button.hovering = False
        button.play_sound = True
    return

def check_button(game, button):
    if (button.text == "1st"):
        game.wordbank = Wordbanks.vocab1stGrade
    elif (button.text == "2nd"):
        game.wordbank = Wordbanks.vocab2ndGrade
    elif (button.text == "3rd"):
        game.wordbank = Wordbanks.vocab3rdGrade
    elif (button.text == "4th"):
        game.wordbank = Wordbanks.vocab4thGrade
    elif (button.text == "5th"):
        game.wordbank = Wordbanks.vocab5thGrade
    elif (button.text == "6th"):
        game.wordbank = Wordbanks.vocab6thGrade
    elif (button.text == "7th"):
        game.wordbank = Wordbanks.vocab7thGrade
    elif (button.text == "8th"):
        game.wordbank = Wordbanks.vocab8thGrade
    if (game.wordbank != None):
        avg_word_length = get_avg_word_length(game.wordbank)
        game.avg_word_length = avg_word_length
        return True
    return False

def check_menu_events(game, buttons):
    mouse_position = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
                    quit_game()
        elif (event.type == pygame.MOUSEMOTION):
            for button in buttons:
                check_menu_mouse_position(game, mouse_position, button)
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            for button in buttons:
                if (button.is_over(mouse_position)):
                    if (check_button(game, button)):
                        return True
    return False


#####################
#  Gameplay Events  #
#####################
def check_game_mouse_position(mouse_position, buttons, game):
    for button in buttons:
        if (button.visible):
            if (button.is_over(mouse_position)):
                button.hovering = True
                if (button.play_sound):
                    game.button_hover_sound.play()
                    button.play_sound = False
            else:
                button.hovering = False
                button.play_sound = True
    return

def click_button(mouse_position, buttons, game):
    for button in buttons:
        if (button.is_over(mouse_position)):
            if (button.text == "Start"):
                game.words_moving = True
                button.visible = True
            elif (button.text == "Pause"):
                if (game.words_moving):
                    game.words_moving = False
                else:
                    game.words_moving = True
            elif (button.text == "Mute"):
                if (game.music_playing):
                    pygame.mixer.music.pause()
                    game.music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    game.music_playing = True
            elif (button.text == "+"):
                game.set_game_speed_up()
            elif (button.text == "-"):
                game.set_game_speed_down()
    return

def check_game_events(game, buttons):
    mouse_position = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT):
            quit_game()
        elif (event.type == pygame.KEYDOWN):
            if event.key == pl.K_ESCAPE:
                if (game.words_moving):
                    game.words_moving = False
                    game.is_paused = True
                else:
                    game.words_moving = True
                    game.is_paused = False
        elif (event.type == pygame.MOUSEMOTION):
            check_game_mouse_position(mouse_position, buttons, game)
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            click_button(mouse_position, buttons, game)
    update_player_input(game, events)
        # TODO add functionality to return false and break the loop
    return True