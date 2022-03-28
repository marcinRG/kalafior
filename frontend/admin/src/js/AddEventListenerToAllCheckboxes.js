export class AddEventListenerToAllCheckboxes {
    constructor() {
        this.checkBoxes = document.querySelectorAll('input[type="checkbox"].form-checkbox');
    }

    addEventsHandler() {
        for (const checkBox of this.checkBoxes) {
            checkBox.addEventListener('change', (event) => {
                if (event.target.value === 'True') {
                    event.target.value = 'False'
                } else {
                    event.target.value = 'True'
                }
            })
        }
    }
}