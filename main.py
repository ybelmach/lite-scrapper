"""Game searcher for site old-games.ru"""

import requests
import os

GAMES_ON_PAGE = 50
PAGES_NUM = 99
SITE_URL = 'https://www.old-games.ru/'

page_num = 1
game_photos = {}
game_ids = []


def get_games_on_page(resp: requests.models.Response):
    text_games_num = resp.text
    text_games_num = text_games_num[
                     text_games_num.find('<!-- Catalog begin -->') + len('<!-- Catalog begin -->'):text_games_num.find(
                         '<!-- Catalog end -->') + len('<!-- Catalog end -->')]
    count = 0
    while True:
        tr = text_games_num.find('game_')
        if tr != -1:
            count += 1
            text_games_num = text_games_num[tr + len('game_'):]
        else:
            return count


def photo_search(resp: requests.models.Response) -> list:
    def get_photo_num(text_photos_num: str) -> int:
        count = 0
        while True:
            a = text_photos_num.find('</a>')
            if a != -1:
                count += 1
                text_photos_num = text_photos_num[a + len('</a>'):]
            else:
                return count

    photos_hrefs_list = []
    photos_text = resp.text
    photos_text = photos_text[
                  photos_text.find('<aside class="game_main_left game_small_screens">'):photos_text.find(
                      '</aside>')]
    photo_num = get_photo_num(photos_text)
    if photo_num == 0:
        return []
    for j in range(1, photo_num + 1):
        # print(photos_text)
        href = SITE_URL + photos_text[
                          photos_text.find('href="') + len('href="'):photos_text.find('"',
                                                                                      photos_text.find('href="') + len(
                                                                                          'href="'))]
        # if not ((href.find('.jpg') == -1 and href.find('.png') == -1) or href.find(' ') != -1):
        photos_hrefs_list.append(href)
        # else:
        #     raise Exception(f"[ERROR] href {href} is invalid! text: {photos_text}.")
        print(f"[INFO] Photo {j} href saved successfully; href={href}.")
        photos_text = photos_text[photos_text.find('<br/>') + len('<br/>'):]
    # print(photos_text)
    return photos_hrefs_list


for page_num in range(1, PAGES_NUM + 1):
    response = requests.get(f'https://www.old-games.ru/catalog/?platform=2&page={page_num}')
    if response.status_code != 200:
        raise Exception(f'[ERROR] Page {page_num} not found!')
    text = response.text
    # print(text)
    text = text[text.find('<!-- Catalog begin -->'):text.find('<!-- Catalog end -->')]
    # print(text)
    counter = 0
    START_POS = 0
    GAMES_ON_PAGE = get_games_on_page(response)
    print(f"[INFO] Games on page {page_num}: {GAMES_ON_PAGE}")
    for game in range(GAMES_ON_PAGE):
        START_POS = text.find('id="game_') + len('id="game_')
        for i in range(5, 0, -1):
            try:
                game_ids.append(int(text[START_POS:START_POS + i]))
                text = text[START_POS + i:]
                break
            except ValueError:
                continue
        print(f"[INFO] =={page_num}== START_POS = {START_POS}; pre_num: {text[START_POS:START_POS + 5]}")
    if len(game_ids) < GAMES_ON_PAGE:
        raise Exception(f'[ERROR] Not enough games in site {page_num}!')
    print(f"[INFO] Game ids on page {page_num}: {game_ids}.")
    print(f"[INFO] Start searching for games.")
    for i in range(GAMES_ON_PAGE):
        game_id = game_ids[i]
        response = requests.get(f'https://www.old-games.ru/game/{game_id}.html')
        if response.status_code != 200:
            raise Exception(f'[ERROR] Game {game_id} not found. (game number {i} on site {page_num})!')
        print(f"\n[INFO] =={page_num}.{i}== game_id: {game_id}; response_code: {response.status_code}")
        url = photo_search(response)
        if not url:
            game_photos[game_id] = [f"game_id={game_id}", ]
        else:
            game_photos[game_id] = url
    print()
    print(game_photos, '\n')
    path = os.path.dirname(__file__) + os.sep + 'screenshots'
    if os.path.exists(path):
        print(f"[INFO] Path already exists.")
    else:
        os.mkdir(path)
        print(f"[INFO] Path created.")

    while len(game_photos) != 0:
        game_set = game_photos.popitem()
        game_ids = game_set[0]
        game_urls = game_set[1]
        counter = 1
        for url in game_urls:
            url_num = url.find('game_id=')
            if url_num != -1:
                game_id = int(url[url_num + len('game_id='):])
                response = requests.get(f'https://www.old-games.ru/game/{game_id}.html')
                s = f"URL: https://www.old-games.ru/game/{game_id}.html\n\n\n{response.text}"
                with open(path + os.sep + str(game_id) + '.txt', "w") as file:
                    file.writelines(s)
                    print(f"[INFO] File {str(game_id) + '.txt'} has been saved.")
            else:
                resolution = url[url.rfind('.'):]
                filename = str(game_ids) + '_' + str(counter) + resolution
                with open(path + os.sep + filename, "wb") as file:
                    file.write(requests.get(url).content)
                    print(f"[INFO] File {filename} has been downloaded and saved.")
            counter += 1
    print(f"[INFO] Games images from page {page_num} saved.")
    game_ids, game_photos = [], {}
print(f"\n\n\n\n\n\n\n\n\n\n[INFO] All games images saved successfully.")
