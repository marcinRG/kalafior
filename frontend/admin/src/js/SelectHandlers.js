export class SelectHandlers {
    constructor() {
        this.mainSelector = document.querySelector('div.selections div[data-type="fill_selection"] select');
        if (this.mainSelector) {
            this.selectsDiv = Array.from(document.querySelectorAll('div.selections div'))
                .filter((div) => {
                    return div.getAttribute('data-type') !== 'fill_selection'
                });
            this.hideAllSelects();
            this.initialize();
        }


    }

    initialize() {
        const currentValue = Array.from(this.mainSelector.querySelectorAll('option')).filter(div => div.hasAttribute('selected'))[0].value;
        if (currentValue) {
            showSelectedDiv(this.selectsDiv, currentValue);
        }
    }

    hideAllSelects() {
        this.selectsDiv.forEach(elem => elem.classList.add('hide'));
    }

    addSelectionHandlers() {
        if (this.mainSelector) {
            this.mainSelector.addEventListener('change', (event) => {
                this.hideAllSelects();
                showSelectedDiv(this.selectsDiv, event.target.value);
            });
        }
    }
}

function showSelectedDiv(divArray, divValue) {
    const selected = divArray.filter(div => div.getAttribute('data-type') === divValue)[0];
    if (selected) {
        selected.classList.remove('hide');
    }
}