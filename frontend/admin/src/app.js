import './scss/app.scss'
import {SelectHandlers} from './js/SelectHandlers';
import {RemoveButtonsHandlers} from './js/RemoveButtonsHandlers';
console.log('działa');
const selectHandlers = new SelectHandlers();
const removeHandlers = new RemoveButtonsHandlers();
selectHandlers.addSelectionHandlers();
removeHandlers.addRemoveButtonHandlers();