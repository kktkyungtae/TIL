var _ = require('lodash') // 모듈 호출
var numders = _.range(1,46)
var picks = _.sampleSize(numders, 6) // 단어들이 이어질때에는 뒤에 대문자로!
// console.log(`오늘의 ㅈㄸ 번호는 ${picks}`)

// 스트링 연결에 `` 얘를 사용했었다.
var name = '경태'
console.log(`제 이름은 ${name}`)
console.log(`제 이름은 ` + name)