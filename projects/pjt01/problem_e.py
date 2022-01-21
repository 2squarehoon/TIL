import json


def dec_movies(movies):
    movie_ids = [13, 122, 129, 155, 238, 278, 311, 424, 497, 550, 598, 637, 680, 914, 4935, 11216, 324857, 372058, 378064, 496243, 527774, 572154]
    december_list = []
    for movie_id in movie_ids:
        file_path = f"C:/Users/SH/Desktop/project/pjt01/data/movies/{movie_id}.json"
        with open(file_path, 'rt', encoding='UTF8') as json_file:
            movie_data = json.load(json_file)
        if movie_data['release_date'][5] + movie_data['release_date'][6] == '12': #string index로 release date 사이의 '12'를 찾기
            december_list.append(movie_data['title']) # title key의 value들을 december_list에 append해서 list로 만들기
    return december_list        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))