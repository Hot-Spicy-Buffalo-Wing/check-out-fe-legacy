# check-out-fe

streamlit-based: Outfit Coordination Recommendation ... "Check out a lookbook for today's outfit!"

## features

1. main page에는 lookbook 이미지를 탐색할 수 있도록 다른 사람들의 lookbook 이미지가 쭉 있고, 오늘의 추천 받은 옷차림 사진이 나오는 공간이 있다. 오늘 추천받은 이력이 없으면 비어있다.
2. 비어있는 사진에는 "오늘의 옷차림을 추천받으세요!"라는 문구와 함께 lookbook을 생성할 수 있는 버튼이 있다.
3. 버튼을 누르면, 성별(여성, 남성, 논바이너리), 연령대(10대 초반, 10대 후반, 20대 초반,...), 사는 지역(선택 영역 세가지가 있고, 각각 list 형태로 선택할 수 있는 요소가 정의되어 있다. ex. 서울특별시 강남구 청담동), TPO 정보 (꾸안꾸, 여름코디, 캠퍼스룩, 결혼식 하객으로 참석, ...)
4. 생성하기 버튼을 누르면, api endpoint로 정보를 전달한다.
5. lookbook은 생성된 이미지와, 실제 제안된 코디와 같이 입은 나의 사진이 들어갈 수 있다. 실제 코디처럼 입은 후에 사진을 업로드할 수 있도록 한다.
