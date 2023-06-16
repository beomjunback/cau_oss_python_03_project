'''
parking_spot_manager모듈은
parking_spot 클래스를 제공합니다.
생성자, get메소드, __str__특수 메소드를 제공합니다.
그 외에 str_list_to_class_list 함수는 str형식의 리스트를 객체 리스트로 저장하여 반환합니다.
print_spots 함수는 매게변수로 받은 리스트의 인덱스를 하나씩 전부 출력합니다.
filter_by_~~ 함수는 사용자가 원하는 딕셔너리의 키값을 기준으로 필터링하고 그 리스트를 반환합니다.
sort_by_keyword 함수는 입력 받은 keyword를 기준으로 정렬하여 반환합니다.
'''
class parking_spot:
    __item = {} #딕셔너리 생성
    
    def __init__(self,name,city,distict,ptype,longitude,latitude):
        self.__item =\
            {
             'name':str(name),
             'city':str(city),
             'district':str(distict),
             'ptype':str(ptype),
             'longitude':float(longitude),
             'latitude':float(latitude)
            }
        
    def get(self,keyword='name'): #__item의 value를 반환
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list): #객체 생성
    list_allinfo =[]
    for i in str_list:
        info = i.split(",")
        name = info[1]
        city = info[2]
        district = info[3]
        ptype = info[4]
        longitude = info[5]
        latitude = info[6]
        spot = parking_spot(name,city,district,ptype,longitude,latitude)
        list_allinfo.append(spot)
    return list_allinfo

def print_spots(spots): #출력
    print(f"---print elements({len(spots)})---")
    for i in spots:
        print(i)
        
def filter_by_name(spots, name): #name을 기준으로 필터링
    filtered_list = [spots[i] for i in range(len(spots)) if name in spots[i].get('name')]
    return filtered_list

def filter_by_city(spots, city): #city을 기준으로 필터링
    filtered_list = [spots[i] for i in range(len(spots)) if city in spots[i].get('city')]
    return filtered_list

def filter_by_district(spots, district): #distirct을 기준으로 필터링
    filtered_list = [spots[i] for i in range(len(spots)) if district in spots[i].get('district')]
    return filtered_list

def filter_by_ptype(spots, ptype): #ptype을 기준으로 필터링
    filtered_list = [spots[i] for i in range(len(spots)) if ptype in spots[i].get('ptype')]
    return filtered_list        

def filter_by_location(spots,locations): #longitude와 latitude의 값을 기준으로 필터링
    filtered_list = [
        spots[i] for i in range(len(spots))
        if spots[i].get('longitude')>locations[2] and
            spots[i].get('longitude')<locations[3] and
            spots[i].get('latitude')>locations[0] and
            spots[i].get('latitude')<locations[1]
    ]
    return filtered_list

def sort_by_keyword(spots,keyword): #입력된 keyword의 벨류값들을 정렬
    sorted_list = sorted(spots,key = lambda x:x.get(keyword))
    return sorted_list

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    spots = filter_by_district(spots, '동작')
    print_spots(spots)
    
    # version#4
    spots = sort_by_keyword(spots, 'name')
    print_spots(spots)