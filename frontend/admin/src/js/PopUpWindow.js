export const ButtonValues = {
    OK: 'ok',
    CANCEL: 'cancel',
    YES: 'yes',
    REMOVE: 'remove'
};

export class PopUpWindow {
    constructor() {
        this.value = ButtonValues.CANCEL;
        this.wrapper = document.querySelector('.info-wrapper');
        this.info = document.querySelector('.info-screen');
        this.windowTitle = document.querySelector('.info-msg .info-title');
        this.message = document.querySelector('.info-msg .message');
        this.buttonWrapper = document.querySelector('.element-btn-wrapper');
        this.showInfoAtCurrentScroll = this.showInfoAtCurrentScroll.bind(this);
        this.showInfoAtCurrentScroll();
    }

    setWindowTitle(text) {
        if (text) {
            this.windowTitle.textContent = text;
        }
    }

    setMessage(text) {
        if (text) {
            this.message.textContent = text;
        }
    }

    showInfoAtCurrentScroll() {
        const scrollTop = document.documentElement.scrollTop;
        this.info.style.top = scrollTop + 'px';
    }

    show() {
        const documentHeight = document.documentElement.offsetHeight;
        this.wrapper.style.height = documentHeight + 'px';
        this.wrapper.style.display = 'block';
    }

    hide() {
        window.removeEventListener('scroll',this.showInfoAtCurrentScroll);
        this.wrapper.style.display = 'none';
    }

    createButtons(buttonsProps, func) {
        this.buttonWrapper.innerHTML = '';
        for (const button of buttonsProps) {
            this.buttonWrapper.append(this.createButton(button, func));
        }
    }

    createButton(buttonProps, func) {
        const button = document.createElement('button');
        button.textContent = buttonProps.title;
        button.className = getButtonClasses(buttonProps.type)
        button.addEventListener('click', () => {
            this.hide();
            func(buttonProps.type);
        });
        return button;
    }



    showPopUpWindow(title, message, buttons, func) {
        this.setWindowTitle(title);
        this.setMessage(message);
        this.show();
        this.showInfoAtCurrentScroll();
        this.createButtons(buttons, func);
        window.addEventListener('scroll',this.showInfoAtCurrentScroll);
    }
}

export function getButtonClasses(buttonValue) {
    let className = `button ${ButtonValues[buttonValue]}`;
    switch (buttonValue) {
        case ButtonValues.OK: {
            return `${className} green`
        }
        case ButtonValues.CANCEL: {
            return `${className} white`
        }
        case ButtonValues.YES: {
            return `${className} green`
        }
        case ButtonValues.REMOVE: {
            return `${className} red`
        }
    }
}
