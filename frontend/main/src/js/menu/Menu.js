import {scrollTo} from '../utils/Animations.utils';
import Velocity from 'velocity-animate';

export class Menu {
    constructor() {
        this.menuBtn = document.querySelector('.main-menu-item.menu-btn');
        this.menuHideBtn = document.querySelector('.hide-menu');
        this.sideMenu = document.querySelector('.side-menu');
        this.slider = document.querySelector('.container');
        this.linksBtn = document.querySelectorAll('.page-link');

        this.linksBtn.forEach(element => {
            element.addEventListener('click', (event) => {
                const selector = `.section.${event.target.getAttribute('data-name')}`;
                const elem = document.querySelector(selector);
                scrollTo(elem, 1000, 'easeOut');
            })
        });


        this.menuBtn.addEventListener('click', () => {
            Velocity(this.slider, {left: 0}, {duration: 500, easing: 'easeOut'});
        });

        this.menuHideBtn.addEventListener('click', () => {
            let width = this.sideMenu.getBoundingClientRect().width;
            Velocity(this.slider, {left: -width}, {duration: 500, easing: 'easeOut'});
        });
    }

}