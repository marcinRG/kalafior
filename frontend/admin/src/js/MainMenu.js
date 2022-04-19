import Velocity from 'velocity-animate';

export class MainMenu {
    constructor() {
        this.showMenu = false;
        this.pageSmall = 1240;
        this.menuButton = document.querySelector('.navbar .menu-button');
        this.menuItems = document.querySelector('.navbar .app-menu');
        this.items = this.menuItems.querySelectorAll('.link');
        this.prevWidth = window.outerWidth;
        this.addEventHandlers();
    }

    isSmallSize(size) {
        return (size < this.pageSmall);
    }

    handleResize() {
        const currentSize = window.outerWidth;
        if (this.isSmallSize(this.prevWidth) && !(this.isSmallSize(currentSize))) {
            this.showMenu = false;
            this.menuItems.removeAttribute('style');
        }
        if (!this.isSmallSize(this.prevWidth) && (this.isSmallSize(currentSize))) {
            this.showMenu = false;
            this.menuItems.removeAttribute('style');
        }
        this.prevWidth = currentSize;
    }

    addEventHandlers() {
        this.menuButton.addEventListener('click', () => {
            if (!this.showMenu) {
                Velocity(this.menuItems, {height: 305 + 'px'}, {duration: 500, easing: 'easeOut'});
            } else {
                Velocity(this.menuItems, {height: 0 + 'px'}, {duration: 500, easing: 'easeOut'});
            }
            this.showMenu = !this.showMenu;
        })

        window.addEventListener('resize', () => {
            this.handleResize();
        });

        for (const link of this.items) {
            link.addEventListener('click', () => {
                if (window.outerWidth<this.pageSmall) {
                    Velocity(this.menuItems, {height: 0 + 'px'}, {duration: 500, easing: 'easeOut'});
                    this.showMenu = false;
                }
            })
        }

    }
}