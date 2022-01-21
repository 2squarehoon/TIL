import json

def max_revenue(movies):
    movie_ids = [13, 122, 129, 155, 238, 278, 311, 424, 497, 550, 598, 637, 680, 914, 4935, 11216, 324857, 372058, 378064, 496243, 527774, 572154]
    budgets = []
    for movie_id in movie_ids:
        #movies.json에서 id들을 불러옴 / movies에서 for문 돌리는건 너무 오래걸릴 것 같아서 생략하고 movie_ids라는 리스트를 따로 만들어서 for문 돌림
        file_path = f"C:/Users/SH/Desktop/project/pjt01/data/movies/{movie_id}.json"
        with open(file_path, 'rt', encoding='UTF8') as json_file:
            movie_data = json.load(json_file)
            #id로 된 제목의 파일을 연다.
        budgets.append(movie_data['budget'])
        # budget값들을 리스트로 저장
    max_budget = max(budgets)
    # 최대 budget값을 찾음
    for movie_id in movie_ids:
        file_path = f"C:/Users/SH/Desktop/project/pjt01/data/movies/{movie_id}.json"
        with open(file_path, 'rt', encoding='UTF8') as json_file:
            movie_data = json.load(json_file)
        if movie_data['budget'] == max_budget:
            return movie_data['title']
            # budget값이 max_budget값과 같으면 title을 리턴함
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))