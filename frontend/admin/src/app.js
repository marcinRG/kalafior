import './scss/app.scss'
import {SelectHandlers} from './js/SelectHandlers';
import {RemoveButtonsHandlers} from './js/RemoveButtonsHandlers';
import {ImageFileUploader} from './js/ImageFileUploader';
import {MainMenu} from './js/MainMenu';

console.log('działa');
const selectHandlers = new SelectHandlers();
const removeHandlers = new RemoveButtonsHandlers();
const imageUploader = new ImageFileUploader();
const mainMenu = new MainMenu();
selectHandlers.addSelectionHandlers();
removeHandlers.addRemoveButtonHandlers();