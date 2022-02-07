export class SvgExample {
    constructor() {
        this.intervalLength = 5000;
        this.showJunior = true;
        this.svg1 = document.querySelector('svg.svg-1');
        this.intervalId = null;
        this.changeDisplayedItem = this.changeDisplayedItem.bind(this);
    }

    run() {
        console.log('run');
        this.intervalId = window.setInterval(this.changeDisplayedItem, this.intervalLength);
    }

    close() {
        window.clearInterval(this.intervalId);
        this.svg1.classList.remove('senior');
        this.svg1.classList.remove('junior');
        console.log('close');
    }

    changeDisplayedItem() {
        if (this.showJunior) {
            changeClassToJunior(this.svg1);
            this.showJunior = false;
        } else {
            changeClassToSenior(this.svg1);
            this.showJunior = true;
        }
        resetAnimationWavesAndLetters(this.svg1);
    }

}

function resetAnimationsOnElement(element,selector) {
    const elemToReset = element.querySelector(selector);
    const copyOfElem = elemToReset.cloneNode(true);
    elemToReset.parentNode.replaceChild(copyOfElem,elemToReset);
}

function resetAnimationWavesAndLetters(element) {
    resetAnimationsOnElement(element,'.waves');
    resetAnimationsOnElement(element,'.letter-container');
}


function changeClassToJunior(element) {
    element.classList.remove('senior');
    element.classList.add('junior');
}

function changeClassToSenior(element) {
    element.classList.remove('junior');
    element.classList.add('senior');
}

const svgExample = new SvgExample();
svgExample.run();
