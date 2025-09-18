import requests
# allows you to pull files from the internet

from bs4 import BeautifulSoup
# install using terminal command (windows): pip install BeautifulSoup4
# bs4 is the BeautifulSoup4 library
# BeautifulSoup is the class located in the library

# # find akk images on the sc.edu home age
# sc_page = requests.get("https://www.sc.edu/")

# # use the beautiful soup library
# soup = BeautifulSoup(sc_page.content, 'html.parser')
# # html.parser tells the code to read the code as html code

# # find all "img" tags
# img_list = soup.find_all("img")

# for each_img in img_list:
#     print(each_img.get("src"))
# print('Found {} images on the home page'.format(len(img_list)))


# # TODO: Find all links in the wikipedia home page (a or anchor tag)
# wiki_page = requests.get('https://en.wikipedia.org/')

# soup = BeautifulSoup(wiki_page.content, 'html.parser')
# link_list = soup.find_all('a')

# for each_link in link_list:
#     print(each_link.get("href"))
# print('Found {} links on the Wikipedia home page'.format(len(link_list)))

# TODO: Print the title, company, and locations for all 100 jobs
fake_jobs = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(fake_jobs.content, 'html.parser')
job_cards = soup.find_all('div', class_='card-content')

for job in job_cards:
    # print(job.find('h2').text)
    title = job.find('h2').text
    company = job.find('h3').text
    location = job.find('p', class_='location').text.strip()
    print('{} with {} ({})'.format(title, company, location))

