import './scss/app.scss'
import {AddEventListenerToAllCheckboxes} from './js/AddEventListenerToAllCheckboxes';
import {SelectHandlers} from './js/SelectHandlers';
import {RemoveButtonsHandlers} from './js/RemoveButtonsHandlers';

console.log('działa');

const checkboxes = new AddEventListenerToAllCheckboxes();
const selectHandlers = new SelectHandlers();
const removeHandlers = new RemoveButtonsHandlers();
checkboxes.addEventsHandler();
selectHandlers.addSelectionHandlers();
removeHandlers.addRemoveButtonHandlers();