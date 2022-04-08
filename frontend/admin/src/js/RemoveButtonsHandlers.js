import {ButtonValues, PopUpWindow} from './PopUpWindow';

export class RemoveButtonsHandlers {
    constructor() {
        this.popUpWindow = new PopUpWindow();
        this.buttons = document.querySelectorAll('[data-btn-type="remove-btn"]');
    }

    addRemoveButtonHandlers() {
        for (const btn of this.buttons) {
            const id = btn.getAttribute('data-id');
            const func = createRemoveData(btn);
            btn.addEventListener('click', () => {
                this.popUpWindow.showPopUpWindow('Uwaga! Usuwanie elementu', 'Czy chcesz usunąć element: ' + id + ' z bazy danych?', [
                    {
                        title: 'Usuń',
                        type: ButtonValues.REMOVE
                    },
                    {
                        title: 'Anuluj',
                        type: ButtonValues.CANCEL
                    }], func);
            });
        }
    }
}

export function createRemoveData(button) {
    const id = button.getAttribute('data-id');
    const action = button.getAttribute('data-btn-action');
    const adr = window.location.pathname;

    const func = (buttonType) => {
        if (buttonType === ButtonValues.REMOVE) {
            window.location.replace(`${adr}?mode=${action}&id_elem=${id}`);

        }
    }
    return func;
}