import time

from jikanpy import Jikan
jikan = Jikan()

with open('../valid_id.txt','r') as f:
    valid_ids = f.readlines()


genres_keys = ['All','Action', 'Adventure','Comedy','Drama','Fantasy','Horror','Mystery','Romance','Sci-Fi','Slice of Life','Sports','Supernatural','Ecchi']

count = 0

for genre_key in genres_keys:
    for id in valid_ids:
        count +=1
        print(count)
        print(id)
        try:
            response = jikan.anime(int(id))
            genres_dicts = response['data']['genres']
            genres = [genre['name'] for genre in genres_dicts]
            if genre_key in genres:
                with open(f'{genre_key}.txt','a+') as f:
                    f.write(id)
            if count >= 2:
                time.sleep(3)
                count = 0
        except Exception as e:
            time.sleep(3)
            print(e)

