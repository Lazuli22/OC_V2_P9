console.log('Hello World')

// get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.form-review')
const confirmbox = document.getElementById('confirm_box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log(confirmbox)
console.log(csrf)

const handleSelect = (selection) => {
    switch (selection) {
        case 'first':
            {
                one.classList.add('checked')
                two.classList.remove('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
        case 'second':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.remove('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
        case 'third':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.remove('checked')
                five.classList.remove('checked')
                return
            }
        case 'fourth':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.remove('checked')
                return
            }
        case 'fifth':
            {
                one.classList.add('checked')
                two.classList.add('checked')
                three.classList.add('checked')
                four.classList.add('checked')
                five.classList.add('checked')
            }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } else if (stringValue === 'second') {
        numericValue = 2
    } else if (stringValue === 'third') {
        numericValue = 3
    } else if (stringValue === 'fourth') {
        numericValue = 4
    } else if (stringValue === 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
}

const arr = [one, two, three, four, five]

arr.forEach(item => item.addEventListener('mouseover', (event) => {
    handleSelect(event.target.id)
}))

arr.forEach(item => item.addEventListener('click', (event) => {
    const val = getNumericValue(event.target.id)
    document.getElementById('confirm_box').innerHTML = `<input id="rating" name="rating" type="hidden" value="${val}">`
}))