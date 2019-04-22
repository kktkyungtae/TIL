    // 는 한줄 주석이다
    
    /*
        여기 는 여러줄을 주석처리한다!
    */

   alert("야!") // 경고창을 날려주는 것!

   // 실제로 프린팅하는 놈들
   console.log("임마!") // 콘솔에다가 로그 찍을래! 콘솔에 찍혀 있다리
   document.write("너!") // html 조작하는! document. 라고 시작하면 엄청 시리 많다.
   document.write("<h1>너</h1>") // 글씨 크기도 조작가능!

   document.querySelector('h1') 
   // 문서안에서 특정한 놈을 찾아서 변경한다! 자주 쓰는 놈임 querySelector(태크이름 또는 샐렉터)
   console.log(document.querySelector('h1')) // 쿼리 셀렉터를 쓰면, <h1>너</h1> 요래 나온다.
   console.log(document.querySelector('h1').innerText) // 너! 만 나온다
   document.querySelector('h1').innerText = "동준아!" // 원래 있던 데이터를 실행하면서 바꾼다.

   // alert 랑 비슷한놈
   user_name = prompt("이름이 뭐냐")
   user_age = prompt("나이를 입력해줘") // 띄워 주는 놈! 파이썬에서 input이랑 똑같이 쓴다
   // console.log(user_input) // 요렇게도 가능!

   if (user_age > 30) { // : 대신에 자바스크립트에서는 {} 요놈을 쓴다.
       age = '아재네'
   } else if (user_age > 20) {
       age ='학식이고'
   } else {
       age = '급식이다잉'
   }

   // if (user_input > 30) { // : 대신에 자바스크립트에서는 {} 요놈을 쓴다. 함수에 넣고 쓸 수도 있다.
   //     age = '아재네'
   // } else if (user_input > 20) {
   //     age ='학식이고'
   // } else {
   //     age = '급식이다잉'
   // }
   
   document.querySelector('h1').innerText = user_name +"는"+ age // 조건에 맞춘 것을 출력해준다.
   document.querySelector('h1').innerText = `${user_name}은(는) ${age}`

   // 반복문
   user_input2 = prompt("숫자 입력해줘")
   
   for (i = 0; i < user_input2; i++) {
       document.write(`<p>${i}</p>`)
   }
   


   // 언어가 스트링을 어떻게 조작하느냐가 중요함