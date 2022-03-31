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
        const options = this.mainSelector.querySelectorAll('option');
        const option = Array.from(options).filter(div => div.hasAttribute('selected'))[0];
        if (option) {
            showSelectedDiv(this.selectsDiv, option.value);
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