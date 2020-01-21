user = raw_input('What is your name?\n').title()


class Physical():
    """Physical Characteristics"""

    def __init__(self, username):
        self.username = username
        self.skin = []

    def chars(self):
        skin = self.skin
        if skin == 'black':
            print 'black'
        elif skin == 'yellow':
            print 'yellow'
        elif skin == 'red':
            print 'red'

username = Physical(user)
username.hair = 'black'
username.skin = []

print username.hair


color = 'black'

def skin():
    for color in skin:
        if color == 'black':
            print 'black'
        else:
            print 'alien'

print skin()
