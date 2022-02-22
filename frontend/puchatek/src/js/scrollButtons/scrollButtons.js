import {scrollTo} from '../utils/Animations.utils';

export class ScrollButtons {
    constructor() {
        this.titleScreen = document.querySelector('.screen.title');
        this.displayScreen = document.querySelector('.screen.book-display');

        this.buttonDown = document.querySelector('.navigation.down');
        this.buttonUp = document.querySelector('.navigation.up');

        this.buttonDown.addEventListener('click', (event) => {
            event.preventDefault();
            scrollTo(this.displayScreen, 1000, 'easeOut');
        });

        this.buttonUp.addEventListener('click', (event) => {
            event.preventDefault();
            scrollTo(this.titleScreen, 1000, 'easeOut');
        });

    }
}