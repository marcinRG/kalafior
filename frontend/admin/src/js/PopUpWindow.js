export class PopUpWindow {
    constructor() {
        this.body = document.querySelector('body');
        this.div = document.querySelector('.info-wrapper');
        const scrollTop = document.documentElement.scrollTop;
        this.div.style.top = scrollTop + 'px';

        this.body.append(this.div);
        console.log(document.documentElement.clientHeight);
        console.log(document.documentElement.offsetHeight);
        console.log('doc offsetTop,: ', document.documentElement.offsetTop);
        console.log('doc, scrollTop: ', document.documentElement.scrollTop);
        console.log('docu, scrollWidth: ', document.documentElement.scrollWidth)
        console.log(this.body.clientHeight);
        console.log(this.body.offsetHeight)
    }
}