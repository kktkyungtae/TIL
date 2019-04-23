const dooly = document.querySelector('#dooly')

// console.log(typeof(dooly)) // object로 뜬다!

// 둘리를 (클릭하면), 호이라고 하게 만든다!  클릭하면 : 조건!!
// 둘리한테 이벤트(조건)을 달아준다. (이벤트, 이벤트 오면 뭐하게 만드는 것(함수))
dooly.addEventListener('click', function(){ alert('호이')})  


// document 전체에도 addEventListener 달아줄 수 있다!
// 키보드 누르면 행동하게
let x = 0
let y = 0

document.addEventListener('keydown',function(event){
    console.log(event.keyCode) // 어떤 키를 눌렀는지 알 수 있게
    // 둘리 위로 올리기
    if (event.keyCode === 38) {
        y += 30
        dooly.style.marginBottom = `${y}px` // 둘리 올리기! , 올라갔다가 안내려와..ㅋ
    } else if (event.keyCode === 40) {
        y -= 30
        dooly.style.marginBottom = `${y}px`
    } else if (event.keyCode === 37){
        x -= 30
        dooly.style.marginLeft = `${x}px`
    } else if (event.keyCode === 39){
        x += 30
        dooly.style.marginRight = `${x}px`
    }
})

