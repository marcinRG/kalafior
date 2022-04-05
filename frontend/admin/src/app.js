import './scss/app.scss'
import {SelectHandlers} from './js/SelectHandlers';
import {RemoveButtonsHandlers} from './js/RemoveButtonsHandlers';
import {ImageFileUploader} from './js/ImageFileUploader';

console.log('działa');
const selectHandlers = new SelectHandlers();
const removeHandlers = new RemoveButtonsHandlers();
const imageUploader = new ImageFileUploader();
selectHandlers.addSelectionHandlers();
removeHandlers.addRemoveButtonHandlers();