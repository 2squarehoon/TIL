import json
from pprint import pprint


def movie_info(movies, genres):
    result_list = []
    for movie in movies:
        lst = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids'] # id가 출력되어있었다는걸 처음엔 놓쳤습니다.
        result = {}
        for key_a in lst:
            result[key_a] = movie.get(key_a)
        for genre in genres:
            for i in range(len(result['genre_ids'])):
                if genre['id'] == result['genre_ids'][i]:
                    result['genre_ids'][i] = genre['name']
        result['genre_names'] = result.pop('genre_ids')
        result_list.append(result)
    return result_list        
    # 생각보다 간단해서 놀랐읍니다... 딱 두줄로 끝나다니

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))