import {getIndexes} from '../utils/GetIndexes';

export class MainSlider {
    constructor(settings, images) {
        this.intervalID = null;
        this.i = 0;
        this.slides = settings.slides;
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
        this.slideDescription.textContent = this.slides[this.i].long;
    }

    changeSlidesTexts() {
        const {previous, current, next} = getIndexes(this.i, this.slides.length - 1);
        this.previousText.textContent = this.slides[previous].title;
        this.currentText.textContent = this.slides[current].title;
        this.nextText.textContent = this.slides[next].title;
    }

    run() {
        this.intervalID = setInterval(() => {

            this.backgroundImage.setAttribute('xlink:href', this.images[this.i + 1].src);
            this.setAnimationClasses();
            this.currentText.addEventListener('webkitAnimationEnd', removeClass(this.currentText, 'slider-text-animation'));
            this.nextText.addEventListener('webkitAnimationEnd', removeClass(this.nextText, 'slider-text-opacity'));
            this.previousText.addEventListener('webkitAnimationEnd', removeClass(this.previousText, 'slider-text-opacity'));
            this.slideDescription.addEventListener('webkitAnimationEnd', removeClass(this.slideDescription, 'slider-text-opacity'));

            this.changeSlidesTexts();
            this.changeDescription();

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
