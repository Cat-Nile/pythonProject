<div align="center">

  # 원티드랩 파이썬 서버개발자 과제 전형

</div>

## 목차
- [개발 기간](#--개발-기간--)  
- [프로젝트 설명 분석](#-프로젝트)
- [개발 조건](#-개발-조건)
- [실행방법](#실행-방법)
- [기술 스택](#기술-스택) 
- 
<br><br>
<div align="center">

  <h2> ⌛ 개발 기간  </h2> 
 2022/08/12  ~ 2022/08/10
 <br><br>
  </div> 


# 💻 프로젝트
  ### 프로젝트 설명

  - 댓글 기능이 있는 익명 게시판 키워드 알림 기능 구현
  - 아래의 요구사항을 만족하는 DB 테이블과 REST API를 만들어주세요.
    - 개발은 Python에 FastAPI 혹은 Flask로 구현해야 합니다.
    - 데이터베이스는 MySQL, MariaDB 중 택일입니다.
    - 게시판 기능 
      - 게시판은 제목, 내용, 작성자 이름, 비밀번호, 작성일시, 수정일시로 구성되어 있습니다.
      - 로그인 기능 없이 작성자도 입력 파라미터로 받습니다.
      - 게시판은 제목, 작성자로 검색이 가능합니다.
      - 게시글 작성, 수정, 삭제가 가능합니다.
      - 게시글 작성시에는 비밀번호를 입력받고, 수정/삭제시 입력한 비밀번호가 맞는 경우만 가능합니다.
      - 게시글에는 댓글을 작성할 수 있습니다.
      - 댓글은 내용, 작성자, 작성일시로 구성되어 있습니다.
      - 댓글의 댓글까지 작성이 가능합니다.
      - 게시물, 댓글 목록 API 는 페이징 기능이 있어야 합니다.
    - 키워드 알림 기능
      - 키워드 알림 테이블은 작성자 이름, 키워드 컬럼을 포함하고 있어야 하고 편의상 작성자는 동명이인이 없다고 가정합니다.
      - 작성자가 등록한 키워드가 포함된 게시글이나 코멘트 등록시 알림을 보내줍니다.
      - 키워드 등록/삭제 부분은 구현을 안하셔도 됩니다.
      - 알림 보내는 함수 호출하는 것으로만 하고 실제 알림 보내는 기능은 구현하지 않습니다.
      <div>
        <br>
      </div>
    - 구현 및 작성 목록
      - DB 스키마 생성 스크립트
      - 게시글 목록 API
      - 게시글 작성 API
      - 게시글 수정 API
      - 게시글 삭제 API 
      - 댓글 목록 API
      - 댓글 작성 API
      - 게시물 또는 댓글 등록시 알림 기능 구현

### API 명세서

| ID   | URI                                | METHOD | 기능                   |
| ---- |------------------------------------|--------| ----------------------|
| 1    | /api/posts                         | GET    | 게시글 리스트 조회           |
| 2    | /api/posts                         | POST   | 게시글 생성                |
| 3    | /api/posts/<int:postid>            | GET    | 게시글 단건 조회            |
| 4    | /api/posts/<int:postid>            | PUT    | 게시글 수정                |
| 5    | /api/posts/<int:postid>            | DELETE | 게시글 삭제               |
| 6    | /api/posts/<int:postid>/comments   | GET    | 게시글 댓글 목록 조회         |
| 7    | /api/posts/<int:postid>/comments   | POST   | 게시글 생성                |



  ### 🚥 개발 조건 

  #### 🙆‍♂️ 필수사항  
    - Python, Flask, MySQL 5.7
    - REST API 구현
    - DDL
    - DB를 이용한 키워드 알림 기능
  #### 🔥 선택사항
    - Docker
    - Unit test codes  
    - REST API Documentation (Swagger UI)

## 실행 방법

```
📌 Dependency

# 로컬에서 바로 서버 구동
pip install -r requirements.txt
set FLASK_APP=app.py flask run

# 도커 실행
pip install docker
pip install docker-compose
docker-compose up -d (도커 실행 후 15초 이후에 실행시켜주세요)
```
## 기술 스택

> - Back-End :  <img src="https://img.shields.io/badge/Python 3.10-3776AB?style=flat&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/flask-009688?style=flat&logo=flask&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL 8.0-4479A1.svg?style=flat&logo=mysql&logoColor=white"/>
>
> - ETC　　　:  <img src="https://img.shields.io/badge/Git-F05032?style=flat-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=flat-badge&logo=Github&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Swagger-FF6C37?style=flat-badge&logo=Swagger&logoColor=white"/>&nbsp;