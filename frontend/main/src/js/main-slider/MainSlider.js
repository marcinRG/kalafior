import {getIndexes} from '../utils/GetIndexes';
import {scrollTo} from '../utils/Animations.utils';

export class MainSlider {
    constructor(slides, images) {
        this.intervalID = null;
        this.i = 0;
        this.slides = slides;
        this.delay = 15000;
        this.images = images;
        this.previousText = document.querySelector('.left  .slider-text');
        this.currentText = document.querySelector('.center .slider-text');
        this.nextText = document.querySelector('.right .slider-text');
        this.slideDescription = document.querySelector('.center .description-text');
        this.backgroundImage = document.querySelector('.bgd-image');
    }

    setAnimationClasses() {
        this.previousText.classList.add('slider-text-opacity');
        this.currentText.classList.add('slider-text-animation');
        this.nextText.classList.add('slider-text-opacity');
        this.slideDescription.classList.add('slider-text-opacity');
    }

    changeDescription() {

        const currentElem = this.slides[this.i];
        this.slideDescription.innerHTML = '';
        let text = document.createElement('span');
        text.classList.add('text-dsc');
        text.textContent = currentElem.description;
        this.slideDescription.appendChild(text);

        if (currentElem.show_on_menu) {
            let link = document.createElement('span');
            link.classList.add('link-dsc');
            link.textContent = 'zobacz więcej';
            this.slideDescription.appendChild(link);

            link.addEventListener('click', () => {
                const selector = `.section.${currentElem.id}`;
                const elem = document.querySelector(selector);
                scrollTo(elem, 1000, 'easeOut');
            });
        }
    }

    changeSlidesTexts() {
        const {previous, current, next} = getIndexes(this.i, this.slides.length - 1);
        this.previousText.textContent = this.slides[previous].long_name;
        this.currentText.textContent = this.slides[current].long_name;
        this.nextText.textContent = this.slides[next].long_name;
    }

    run() {
        this.intervalID = setInterval(() => {

            this.backgroundImage.setAttribute('xlink:href', this.images[this.i + 1].src);
            this.setAnimationClasses();
            this.currentText.addEventListener('webkitAnimationEnd', removeClass(this.currentText, 'slider-text-animation'));
            this.nextText.addEventListener('webkitAnimationEnd', removeClass(this.nextText, 'slider-text-opacity'));
            this.previousText.addEventListener('webkitAnimationEnd', removeClass(this.previousText, 'slider-text-opacity'));
            this.slideDescription.addEventListener('webkitAnimationEnd', removeClass(this.slideDescription, 'slider-text-opacity'));

            this.changeDescription();
            this.changeSlidesTexts();

            this.i = this.i + 1;
            if (this.i >= this.slides.length) {
                this.i = 0;
            }
        }, this.delay);
    }
}

function removeClass(elem, className) {
    const functionToReturn = () => {
        elem.classList.remove(className);
        elem.removeEventListener('webkitAnimationEnd', functionToReturn, true);
    }
    return functionToReturn;
}
