import json
from pprint import pprint


def movie_info(movie):
    lst = ['title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    result = {} # result를 dictionary형태로 만듦
    for key_a in lst:
        result[key_a] = movie.get(key_a) # lst에서 key를, 그 key와 get을 통해서 value를 불러와서 result에 dictionary 형태로 추가함
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))