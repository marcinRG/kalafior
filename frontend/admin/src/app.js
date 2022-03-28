import './scss/app.scss'
import {AddEventListenerToAllCheckboxes} from './js/AddEventListenerToAllCheckboxes';
import {SelectHandlers} from './js/SelectHandlers';

console.log('działa');

const checkboxes = new AddEventListenerToAllCheckboxes();
const selectHandlers = new SelectHandlers();
checkboxes.addEventsHandler();
selectHandlers.addSelectionHandlers();