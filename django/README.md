## Django intro

### Start Django

1. 장고 설치

   ```bash
   pip install django==2.1.15
   pip list
   ```

2.  프로젝트 생성

   ```bash
   django-admin startproject <프로젝트 명>
   ```

   ```bash
   python manage.py runserver
   ```

3. 프로젝트 생성시 제공하는 파일

   * manage.py
     * 전체 django와 관련된 모든 명령어를 manage.py를 통해 실행합니다.
   * \__init__.py
     * 현재 \__init__.py 파일이 존재하는 폴더를 하나의 프로젝트, 혹은 패키지로 인식하게 해주는 파일
   * settings.py
     * 현재 프로젝트의 전체적인 설정 및 관리를 위해 존재하는 파일.
   * urls.py
     * 내 프로젝트에 접근할 수 있는 경로를 설정하기 위한 파일





pages라는 앱을 만들고

![](C:\Users\student\Desktop\python\django\img\0.PNG)



INSTALLED_APPS 부분에 pages를 추가한다

![](C:\Users\student\Desktop\python\django\img\1.PNG)



![2](C:\Users\student\Desktop\python\django\img\2.PNG)



한글로 바뀐다.

![3](C:\Users\student\Desktop\python\django\img\3.PNG)



