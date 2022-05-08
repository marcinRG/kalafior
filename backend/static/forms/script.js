const massRadio = document.querySelector('input[type="radio"][value="mass"]');
const lengthRadio = document.querySelector('input[type="radio"][value="length"]');

const lengthDiv = document.querySelector('div.length');
const massDiv = document.querySelector('div.mass');

if (massRadio && lengthRadio && lengthDiv && massDiv) {

    massRadio.addEventListener('click', () => {
        lengthDiv.classList.add('d-none');
        massDiv.classList.remove('d-none');
    });

    lengthRadio.addEventListener('click', () => {
        massDiv.classList.add('d-none');
        lengthDiv.classList.remove('d-none');
    });

    if (lengthRadio.checked) {
        massDiv.classList.add('d-none');
        lengthDiv.classList.remove('d-none');

    } else {
        lengthDiv.classList.add('d-none');
        massDiv.classList.remove('d-none');
    }
}
