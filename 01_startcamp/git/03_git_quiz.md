```
quiz/
	.git/
	a.txt
	my_folder/
	
project/
	.git/
	a.py
	b.py

내 폴더/
	마케팅/
	..
```

* quiz 폴더 이름을 변경해도 되는가? O
* quiz 폴더 이름 변경에 대한 기록이 남는가? X
* quiz 폴더 위치를 변경해도 되는가? △
  * project에는 이동 X 
    * .git 관리되는 리포지토리가 하나의 폴더(project)에서 두개가 존재하게 됨.
  * 내 폴더는 이동 O 언제든지!
* my_folder는 지우면 복원 가능한가? △
  * 커밋된 변경사항은 무조건 복원 가능!
  * 커밋되지 않은 경우는 절대 불가능!
* 만약에 .git 폴더가 있는 저장소 내부에서 새롭게 .git을 만들어도 되나요? X
  * 하지말자!
  * `git init` 명령어를 입력하려고 하는데 `(master)` 가 있다? 다시 생각해보기!

* fetch vs pull?
  * fetch : 받아오기만 해요
  * pull : fetch + merge (병합)















