#### Functions


def list_benefits():
    print 'More organized code'
    print 'More readable code'
    print 'Easier code reuse'
    print 'Allowing programmers to share and connect code together'
    return

print list_benefits()

def build_sentence(info):
    for benefit in list_benefits:
        print benefit, ' is a benefit of functions!'

print build_sentence(list_benefits)
