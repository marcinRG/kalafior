import './scss/app.scss'
import {ButtonValues, PopUpWindow} from './js/PopUpWindow';
// import {AddEventListenerToAllCheckboxes} from './js/AddEventListenerToAllCheckboxes';
// import {SelectHandlers} from './js/SelectHandlers';

console.log('działa');

export function printSomething(buttonValue) {
    console.log('button value:');
    console.log(buttonValue);
}
const popUp = new PopUpWindow();

const btn = document.querySelector('.custom-btn');
btn.addEventListener('click', () => {
    popUp.showPopUpWindow('Uwaga! To jest okienko', 'To jest jakaś customowa wiadomość', [
        {
            title: 'Ok',
            type: ButtonValues.OK
        },
        {
            title: 'Anuluj',
            type: ButtonValues.CANCEL
        }], printSomething);
});


// const checkboxes = new AddEventListenerToAllCheckboxes();
// const selectHandlers = new SelectHandlers();
// checkboxes.addEventsHandler();
// selectHandlers.addSelectionHandlers();