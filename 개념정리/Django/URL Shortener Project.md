# URL Shortener Project 🔗

> 가끔씩 **너무 길어서 공유하기 조금 불편한 URL들이 있죠. 이런 URL들을 짧고 간결하게 단축해주는 서비스를 만들어봅시다-!**

# 기술스택

- Django
- DRF(Django REST Framework)
- SQLite3

# 요구사항

- 단축된 URL의 기본 형식은 영문과 숫자의 조합으로 구성된 7자리로 코드로 구성

  합니다.

  - (예시) `www.naver.com/news/some-long-thingy` ⇒ `localhost:8000/a8bxL0`
  - (조건) 단축 전 URL의 길이와 상관없이 7자리로 고정합니다.
  - (조건) 문자 변환에 사용되는 알고리즘은 직접 선정합니다.
  - (조건) 기존에 단축된 URL들과 중복되어서는 안됩니다.

- 단축 URL의 이름을 기본값이 아닌 유저가 원하는 형식으로 설정 할 수도 있습니다.

  - (예시) `www.naver.com/news/some-long-thingy` ⇒ `localhost:8000/naver-news`
  - (조건) 기존에 단축된 URL들과 중복되어서는 안됩니다.

- 단축 URL을 코드 또는 유저가 지정한 이름으로 해제 요청할 수 있습니다.

- 단축된 URL로 요청이 들어올 경우, 원래 URL로 Redirect합니다.

  - (예시) `localhost:8000/a8bxL0` ⇒ `www.naver.com/news/some-long-thingy`

## (예시) Database Modeling

*예시는 참고용입니다. 실제 설계는 여러분만의 고민을 담아서 직접 만들어주세요.*

| Field        | Type     |
| ------------ | -------- |
| original_url | URLField |
| short_url    | URLField |

## (예시) API Endpoints

*예시는 참고용입니다. 실제 설계는 여러분만의 고민을 담아서 직접 만들어주세요.*

| Description           | URL         | Method | Payload* |
| --------------------- | ----------- | ------ | -------- |
| 단축 URL 접근         | /:short_url | GET    |          |
| 전체 단축 URL 조회    | /urls/      | GET    |          |
| 단축 URL 생성         | /urls/      | POST   | {        |
| “original_url”: text, |             |        |          |
| “short_url: text      |             |        |          |
| }                     |             |        |          |
| 개별 단축 URL 조회    | /urls/:pk   | GET    |          |
| 개별 단축 URL 삭제    | /urls/:pk   | DELETE |          |

- *Payload는 무엇인가요?

  Payload는 네트워크 요청을 보낼 때 HTTP Body에 담기는 내용을 말합니다.

# 참고자료

## 유사 서비스

- https://short.io/ko/
- https://bitly.com/
- https://www.rebrandly.com/

## 학습 자료

- [초보 개발자의 url shortner 서버 만들기 1편](https://medium.com/monday-9-pm/초보-개발자-url-shortener-서버-만들기-1편-base62와-춤을-9acc226fb7eb)
- [서울 42 교육생의 url shortner 개발기](https://42place.innovationacademy.kr/archives/9063)
- [django를 이용하여 url shortner 만들기](https://geekflare.com/build-url-shortener-app-in-django/)