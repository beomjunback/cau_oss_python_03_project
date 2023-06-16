'''
menu_selector 모듈은
start_process 함수를 제공합니다. 이는
메뉴에 표시된 원하는 옵션을 입력받고 실행합니다.
현재 완성된 기능: "[1] print", "[4] exit"
사용자가 1번을 택할시 path로 받은 정보를 모두 parking_spot_manager의 클래스의 형식에 맞게 출력합니다.
사용자가 4번을 택할시 프로그램을 종료합니다. 그전까지 반복합니다.
'''    

import parking_spot_manager
import file_manager

def start_process(path):
    
    got = parking_spot_manager.str_list_to_class_list(file_manager.read_file(path))
    
    while True:
        print("---menu---") #메뉴를 표시합니다.
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1: #1번 선택시 전부 출력합니다.
            parking_spot_manager.print_spots(got)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
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