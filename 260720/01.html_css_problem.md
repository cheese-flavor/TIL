### 문제풀면서 개념잡기 ###

#### 기본개념 ####
```
.body, .outer 등은 선택자를 지정하는 개념
그냥 점 없이 진행하면 태그 개념
class 명을 잘 만들어야할듯?

전체구조를 이해하는 방법
-css를 사용해서 class 구조화
방법론
1. 00CSS - 객체지향형
    .m20 이라는 클래스를 가진 모든 인스턴스들은 동일한 속성을 갖는다.
    .m20{
        margin-top: 20px;
        margin-bottom: 20px;
    }
2. BEM(block element modifier)
    block: .card-profile
    element: .card-profile > div
    modifier: .card-profile--large

-> 변수명에 따라 다르게 적용되도록
```

#### 반복개념 ####
```
#가운데 맞춤!

display: flex;  -> 디스플레이 기본값을 풀어줘야함!!!
flex-direction: column;
align-items: center;
justify-content: center;

#test-align: center ; = 작성글 가운데로
#pedding: ? ; = 여백 주기


#flex
-> display: inline 속성을 특징을 생각해서 -> text-align: center;
구조를 꼭 활용해서 
```

#### 중요개념 ####
```
상속자
.선택자 p = 자손결합자 -> 모두를 포함한(넓은범위)
.선택자 > p = 자식결합자 -> 직계 자식만 해당

자식결합자, 자손결합자 모두 명시도가 동일하기 때문에 차이를 둬야함

상속받는 속성들의 명시도는 최하위
```
