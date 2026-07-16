# 마크다운

> 문서를 체계적으로 관리할수있도록 하는 문법
- 순서가 없는 리스트
  1. 순서가 있는 리스트

[링크] (http://naver.com)

### 코드 복사는 백틱으로 진행
``` python
#백틱으로 감싸진 영역은 code block 영역이 되어서 
print('hellow') # 이렇게 그 언어의 문법에 맞춰 하이라이팅 된다
```


# CLI
### 명령어를 통해 코드 진행(리눅스 기반에 적합)
### 무조건알기
```
  1. .  = 현재 디렉토리를 나타내는(상대경로)
  2. .. = 상위 디렉토리를 나타내는(부모폴더)
```

### 기초문법 함수
```
  1. touch = 파일을 만드는 코드
  2. mkdir = 폴더 만들기  #make directory
  3. mv = 파일 옮기기 (mv what where 형태) #move
  4. cd = 폴더로 이동하기 (내가 작업하고자 하는 공간으로) #chage directory
  5. ls = 현재 폴더의 파일 리스트 불러오기 #list
  6. code = 원하는 파일을 열때 (code 뒤에 그냥 파일주소) #tab으로 내부 폴더명 찾기
```



# GIT
### 분산버전 관리 시스템
#### 버전관리: 변화를 기록하고 추적
```
GIT 3가지 영역 (W->S->R)
  1. WORKING DIRECTORY: 실제 수정하는 파일들의 공간
  2. STAGING AREA: 다음버전에 추가할 내용을 모아놓은 공간(완료되면 비어짐)
  3. REPOSITOY: V1로 수정완료된 파일의 공간
```

```
GIT의 동작
  1. git init = 깃으로 해당 경로의 폴더를 관리대상으로 선정(MASTER) #자주 까먹음
  
  2. git status = 상태확인(매 작업마다 해당 작업 확인하기)
  
  3. git add 파일명 위치  = staging area 파일을 옮기는것 // 한번에도 다 가능
  
  4. git commit  = 버전을 남긴다(무엇을 어떻게 수정했는지에 대한 설명)
    - git config --global user.email "you@example.com"
    - git config --global user.name "Your Name"
    - ## code ~/.gitconfig   = 저장된 이름 또는 메일 수정시
    - 수정시 insert -> 버전내용 기입
    - 끝나면 esc로 나가고 저장정보 남길때 :wq

  5. git log #최종적으로 버전 확인할때 로그 파일을 열기
    - git log --oneline = 한줄로 만들기
    - git log --oneline --graph = 노드 형태로 만들어지는

  6. git commit(실행) -m(message)

  7. git restore 파일명 = 이전버전으로 돌아가는
```

#### 연습할것: git add commit 형태를 매번 눌러서 작업내용 -m으로 수정하기
#### (무엇을 어떻게 수정했는지에 대한 설명)

#### 서브 모듈
```
전체를 총괄하는 메인과 각각의 git을 관리하는 서브 모듈로 진행하다보면 부모가 2개 될 수 있음
```

## GIT - HUB ##
```
아예 비어있는 깃 상태를 원하면 체크 없이 진행

  1. fetch: 내려받기 / pull: 변동사항 확인
  2. push: 

  - git remote add origin https://github.com/cheese-flavor/TIL.git
  - git remote -v = 현재 있는 별명 및 주소들 관리
  - origin 사이트명
  - git branch -M master  #마스터가 저장위치가 아니면 이걸로 바꾸기
  
  - git push origin master  # 업로더를 지정하는거 // 작성자랑 별개 
    // 집에 가기전에 push
```

## 큰 사이클 ##
```
1. git init : 최초 시작만
2. git add : 수정사항이 생길때마다 포함해서 계속 add 형식으로 진행
3. git status : 확인
4. git commit -m "내용"
5. git push origin master  # 주소, 내 명칭 
   - git push -u origin master # -> 이걸 쓰면 그냥 git push만 진행해도 됨

```

## 남의작업을 활용할 때 ##
```
남의 원격 주소를 복사한 후
git clone 주소
-> push는 상대방 주소를 기반으로 진행

pull로 땡겼을때 로컬파일과 겹치게 되면 문제
-> vs 기반에서는 current change나 accept incoming change를 쓰면 된다
```


## GIT BRANCH ##
```
나뭇가지처럼 여러 갈래로 "작업공간"을 나누어 독립적으로 작업을 도와주는 도구
  - 독립이기에 원본(MASTER)안전
  - 하나의 작업은 하나의 브랜치로 나누어 진행 -> 협업 개발 가능
  - 손쉽게 생성, 브랜치 사이 이동 가능
```

```
1. git branch = 목록을 확인가능
  -git branch -r = 외부 공간에 연결되어이는지
2. git switch (다른 특성) = 다른 공간으로 이동하는거(head를 이동하는것)
3. switch로 넘어가기전에 add commit 꼭 진행하기!!!! // untracked 상태에서는 작업 기록 저장이 안됨

4. git branch (생성명) -> head가 가리키는 시점에 동일하게 구조를 다 가져오는

5. git merge = head 지점에서 병합할 내용을 가져오는 형태 (fastforward - 빨리감기)
  - master에서도 추가작업을 진행했다면 합치고 나서 :wq 누르고 나오기 (세 갈래길)

* fork는 단지 별개의 프로젝트 느낌 / 편의성 down
* CONFLICT merging -> 겹치게 되면 브랜치 쪽에 문의하기
* master에서는 기본 명세서, readme, 세팅
* dev 공간은 추가발전 단계 -> 해당 단계가 완료되고 master랑 같이 최신화 / 실작업이 dev에서 진행

6. 작업이 완료된 후에 branch를 삭제
  git branch -d 브랜치명
```