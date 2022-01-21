import json
from pprint import pprint


def movie_info(movie, genres):
    lst = ['title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    result = {}
    for key_a in lst:
        result[key_a] = movie.get(key_a)
    for genre in genres:
        for i in range(len(result['genre_ids'])):
            if genre['id'] == result['genre_ids'][i]:  # 처음엔 인덱스 0과 1만으로 2개의 genre_ids값만 바꿨지만 다른 movie들은 genre_ids들이 여러개 있어서 for문으로 수정
                result['genre_ids'][i] = genre['name']
    result['genre_names'] = result.pop('genre_ids') # genre_ids key값을 genre_names로 바꾸는 메서드, 구글링 짱
    return result
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))