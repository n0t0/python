#### Exercises

#   Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
    print 'Hello ' + name
hello_name('Bob')

# ABBA

def makeabba(hi, bye):
    print (1, 2)+(2, 1)

print makeabba(1,2)

#   The web is built with HTML strings like "<i>Yay</i>"
#   which draws Yay as italic text. In this example, the
#   "i" tag makes <i> and </i> which surround the word "Yay".
#   Given tag and word strings, create the HTML string with
#   tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
    
