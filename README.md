<div align="center">

</div>

## 목차
- [개발 기간](#--개발-기간--)  
- [프로젝트 설명 분석](#-프로젝트)
- [개발 조건](#-개발-조건)
- [API 명세서](#API-명세서)
- [기술 스택](#기술-스택) 

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
      - 게시글 작성 시에는 비밀번호를 입력받고, 수정/삭제시 입력한 비밀번호가 맞는 경우만 가능합니다.
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
      - DB 스키마 생성 스크립트(python create_db.py 명령 실행)
      - 게시글 목록 API
      - 게시글 작성 API
      - 게시글 수정 API
      - 게시글 삭제 API 
      - 댓글 목록 API
      - 댓글 작성 API
      - 게시물 또는 댓글 등록시 알림 기능 구현

  ### 🚥 개발 조건 

  #### 🙆‍♂️ 필수사항  
    - Python, Flask, MySQL 5.7
    - REST API 구현
    - DB 스키마 스크립트
    - DB를 이용한 키워드 알림 기능

📌 Dependency
```
1. 의존성 설치
pip install -r requirements.txt

2. DB 스키마 생성
python create_db.py

3. 앱 실행
export FLASK_APP=app.py
flask run

or

set FLASK_APP=app.py 
flask run
```

<br>


## API 명세서

| ID  | URI                                   | METHOD | 기능           |
|-----|---------------------------------------|--------|--------------|
| 1   | /api/posts                            | POST   | 게시글 생성       |
| 2   | /api/posts                            | GET    | 게시글 리스트 조회   |
| 3   | /api/posts/<int:postid>               | GET    | 게시글 단건 조회    |
| 4   | /api/posts/<int:postid>               | PUT    | 게시글 수정       |
| 5   | /api/posts/<int:postid>               | DELETE | 게시글 삭제       |
| 6   | /api/posts/<int:postid>/comments      | POST   | 게시글 댓글 생성    |
| 7   | /api/posts/<int:postid>/comments      | GET    | 게시글 댓글 목록 조회 |
| 8   | /api/keywords                         | POST   | 알림 키워드 등록    |
| 9   | /api/keywords                         | GET    | 알림 키워드 조회    |
| 10  | /api/search?q='검색할 단어'                | GET    | 알림 키워드 조회    |

<br><br>
  <summary>1. 게시글 생성</summary>
  
  ```
  [POST]
  api/posts
  ```
  - Request
  ```
201 CREATED

{
	"username": "test2",
	"title": "This is another row?",
	"content": "I am seeing lion.",
	"password": "1234"
}
  ```
  - Response
  ```
200 OK

{
	"username": "test2",
	"title": "This is another row?",
	"content": "I am seeing lion.",
}

  ```
- 키워드 알림 기능: 게시글 제목이나, 내용 중 키워드 알림 등록된 단어가 들어간 경우
- 의미: "test1": 6
  '알림 보낼 사용자': '알림 대상인 게시글 고유 번호'
```
201 CREATED

{
	"alarm": [
		{
			"test1": 6
		}
	],
	"content": "I am seeing lion.",
	"title": "This is another row?",
	"username": "test2"
}
```
<br><br>

  <summary>2. 게시글 전체 목록 조회</summary>
  
  ```
  [POST]
  /api/posts
  ```

  - Response
  ```
200 OK

{
	"pagination": {
		"page": 1,
		"per_page": 5
	},
	"results": [
		{
			"content": "Everyday, I wake up early, test",
			"created_at": "Sun, 14 Aug 2022 22:27:09 GMT",
			"id": 1,
			"title": "When do you wake up?",
			"updated_at": "Sun, 14 Aug 2022 22:27:09 GMT",
			"username": "test12"
		},
		{
			"content": "Yes, it is created now.",
			"created_at": "Sun, 14 Aug 2022 22:32:27 GMT",
			"id": 2,
			"title": "This is second row?",
			"updated_at": "Sun, 14 Aug 2022 22:32:27 GMT",
			"username": "test13"
		},
		{
			"content": "Yes, it is created now.",
			"created_at": "Sun, 14 Aug 2022 22:42:07 GMT",
			"id": 3,
			"title": "This is second row?",
			"updated_at": "Sun, 14 Aug 2022 22:42:07 GMT",
			"username": "test13"
		},
		{
			"content": "Yes, it is created now.",
			"created_at": "Sun, 14 Aug 2022 23:02:43 GMT",
			"id": 4,
			"title": "This is second row?",
			"updated_at": "Sun, 14 Aug 2022 23:02:43 GMT",
			"username": "test22"
		}
	]
}

  ```
<br><br>
  <summary>3. 게시글 단건 조회</summary>
  
  ```
  [GET]
  /api/posts/<int: postid>
  ```
  - Response
  ```
200 OK


{
	"content": "Everyday, I wake up early, test",
	"created_at": "Sun, 14 Aug 2022 22:27:09 GMT",
	"id": 1,
	"title": "When do you wake up?",
	"updated_at": "Sun, 14 Aug 2022 22:27:09 GMT",
	"username": "test12"
}
  ```
<br><br>
<summary>4. 게시글 단건 수정</summary>

  ```
  [PUT]
  /api/posts/<int: postid> 
  ```
  - Request
```
{
	"username": "test2",
	"title": "This api test. testing...",
	"password":"1234"
}
  ```
  - Response
```
200 OK

{
	"title": "This api test. testing...",
	"updated_at": "Sun, 14 Aug 2022 23:11:40 GMT",
	"username": "test2"
}
  ```
<br><br>
  <summary>5. 게시글 단건 삭제</summary>
  
  ```
  [DELETE]
  /api/posts/<int: postid>
  ```
  - Request
  ```
{
	"password": "1234"
}
  ```
  - Response
  ```
204 No Content
{
}
  ```
<br><br>
  <summary>6. 댓글 작성</summary>
  
  ```
  [POST]
  /api/posts/<int: postid/comments
  ```
  - Request
  ```
{
	"username": "test3", 
	"content": "I am want more reply, this is test comment!"
}
  ```
  - Response
  ```
201 CREATED


{
	"content": "I am want more reply, this is test comment!",
	"created_at": "Sun, 14 Aug 2022 23:16:54 GMT",
	"id": 1,
	"parent_id": null,
	"postid": 2,
	"username": "test3"
}
  ```
- 키워드 알림 기능: 댓글 내용 중 키워드 알림 등록된 단어가 들어간 경우
- - 의미: "test2": 5
  '알림 보낼 사용자': '알림 대상인 댓글 고유 번호'
```
{
	"alarm": [
		{
			"test2": 5
		}
	],
	"content": "I am want more reply, this is test comment!",
	"id": null,
	"parent_id": null,
	"username": "test3"
}
```
<br><br>
  <summary>7. 댓글 조회</summary>
  
  ```
  [GET]
  /api/posts/<int: postid>/comments
  ```
  - Response

  ```
200 OK

{
	"pagination": {
		"page": 1,
		"per_page": 5
	},
	"results": [
		{
			"content": "I am want more reply, this is test comment!",
			"created_at": "Sun, 14 Aug 2022 23:16:54 GMT",
			"id": 1,
			"parent_id": null,
			"postid": 2,
			"username": "test3"
		},
		{
			"content": "this is another test comment",
			"created_at": "Sun, 14 Aug 2022 23:19:22 GMT",
			"id": 2,
			"parent_id": null,
			"postid": 2,
			"username": "test4"
		}
	]
}

  ```
<br><br>
  <summary>8. 키워드 알림 등록</summary>
  
  ```
  [POST]
  /api/keywords
{
	"username": "test1",
	"word": "lion,tiger"
}
  ```
  - Response
  ```
201 CREATED

{
	"username": "test1",
	"word": "lion,tiger"
}
  ```
<br><br>
  <summary>9. 키워드 알림 목록 조회</summary>
  
  ```
  [GET]
  /api/keywords
  ```
  - Response
  ```
201 CREATED

{
	"username": "test1",
	"word": "lion,tiger"
}
  ```
<br><br>
  <summary>10. 게시글 검색</summary>
  
  ```
  [GET]
  127.0.0.1:5000/api/search?q=test
  (게시글 검색은 '작성자', 게시글 제목으로 검색 가능합니다.)
  ```
  - Response
  ```
200 OK

[
	{
		"content": "Everyday, I wake up early, test",
		"created_at": "Sun, 14 Aug 2022 22:27:09 GMT",
		"id": 1,
		"title": "When do you wake up?",
		"updated_at": "Sun, 14 Aug 2022 22:27:09 GMT",
		"username": "test12"
	},
	{
		"content": "Yes, it is created now.",
		"created_at": "Sun, 14 Aug 2022 22:32:27 GMT",
		"id": 2,
		"title": "This is second row?",
		"updated_at": "Sun, 14 Aug 2022 22:32:27 GMT",
		"username": "test13"
	},
  ```
<br><br>

## 기술 스택

> - Back-End :  <img src="https://img.shields.io/badge/Python 3.10-3776AB?style=flat&logo=Python&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/flask-009688?style=flat&logo=flask&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/MySQL 8.0-4479A1.svg?style=flat&logo=mysql&logoColor=white"/>
>
> - ETC　　　:  <img src="https://img.shields.io/badge/Git-F05032?style=flat-badge&logo=Git&logoColor=white"/>&nbsp;<img src="https://img.shields.io/badge/Github-181717?style=flat-badge&logo=Github&logoColor=white"/>&nbsp;