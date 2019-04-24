import bs4

with open("../other/before_tag.html", "r") as f:
    bef = f.read()

with open("../other/simple_tag.html", "r") as f:
    sim = f.read()

soup = bs4.BeautifulSoup(bef, "html.parser")

sim_soup = bs4.BeautifulSoup(sim, "html.parser")

sim_a_href = sim_soup.a.attrs['href']
sim_a_img_src = sim_soup.a.img.attrs['src']
sim_a_text = sim_soup.a.text
sim_img_src = sim_soup.find_all('img')[1].attrs['src']

# new_image_soup = new_tag('a', attrs={'href': sim_a_href, 'target': '_blank'})
# new_image_a_img = new_tag('img', attrs={'src': sim_a_img_src, 'style': 'border: none;'})
# new_image_a = new_image_soup.a
# new_image_a.append(new_image_a_img)

# new_image_img = new_tag('img', attrs={'src': sim_img_src, 'width': '1', 'height': '1', 'style': 'border: none;'})

# new_name_a

soup.find('div', class_='kaerebalink-image').a.attrs['href'] = sim_a_href
soup.find('div', class_='kaerebalink-image').img.attrs['src'] = sim_a_img_src
soup.find(
    'div',
    class_='kaerebalink-image').find_all('img')[1].attrs['src'] = sim_img_src

soup.find('div', class_='kaerebalink-powered-date').extract()
soup.find('div', class_='kaerebalink-name').a.attrs['href'] = sim_a_href
soup.find('div', class_='kaerebalink-name').a.string = sim_a_text
soup.find('div', class_='kaerebalink-name').img.attrs['src'] = sim_img_src

amz_div = soup.find('div', class_='shoplinkamazon')
soup.find('div', class_='shoplinkamazon').extract()
soup.find('div', class_='shoplinkrakuten').insert_before(amz_div)

with open("../other/after_tag.html", "w") as f:
    f.write(str(soup))