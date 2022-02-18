import './scss/app.scss';

const charactersSetsLength = {
    bigLetter: 24,
    smallLetter: 24,
    digits: 10,
    special: 5,
    brackets: 8,
    other: 10
}

const selectedCharacterSets = {};

function checkBoxClick(checkbox, obj, objPropertyAsString) {
    if (checkbox.value === 'true') {
        if (obj && obj.hasOwnProperty(objPropertyAsString)) {
            delete obj[objPropertyAsString];
        }
        checkbox.value = 'false';
    } else {
        obj[objPropertyAsString] = true;
        checkbox.value = 'true';
    }
    console.log(obj);
}

const bigLettersCheckBox = document.getElementById('bigLetters');

bigLettersCheckBox.addEventListener('change', (event) => {
    checkBoxClick(event.target, selectedCharacterSets, 'bigLetters');
});

const smallLettersCheckBox = document.getElementById('smallLetters');
smallLettersCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'smallLetters'));
const digitsCheckBox = document.getElementById('digits');
digitsCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'digits'));
const commasMathCheckBox = document.getElementById('commasMath');
commasMathCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'digits'));
const specialCheckBox = document.getElementById('special');
specialCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'special'));
const bracketsCheckBox = document.getElementById('brackets');
bracketsCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'brackets'));
const otherCheckBox = document.getElementById('other');
otherCheckBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'brackets'));
const uniqueChBox = document.getElementById('uniqe');
uniqueChBox.addEventListener('change',
    (event) => checkBoxClick(event.target, selectedCharacterSets, 'unique'));

const lengthInput = document.querySelector('.form-input.size');
lengthInput.addEventListener('input', (event) => {
    console.log(event.target.value);
});

const createPasswordBtn = document.querySelector('.form-btn.password');
const copyToClipboardBtn = document.querySelector('.form-btn.copy-to-clipboard');


const form = document.querySelector('.generator-form');
form.addEventListener('submit',(event)=>{
    console.log('submit');
    event.preventDefault();
})


console.log(bigLettersCheckBox);
console.log(smallLettersCheckBox);


console.log('działa');
