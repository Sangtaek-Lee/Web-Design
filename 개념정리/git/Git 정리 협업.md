# **Git**

VCS (Version Control System) - 버전 관리 시스템





https://techblog.woowahan.com/2553/

https://lhy.kr/git-workflow



## Workflow

working directory



staging area



.git directiory





## Set Up

- 실무에선 CLI 가 주 이지만 GUI 혼용하기도 한다.

  

**- CLI**

- Terminal - Git bash, cmder(git 내장되어 있다.)

```
Git 설치 확인
git --version
```

**- GUI** (CLI 대비 기능이 한정)

- Application - Sorucetree(추천), GitKraken



**초기 설정**

설정 파일 .gitconfig

```bash
# 설정 정보 확인
git config --list

# 설정 정보 기본 에디터로 열기
git config --global -e

# 설정 정보 VSCODE로 열기
git config --global core.editor "code" 			# Teriminal 활성화 상태
git config --global core.editor "code --wait"	# Editor 종료 전까지 Terminal 비활성화

git config --global -e						# global 설정 된 에디터로 config 파일 실행

# global 변수 설정
git config --global user.name "username"
git config --global user.email "useremail"

# global 변수 확인
git config user.name
git config user.email


# global CRLF 설정 (CR: Carriage Return 커서를 맨 앞으로 (\r), LF : Line Feed 커서 위치 고정 다음 라인으로 (\n)) ..... Git 은 default lf

## mac default lf ==> Git 에 저장할 때 cr 지워준다.
git config --global core.autocrlf input
## window default crlf ==> Git 에 가져올 때 cr 붙여준다.
git config --global core.autocrlf true

# 기본 브랜치명 변경 요즘은 그냥 defalut main이긴 하다
git config --global init.defaultBranch main
cat ~/.gitconfig
```



**기본 문법** -- https://git-scm.com/docs (명렁어 참고, 명령어 사용가능 Option 확인)

```bash
git command -option
```

```bash
# git local repository 생성 (.git) 
git init

# <-> git init 제거
rm -rf .git
```

```bash
# repository 상태 확인
git status

# 명령어 단축 설정
git config --global alias.st status		# git status ==> git st
```

```bash
# 명령어 option 확인
git 명령어 --h
```















