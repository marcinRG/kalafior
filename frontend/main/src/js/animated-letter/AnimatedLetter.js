export class AnimatedLetter {
    constructor() {
        this.j = 0;
        this.text = 'Kalafior'.toUpperCase().split('');
        this.letter = document.querySelector('.letter');
        this.shortDescription = document.querySelector('.logo-content .text');
        this.intervalID = null;
        this.delay = 3050;
    }

    run() {
        this.intervalID = setInterval(() => {
            this.letter.classList.add('letter-animation');
            this.shortDescription.classList.add('text-slide-down');
            this.letter.textContent = this.text[this.j];
            this.j = this.j + 1;
            if (this.j >= this.text.length) {
                this.j = 0;
            }

            const functionAfterAnimation = () => {
                this.letter.classList.remove('letter-animation');
                this.letter.removeEventListener('webkitAnimationEnd', functionAfterAnimation, true);
            }

            this.letter.addEventListener('webkitAnimationEnd', functionAfterAnimation);


        }, this.delay);
    }


}