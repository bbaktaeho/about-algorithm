## 풀이

- 백준
- 프로그래머스
- leetcode

## 기록

[내 기록](https://www.notion.so/bbaktaeho/CodingTest-Study-0096329e66aa49ff9aac4b435b585174)

## 꿀팁

- Python
  - 문자열 슬라이싱은 내부적으로 매우 빠르게 동작한다.
  - sorted() 함수는 `Timsort` 알고리즘이다.
    - 대부분의 데이터는 어느정도 정렬되어있다고 가정한 개빠른 소팅
  - Counter 클래스
    - Iterator의 요소들을 카운트해서 Dict 자료구조로 만들어줌
    - most_common() 메서드로 가장 흔하게 등장하는 요소를 List안의 Tuple로 리턴해줌

## Python vs JavaScript

- 리스트를 문자열로 (리스트의 구분자로 \n 특수문자 지정)

  ```python
  # python (문자열 타입의 리스트만 가능)
  "\n".join(리스트)

  # javascript
  리스트.join("\n")
  ```

- 슬라이싱

  ```python
  # python
  문자열[1:]
  문자열[2:5]

  # javascript
  문자열.slice(1)
  문자열.slice(2,5)
  ```

- 문자열 또는 리스트 리버싱

  ```python
  # python
  반복자[::-1]

  # javascript
  문자열.split("").reverse().join("")
  ```
