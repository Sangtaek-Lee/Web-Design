django - model



sql  : database 다루는 언어

orm : sql 언어를 python으로 감싸 python 문법으로 사용 (java에도 존재)

migrations : model 의 히스토리를 쌓는거

CRUD : Create Read Update Delete (생성, 읽기, 수정, 삭제) 프로그램의 기본적인 기능

# Model

- Model
  - 단일한 데이터에 대한 정보를 가짐 (django 데이터 구조)
  - 웹 애플리케이션(장고)의 데이터를 구조화하고 조작(CRUD)하기 위한 도구

- 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - Query를 날린다 -> DB 조작한다.
- 데이터베이스(DB)
  - 체계화된 데이터의 모임
- Database의 기본 구조
  - 스키마(Schema)
    - 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조 (structure)
  - 테이블(Table)
    - 열(column) : 필드(Field) or 속성
    - 행(row) : 레코드(record) or 튜플
  - PK(Primary Key : 기본키) 
    - 중복 불가, 데이터 베이스 관리 및 설정시 주요하게 활용

# ORM

- ORM (Object Relational Mapping) : **DB를 객체(object)로 조작하기 위해 ORM을 사용**

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터(장고 - sql)를 변환하는 프로그래밍 기술
- Django 는 내장 Django ORM을 사용함
- sql vs nosql 두 구조가 있다.
- SQL을 잘 알지 못해도 DB 조작이 가능
- SQL의 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성
- ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것. (생산성)



# Model 사용 (순서, 설명 등)

1. ```python
   # 각 모델은 django.models.Model 클래스의 서브 클래스로 표현됨
   # django.db.models 모듈의 Model 클래스를 상속받음
   from django.db import models
   							
   # applications/models.py 에서 model을 정의
   # models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의
   # title과 content는 모델의 필드를 나타냄
   # 각 필드는 클래스 속성으로 지정되어 있으며, 각 속성은 각 데이터베이스의 열에 매핑
   class Article(models.Model):
       title = models.CharField(Max_length=10)
       content = models.TextField()
   ```

- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - CharField의 max_length는 필수 인자
  - 필드의 최대 길이(문자), 데이터베이스 레벨과 Django의 유효성 검사(값을 검증하는 것)에서 활용
- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영은 되지만 모델과 데이터베이스 수준에서는 적용되지 않음 (max_length 사용은 CharField)





python manage.py sqlmigrate app.name 0001 # sql로 변환 된 데이터

```
# 마이그레이션 파일 생성 
$ python manage.py makemigrations <app-name> 
# 마이그레이션 적용 
$ python manage.py migrate <app-name> 
# 마이그레이션 적용 현황 
$ python manage.py showmigrations <app-name> 
# 지정 마이그레이션의 SQL 내역 
$ python manage.py sqlmigrate <app-name> <migration-name>
```

DateTimeField auto_now_add 최초 생성 시간, auto_now 조작 시 마다



DB 와 ORM 사이 data를 바로 조작하고 볼 수 있는 환경이 있다.

환경 접속



# Create

$ python manage.py shell

데이터 row 생성

#인스턴스를 만들고 save

article = Article()

article.attribute = "data"

article.save()

#keyword 인잘르 넘기는 방식

article = Article(attribute = "")

article.save()

#create() 이용하는 방법 save 자동

Article.objects.create(attribute="")

# Read

objects.get()  은 반드시 한가지 데이터만 가져옴 2개 이상은 error

objects.filter()

# Update

article.attribute = "data" 로 덮어 쓰면 된다.

# Delete

article = Article.objects.get(id="")  지울 내용 담는다

article.delete()								지운다.







# 관리자

/admin

python manage.py  createsuperuser  로그인 계정 생성





http method 시멘틱한 의미가 있다.

get : 기본값, 서버 리소스를 요청할 때, url에 query string 으로 보낸다.

post : 리소스를 생성,수정,삭제할때, body 안쪽에 data를 숨겨 보낸다.



데이터를 추가할 때 url query로 submit 하면 query 조작, 새로고침으로 계속 데이터가 추가 될 수 있다는 문제가 있다.

csrf 공격 사용자인척 공격하는것

csrf token 을 이용해 토큰 값 비교해 방어

POST 는 CSRF Token 을 항상 사용해야 된다. 

장고는 {% csrf_token %} 태그를 작성해 주면 자동으로 토큰 비교해준다.

settings 의 middleware 에 보면 csrf 가 있다. middleware는 요청시 거쳐가야 되는 중간 장소