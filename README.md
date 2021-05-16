## 풀이

- 백준
- 프로그래머스
- leetcode

## 기록

[내 기록](https://www.notion.so/bbaktaeho/CodingTest-Study-0096329e66aa49ff9aac4b435b585174)

## 꿀팁

- **Python**
  - 문자열 슬라이싱은 내부적으로 매우 빠르게 동작한다.
  - sorted() 함수는 `Timsort` 알고리즘이다.
    - 대부분의 데이터는 어느정도 정렬되어있다고 가정한 개빠른 소팅
  - Counter 클래스
    - Iterator의 요소들을 카운트해서 Dict 자료구조로 만들어줌
    - most_common() 메서드로 가장 흔하게 등장하는 요소를 List안의 Tuple로 리턴해줌
  - set
    - 차집합을 구할 때는 두 set 자료형을 뺄셈으로 구할 수 있음 `set(a) - set(b)`

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

- 문자열이 숫자인지 확인

  ```python
  # python
  "".isdigit() # 숫자라면 Tue, 숫자가 아니라면 False

  # javascript
  isNaN("") // 숫자가 아니라면 true, 숫자라면 false,
  ```

- 지정된 소수점까지 반올림 (소수점 2번째 위치까지 반올림)

  ```python
  # python
  round(숫자, 2)

  # javascript
  숫자.toFixed(2)
  ```

- 리스트 펼치기

  ```python
  # python
  print(*[1,2,3,4])

  # javascript
  console.log(...[1,2,3,4])
  ```
