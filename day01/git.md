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
  1. git init = 깃으로 해당 경로의 폴더를 관리대상으로 선정(MASTER)
  
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
```

