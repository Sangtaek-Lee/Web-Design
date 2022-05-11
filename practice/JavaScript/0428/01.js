const number = document.querySelector('#number')
const plusBtn = document.querySelector('#plusBtn')
const minusBtn = document.querySelector('#minusBtn')


function plusminus(bloonleanVal) {
  number.innerContent += 1
  if (bloonleanVal) {
    number.innerContent += 1
  }
}



minusBtn.addEventListener('click', plusminus(1))

EventTarget.addEventListener('click', function(){
  
})