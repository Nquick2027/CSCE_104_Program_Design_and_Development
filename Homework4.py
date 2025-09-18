import requests

response = requests.get('https://raw.githubusercontent.com/priscian/nlp/master/OpenNLP/models/coref/acronyms.txt')

text_lines = response.text.split('\n')

acronyms = dict()

for line in text_lines:
    components = line.split('\t', 1)

    if len(components) > 1:
        if components[0] in acronyms.keys():
            acro = components[0].strip()
            mng = components[1].strip()
            acronyms[acro] += ', {}'.format(mng)
        else:
            acro = components[0].strip()
            mng = components[1].strip()
            acronyms[acro] = mng




search = ''

print('Welcome to the Acronym Search App!')

while True:
    search = input('Enter the Acronym ("End" to quit, "Add" to add acronym): ')

    if search in acronyms.keys():
        print('Acronym: {}, Meaning: {}'.format(search, acronyms[search]))
    elif search == 'End':
        break
    elif search == 'Add':
        term = input('Enter the new Acronym:')
        meaning = input('Enter the meaning of the Acronym: ')
        acronyms[term] = meaning
    else:
        print('Acronym {} was not found in the list'.format(search))