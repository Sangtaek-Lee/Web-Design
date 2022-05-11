server
web server : request가 왔을 때 **web page를** response의 body에 정보를 담아 준다.
api server : request 를 처리하고 **요청한 것을** response의 body에 담아 준다.

http : hypertext transfer protocol 클라이언트와 서버가 서로 어떤 형식으로 데이터를 보내 줄 건지 약속한 것 규약

웹 개발은 http, https (s : secure)  을 사용한다.



## http

- 비 연결성 (Connectless) 클라이언트와 서버가 한 번 응답을 주고 받으면, 연결을 끊는다.

- 무상태(Stateless) : 비 연결 성 때문에 발생 서버가 클라이언트를 기억하지 못함(식별 불가능

  매번 요청할 때마다, 내가 누군지를 서버에게 알려줘야 한다.

- 매번 알려주는 불편함을 해결하기 위해 쿠키와 세션이 등장
  쿠키 - 클라이언트가 기억해서 서버에 가져감 (보안이 취약하여 세션이 등장)
  세션 - 민감한 정보, 서버가 기억한다.

- Method : request에서 어떤걸 요청하는 지, head 와 body로 구분 되어 있다.
  head : 요청에 대한 부가정보, method (header : head 안에 있는 각각 정보 쌍 key : value)
  body :  실제 데이터, POST, PUT 만 data 가 존재

- response : head, body 로 구성
  head : 상태코드 (Status Code)를 가지고 있다. (상태코드는 각각 의미를 가진 상태 메세지를 가지고 있다.)
  - 상태코드 5가지 그룹
    100 : 서버가 클라이언트한테 정보성 응답 (100 : Continue 클라이언트가 서버에 계속 요청 가능한지 )
    200 : 일반적인, 정상적인 상황 (200 : OK 성공적으로 처리됨, 201 : Created 클라이언트 요청대로 리소스가 잘 생성됨)
    300 : 클라이언트 요청을 하기위해 추가 작업이 필요한 상황 ( 301 : Moved Permanently 리소스 위치가 옮겨져있다. 그래서 리다이렉트 해주겠다. 304 : Not Modified 수정사항이 없다는 정보를 줘 서버가 재 조회하는데 네트워크 자원을 아낄 수 있다. 캐싱)
    400 : 클라이언트 문제 ( 401 : Unauthorized 인증해야 한다. 403 : Forbidden 권환이 있어야 한다. 404 : Not Found 리소스가 없다. 429 : Too many Requests 짧은 시간에 많은 요청이 발생했을 때)
    500 : 서버 문제 (500 : Internal Server Error 서버 내부 에러 503 : Service Unavailable 많은 요청이 들어 왔을 때 처리하지 못하는 경우)

- Resource : 서버에 존재하는 정보
- URI(Uniform Resource Indentifier)는 URL(Locator), URN(Name) 이 있지만 URN은 거의 안쓰인다. 그래서 URI 를 URL 로 부른다
- URL Resource의 위치 정보
- Scheme (protocol) : http
- Host (Domain name) : ip adress -> 이름으로
- Port : 웹 서버상 리소스에 접근하기 위한 gate
- Path : 웹 서버 상의 리소스 경로
- Query (Identifier) : 옵션,  & 로 구분되는 key = value
- Fragment : Anchor, 특정 부분을 보여 주기 위해, 북마크



## RESTful API

- Web API : 프론트엔드와 백엔드가 정보를 교환할 때 약속
- REST API (Representational State Transfer) : Web API를 설계할 때 가이드 라인
- 1. URL은 리소스를 나타내기 위해서만 사용하고, 리소스에 대한 처리는 메서드로 표현한다.
  2. Doucumnet는 단수명사로, Collection은 복수 명사로 표현한다.
     Doucument 가 모여 Collection 을 이룬다. (예 article이 모여 articles 를 이룬다.)



## Response

- 직렬화























