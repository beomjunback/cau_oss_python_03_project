'''
menu_selector 모듈은
start_process 함수를 제공합니다. 이는
메뉴에 표시된 원하는 옵션을 입력받고 실행합니다.
현재 완성된 기능: "[1] print", "[2] filter", "[4] exit"
사용자가 1번을 택할시 "got"을 parking_spot_manager의 클래스의 형식에 맞게 출력합니다.
사용자가 2번을 택할시 원하는 key값을 기준으로 필터링할 수 있습니다.
사용자가 4번을 택할시 프로그램을 종료합니다. 그전까지 반복합니다.
'''    

import parking_spot_manager as psm
import file_manager as fm

def start_process(path):
    
    got = psm.str_list_to_class_list(fm.read_file(path))
    
    while True:
        print("---menu---") #메뉴를 표시합니다.
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1: #1번 선택시 전부 출력합니다.
            psm.print_spots(got)
        elif select == 2: #2번 선택시 필터링 메뉴 출력
            got = psm.str_list_to_class_list(fm.read_file(path)) #got 초기화
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1: #1번 : name을 기준으로 필터링
                keyword = input('type name:')
                got = (psm.filter_by_name(got,keyword))
            elif select == 2: #2번 : city을 기준으로 필터링
                keyword = input('type city:')
                got = (psm.filter_by_city(got,keyword))
            elif select == 3: #3번 : district을 기준으로 필터링
                keyword = input('type district:')
                got = (psm.filter_by_district(got,keyword))
            elif select == 4: #4번 : ptype을 기준으로 필터링
                keyword = input('type ptype:')
                got = (psm.filter_by_ptype(got,keyword))
            elif select == 5: #5번 : 경도와 위도의 최대 최소값을 기준으로 필터링
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                minmax = (min_lat,max_lat,min_lon,max_lon)
                got = (psm.filter_by_location(got,minmax))
            else: #input 오류
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4: #4번 선택시 프로그램을 종료합니다.
            print("Exit")
            break
        else:
            print("invalid input")