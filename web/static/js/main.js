'use strict'

const btn = document.querySelector('.button')
const test = document.querySelector('.test')
test.classList.add('opacity-0')
test.classList.add('translate-y-1')


btn.addEventListener('click', (e) => {
  if (test.classList.contains('opacity-0')) {
    test.classList.remove('opacity-0')
    test.classList.remove('translate-y-1')
    test.classList.add('opacity-100')
    test.classList.add('translate-y-0')
  }
  else {
    test.classList.add('opacity-0')
    test.classList.add('translate-y-1')
    test.classList.remove('opacity-100')
    test.classList.remove('translate-y-0')
  }
})