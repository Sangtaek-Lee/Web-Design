# Git Branch

- master branch : 상용 버전

- HEAD : 현재 가르키는 위치 (브랜치 이동은 헤드의 이동이다)

- git init

- touch 파일

- git log

- git log --oneline

- git log --oneline --all : 전체 브런치 log

- git log --oneline --all  --graph : 브랜치를 시각적으로 확인

- git branch : 브랜치 목록 확인

- git branch 브랜치이름 : 새로운 브랜치 생성

- git branch -d 브랜치이름 : 특정 브랜치 삭제(병합된 브랜치만 삭제)

- git branch -D 브랜치이름 : 강제 삭제

- git switch 브랜치이름 : 다른 브랜치로 이동

- git switch -c 브랜치이름 : 브랜치를 새로 생성과 동시에 이동

- 주의 사항 : git의 관리를 받고 있어야지만 버전관리가 된다 예) 마스터에서 브랜치로 이동하여 새로운 파일을 만들었지만 월킹 아레아에서 스테이징 아레아로 add, commit 하지 않았다면 이는 git tree에서 벗어나 관리되지 않아 관리가 꼬이게 된다.

- ### merge (병합)

- git merge 병합할 브랜치 이름 : merge 하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야 함

- merge 진행 하면 브랜치는 역할을 다했으므로 삭제한다.

- 시나리오 (마스터 기준 병합)
  - fast-forward : 머지 하였지만 master 브랜치의 최신버전에서 나온 브랜치이기 때문에 머지 하였지만 커밋은 마스터와 브랜치가 합쳐진 버전이 되어 새로 생정 되지 않고 헤드가 마스터와  브랜치를 같이 가르킨다. 단순히 헤드가 최신버전으로 나아가는 것 
  - 3-way merge (merge commit) : 마스터 커밋과 브랜치 커밋의 공통 조상인 commit 을 기준으로 머지하여 새로운 커밋을 만들어 낸다.
  - merge conflict : merge하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면 git은 해당 부분을 자동으로 merge 해주지 못함. 반면 동일 파일이더라도 서로 다른 부분을 수정했다면 conflict 없이 자동으로 merge commit 된다.

- ## vim

- :wq : 쓰고 종료