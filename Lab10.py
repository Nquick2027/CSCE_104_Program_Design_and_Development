import requests
from bs4 import BeautifulSoup

# TODO: download the page using requests
# StackOverflow website, top 45 unanswered questions with python tags
so_page = requests.get('https://stackoverflow.com/questions/tagged/python?tab=unanswered&pagesize=50')

text_lines = so_page.text.split('\n')

# TODO: using BeautifulSoup, extract the following from the list of questions: title, user, text excerpt
soup = BeautifulSoup(so_page.content, 'html.parser')
question_list = soup.find_all('div', class_='s-post-summary--content')
# print(len(question_list))

count = 0

for question in question_list:

    count += 1
    if count == 46:
        break

    print('\n======================== Question {} ========================\n'.format(count))
    title = question.h3.a.text.strip()
    user_div = question.find('div', class_="s-user-card--info")
    user = user_div.div.a.text.strip()
    text_excerpt = question.div.text.strip()
    print('{} ({}):\n{}'.format(title, user, text_excerpt))
    


# NOTE: you might need to get page 2 and page 3, to get to 45 (do lots of testing)

# TODO: print all 45 questions in the format "{title} ({user}):\n{excerpt}"
