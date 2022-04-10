import Velocity from 'velocity-animate';
import {scrollTo} from '../utils/Animations.utils';

export class UpArrows {
    constructor() {
        this.arrows = document.querySelectorAll('span.up');
        this.topComponent = document.querySelectorAll('.main-slider');
        if (this.arrows && this.arrows.length > 0) {
            for (const arrow of this.arrows) {
                arrow.addEventListener('click', () => {
                    if (this.topComponent) {
                        scrollTo(this.topComponent, 500, 'easeOut');
                    }
                });
            }
        }
    }
}