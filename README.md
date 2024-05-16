# Web-Client Computing Project
Django Framework를 사용한 국민대 휴게시설 안내 서비스

# 🖥️ 프로젝트 소개
국민대 내부 휴게시설 안내의 부재를 해소하고자 기획한 서비스
<br>

## ⚙️ 개발 환경
- **Front-End**: HTML, CSS, Javascript(ES6)
- **IDE** : Visual Studio Code
- **Framework** : Django 5.0.6
- **Database** : Django ORM

## 🛠사용된 기술
- **Django**: 백엔드 프레임워크
- **HTML/CSS**: 프론트엔드 마크업 및 스타일링
- **JavaScript*ES6)**: 프론트엔드 상호작용
- **Django ORM**: 데이터베이스 관리

# 📌 주요 기능
## 👤 로그인
- DB값 검증
- 로그인 유지 – Session 사용
## 🔑 회원가입 
- ID 중복 체크
- 팝업 확인 창
## 📝 게시글 작성
- 로그인 한 유저만 작성 가능
- 사진 삽입
- 팝업 확인 창
- 글 작성, 읽기
## 📃 메인 페이지 
- 건물 별 게시물 확인
- 건물명 검색 기능
- 전체 게시글 확인
- 게시글 호버 이펙트

# 🚀 설치 및 실행 방법
1. **프로젝트 클론**  
```bash  
git clone https://github.com/Alex-SH-Ahn/KMUbreakroom  
cd KMUbreakroom  
```  
2. **가상 환경 실행 및 패키지 설치**  
``` bash  
source venv/Scripts/activate # (Mac : source venv/bin/activate)  
cd breakroom  
```  
3. **마이그레이션 및 서버 실행**  
``` bash  
python manage.py migrate  
python manage.py runserver  
```  

# 📁 프로젝트 구조
KMUbreakroom <br>
├── breakroom/ <br>
│ ├── breakroom/ <br>
│ ├── media/ <br>
│ ├── static/ <br>
│ ├── posts/ <br>
│ ├── user/ <br>
│ ├── db.sqlite3 <br>
│ ├── manage.py <br>
└── venv/ <br>

## ✉ 문의
프로젝트 관련 문의 사항은 alex2321218@gmail.com이나 alexahn@kookmin.ac.kr로 연락해 주세요.
