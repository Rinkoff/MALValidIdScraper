import time
from jikanpy import Jikan

jikan = Jikan()


id_list = []
curr_id = 1
save_checkpoint = 0

for _ in range(1,20000):
    # Escape Jikan Rate limit exception HTTP429
    for _ in range(3):
        try:
            save_checkpoint += 1
            response = jikan.anime(curr_id)
            genres_dicts = response['data']['genres']
            genres = [genre['name'] for genre in genres_dicts]
            # Remove genres
            if 'Hentai' in genres or 'Avant Garde' in genres:
                curr_id+=1
                continue
            # Remove untitled
            if response['data']['title'] == 'LET\'S ALL LOVE LAIN':
                curr_id+=1
                continue

            id_list.append(response['data']['mal_id'])

        except Exception as E:
            pass
        curr_id += 1
    else:
        with open('valid_ids.txt', 'a+') as file:
            for id in id_list:
                file.write(f"{str(id)}\n")
                print("saved")
        id_list.clear()
    time.sleep(3)

