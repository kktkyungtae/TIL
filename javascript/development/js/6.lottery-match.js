
const luckyNumbers = [5,7,32,2,36,26]
const _ = require('lodash') // 모듈 호출
// console.log(`오늘의 ㅈㄸ 번호는 ${picks}`)


function match() {
    const numders = _.range(1,46)
    const picks = _.sampleSize(numders, 6) // 단어들이 이어질때에는 뒤에 대문자로!/ 6개의 랜덤 번호
    
    //썜 코드 
    let count = 0
    for (pick of picks) {
        if (_.includes(luckyNumbers,pick)) {
            count = count + 1
        }
    }
    console.log('My numbers', pick)
    console.log('lucky numbers ', luckyNumbers)
    console.log('matches ', count)

}
match()