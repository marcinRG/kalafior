import './scss/app.scss';

const serverPath = '/pass_generator/data';

const charactersSetsLength = {
    big: 25,
    small: 25,
    numbers: 10,
    brackets: 8,
    commas: 4,
    other: 14
};

const lengthBounds = {
    min: 5,
    max: 40
};

function checkBoxClick(checkbox, objProperties, objPropertyAsString) {
    if (checkbox.checked) {
        objProperties[objPropertyAsString] = true;
        objProperties['stringLength'] = objProperties['stringLength'] + charactersSetsLength[objPropertyAsString];
    } else {
        if (objProperties && objProperties.hasOwnProperty(objPropertyAsString)) {
            objProperties['stringLength'] = objProperties['stringLength'] - charactersSetsLength[objPropertyAsString];
            delete objProperties[objPropertyAsString];
        }
    }
}


class PasswordGenerator {
    constructor() {
        this.selected = {
            stringLength: 0,
            passwordLength: 10,
        };
        this.form = document.querySelector('.generator-form');
        //buttons
        this.generatePasswordBtn = document.querySelector('.form-btn.password');
        this.copyToClipboardBtn = document.querySelector('.form-btn.copy-to-clipboard');
        //input fields
        this.lengthInput = document.querySelector('.form-input.size');
        this.passwordInput = document.querySelector('.form-input.password');
        //error messages
        this.lengthError = document.querySelector('.form-input.error.length');
        this.noDataSetError = document.querySelector('.form-input.no-dataset');
        this.uniqueError = document.querySelector('.form-input.unique');
        //server results
        this.divOk = document.querySelector('.div.password.ok');
        this.divError = document.querySelector('.div.password.error');
        //checkboxes
        this.checkBoxes = document.querySelectorAll('input[type="checkbox"].strings');
        this.checkBoxUnique = document.querySelector('input[type="checkbox"].unique');
        //adding event listeners
        this.addEventListeners();
        this.addCheckBoxesEventListeners();
        //setting initial values
        this.setInitialValues();
        this.hideResults();
    }

    addCheckBoxesEventListeners() {
        const selected = this.selected;
        const self = this;
        this.checkBoxes.forEach((checkBox) => {
            checkBox.addEventListener('change', (event) => {
                const name = checkBox.getAttribute('id');
                checkBoxClick(event.target, selected, name);
                const check = self.selected.stringLength > 0;
                self.checkIfValid(check, self.noDataSetError);
                self.checkIfUnique();
                self.hideResults();
            });
        });
    }

    setInitialValues() {
        this.checkBoxes.forEach((checkBox) => {
            checkBox.checked = false;
        });
        this.checkBoxUnique.checked = false;
        this.checkBoxes[0].click();
        this.lengthInput.value = this.selected.passwordLength;
    }

    checkIfValid(check, error) {
        if (check) {
            this.generatePasswordBtn.removeAttribute('disabled');
            error.classList.add('hide');
        } else {
            this.generatePasswordBtn.setAttribute('disabled', 'true');
            error.classList.remove('hide');
        }
    }

    hideResults() {
        this.divError.classList.add('hide');
        this.divOk.classList.add('hide');
    }

    checkIfUnique() {
        if (this.checkBoxUnique.checked) {
            this.selected[this.checkBoxUnique.getAttribute('id')] = true;
            const check = (this.selected.stringLength >= this.selected.passwordLength) && this.selected.passwordLength > 0;
            this.checkIfValid(check, this.uniqueError);
        } else {
            delete this.selected[this.checkBoxUnique.getAttribute('id')];
        }
    }

    addEventListeners() {
        this.form.addEventListener('submit', (event) => {
            event.preventDefault();
        })

        this.generatePasswordBtn.addEventListener('click', () => {
            fetch(serverPath, {
                method: 'POST',
                headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
                body: JSON.stringify(this.selected)
            }).then(response => response.json()).then(data => {
                if (data && data.password) {
                    this.divError.classList.add('hide');
                    this.divOk.classList.remove('hide');
                    this.passwordInput.value = data.password;
                }
                if (data && data.error) {
                    this.divError.classList.remove('hide');
                    this.divOk.classList.add('hide');
                    this.divError.textContent = 'Błąd!' + data.error
                }

            }).catch((err) => {
                this.divError.classList.remove('hide');
                this.divOk.classList.add('hide');
                this.divError.textContent = 'Błąd!' + err.message
            });
        });

        this.lengthInput.addEventListener('input', (event) => {
            const value = Number.parseFloat(event.target.value);
            let valueOk = (Number.isInteger(value) && (value >= lengthBounds.min && value <= lengthBounds.max));
            this.checkIfValid(valueOk, this.lengthError);
            if (valueOk) {
                this.selected.passwordLength = Number.parseInt(event.target.value);
            } else {
                this.selected.passwordLength = 0;
            }
            this.checkIfUnique();
            this.hideResults();
        });

        this.checkBoxUnique.addEventListener('change', () => {
            this.checkIfUnique();
            this.hideResults();
        });

        this.copyToClipboardBtn.addEventListener('click', () => {
            if (this.passwordInput.value) {
                navigator.clipboard.writeText(this.passwordInput.value).catch(() => {
                    console.log('błąd kopiowania do schowka');
                });

            }
        });
    }

}

new PasswordGenerator();
