var _ = require('lodash') // 모듈 호충
var menus = ['짜장면', '짬뽕','볶음밥'] // 배열 선언
var pick = _.sample(menus)
var object = {
    '짜장면' : 'image1',
    '짬뽕' : 'image2',
    '볶음밥' : 'image3',
}

console.log(object['짜장면']) // 키값을 넣어서 출력
console.log(object[pick]) // 얘도 가능