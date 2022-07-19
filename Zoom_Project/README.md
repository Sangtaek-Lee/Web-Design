# Zomm Clone using NodeJS, WebRTC and Websockets


# Websocket

- Browser 가 요청을 했을 때만 (request <-> response) 데이터를 browser 가 받아올 수 있다.
- http 만을 이용하여 채팅을 구현하게 되면 일정 시간 마다 새로고침이 필요하다.
- 그래서 웹 소켓 프로토콜이 등장
- 웹 소켓 프로토콜은 http 와 달리 open <-> close 로 통신여부 결정
- 즉, Browser 가 Websocket을 이용해 server와 연결하게 되면 통신을 close 할때까지 open 되어있게 된다.
- websocket 은 bidirectional이다
- Websocket 서버를 통해 채널이용자에게 데이터를 보내준다
- websocket은 인원이 늘어날 수록 통신을 추적할 수 있도록 메모리 성능이 더 요구된다.

# WebRTC

- Browser가 server를 통해 통신하는데서 발생하는 문제 (수 많은 컨넥션으로 인한 딜레이, 서버가 꺼지면 통신이 끊긴다)를 개선하고자 Browser 끼리 연결하는 WebRTC 등장
- P2P (Peer to Peer) 방식
- 텍스트 뿐만 아니라 영상, 오디오 등 데이터를 주고 받을 수 있다.
- 브라우저끼리 연결하므로 중개자(server)가 없으니 속도가 빠르다.
- 확장성 제약이 있다. 화상 채팅방에 100명이 있다면 개인은 99명에 비디오를 받아와야 하고 99명에게 비디오를 업로드해야한다.


# Requirments
Backend
- ExpressJS, app.get(), Pug, (request, response)

Frontend
- Vanilla JavaScript, package.json, babel, nodemon

# Server Setup
package.json을 만들고 Babel과 Nodemon 설정을 하자

1. package.json 생성

package.json 생성 설정 수동으로 지정

```nmpm init```

package.json 을 생성하는데 default로 설정으로 만들겠다는 옵션 -y

```npm init -y```

package 설정 -> main, script를 지웠는데 왜 지웠는지 모르겠다.

2. Nodemon 설정

Nodemon : 서버 코드를 변경 할 때마다, 서버를 재시작하는 번거러움을 줄이기 위한 도구로 이를 자동으로 해준다.

Nodemon 설치

```npm i nodemon -D```

3. babel 설정

babel : babel is a javascript compiler 새로운 ESnext 문법을 기존 브라우저에 사용하기 위함 (brower 발전은 빠르다)



**NodeJS 로 서버 설정 (만들기)**

- creat file, folder ./

- 바벨 파일 만들기
  - babel.config.json

- 노데몬 파일 만들기
  - nodemon.json

- 소스폴더안에 서버파일 만들기
  - src/server.js

- 바벨 설치 core, cli, node

  - ```npm i @babel/core @babel/cli @babel/node -D```

- gitignore 파일 만들기

  - .gitignore

  - /node_modules 작성


- nodemon.json 작성 (exec (key) 하나만 실행하도록) ==> src/server.js에 대해 babel-node 명령문을 실행시키는것
  - ```{"exec": "babel-node src/server.js"}```

- babel preset-env 설치 : npm 설치와 babel 설정을 해주게 되면 후에 plugin들은 자동 설치하게 해준다.
  - ```npm i @babel/preset-env -D```
- babel.config.json 에서는 preset을 설정
  - ```{"preset": ["@babel/preset-env"]}```

- package.json에 script 작성
- package에서 dev를 호출할거고 dev는 nodemon을 홀출할것이다. nodemon은 nodemon.json을 살펴보고 실행할것이다
  - ```"script": {"dev": "nodemon"},```

- 작성해줄 set은 끝났고 express, pug
  - ```npm i express```
  - ```npm i pug```


- src/server.js 에서 express를 import, app 만들고, 3000 port로 listen
  - ```import express from "express"```
  - ```const app = express();```
  - ```app.listen(3000);```


- npm run dev 하면 서버 켜진다 console에 hellow 뜨고 localhost:3000 page 가 error가 아니다






