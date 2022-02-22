import './scss/app.scss';
import {ScrollButtons} from './js/scrollButtons/scrollButtons';
import {LocalStorage} from './localStorage/localStorage';
import {Settings} from './js/settings/settings';
import Velocity from 'velocity-animate';
import {getRandomInt} from './js/utils/Random';

class AppWinnieThePooh {
    constructor() {
        this.appState = Settings.appStates.LOADING;
        this.bookLinesQuantity = Settings.appSetting.lines;
        this.titleScreen = document.querySelector('.screen.title');
        this.displayScreen = document.querySelector('.screen.book-display');
        this.loadingScreen = document.querySelector('.screen.loading');
        this.errorScreen = document.querySelector('.screen.error');
        this.errorButton = document.querySelector('.btn.error');
        this.previousParagraphsButton = document.querySelector('.btn.previous');

        //book random quote slider

        this.topContainer = document.querySelector('.book-display');
        this.slidesContainer = document.querySelector('.slides');
        this.bookNextBtn = document.querySelector('button.next.page');
        this.bookPreviousBtn = document.querySelector('button.previous.page');
        this.randomBtn = document.querySelector('button.btn.random');
        this.bookBtn = document.querySelector('button.btn.book');
        this.isOnRandom = false;


        this.errorButton.addEventListener('click', () => {
            this.initializeData()
        });

        this.randomBtn.addEventListener('click', () => {
            this.moveToRandom();
        });

        this.bookNextBtn.addEventListener('click', () => {
            if (this.text.length > 0) {
                const newLine = this.line + this.bookLinesQuantity;
                if (newLine < this.text.length) {
                    this.localStorage.setLine(newLine).then(() => {
                        this.line = newLine;
                        this.fillBookText();
                    });
                }
            }
        });

        this.bookPreviousBtn.addEventListener('click', () => {
            if (this.text.length > 0) {
                const newLine = this.line - this.bookLinesQuantity;
                if (newLine >= 0) {
                    this.localStorage.setLine(newLine).then(() => {
                        this.line = newLine;
                        this.fillBookText();
                    });
                }
                this.fillBookText();
            }
        });

        this.bookBtn.addEventListener('click', () => {
            this.moveToBook();
        });

        this.scrollButtons = new ScrollButtons();
        this.localStorage = new LocalStorage();
        this.authorAndTitle = {};
        this.text = [];
        this.line = 0;
        this.appLoading();
        this.initializeData();
    }


    moveToRandom() {
        if (!this.isOnRandom) {
            const width = this.topContainer.getBoundingClientRect().width;
            this.isOnRandom = true;
            this.bookNextBtn.classList.add('hide');
            this.bookPreviousBtn.classList.add('hide');
            this.bookBtn.classList.remove('hide');
            Velocity(this.slidesContainer, {left: -width}, {duration: 1000});
        }
        this.fillRandomQuote();

    }

    moveToBook() {
        this.bookNextBtn.classList.remove('hide');
        this.bookPreviousBtn.classList.remove('hide');
        this.bookBtn.classList.add('hide');
        this.isOnRandom = false;
        Velocity(this.slidesContainer, {left: 0}, {duration: 1000});
    }

    fillBookText() {
        if (this.text.length > 0) {
            const ps = Array.from(document.querySelectorAll('.book-paragraphs p.book-p'));
            this.fillParagraphs(ps, this.line, this.bookLinesQuantity);
        }
    }


    fillRandomQuote() {
        if (this.text.length > 0) {
            const ps = Array.from(document.querySelectorAll('.book-random p.book-p'));
            const random = getRandomInt(this.text.length - 2);
            this.fillParagraphs(ps, random, 2);
        }

    }

    fillParagraphs(paragraphs, start, quantity) {
        this.clearParagraphs(paragraphs);
        for (let i = 0; i < quantity; i++) {
            if (this.text.length > start + i) {
                paragraphs[i].textContent = this.text[start + i];
            }
        }
    }

    clearParagraphs(paragraphs) {
        paragraphs.forEach((p) => {
            p.textContent = '';
        })
    }


    appLoading() {
        this.appState = Settings.appStates.LOADING;
        this.hideAllScreens();
        this.loadingScreen.classList.remove('hide');
    }

    appError() {
        this.appState = Settings.appStates.ERROR;
        this.hideAllScreens();
        this.errorScreen.classList.remove('hide');
    }

    appNormal() {
        this.appState = Settings.appStates.ERROR;
        this.hideAllScreens();
        this.titleScreen.classList.remove('hide');
        this.displayScreen.classList.remove('hide');
    }

    hideAllScreens() {
        const screens = document.querySelectorAll('div.screen');
        screens.forEach((screen) => {
            screen.classList.add('hide');
            screen.removeAttribute('style');
        })
    }


    loadDataFromServer() {
        fetch(Settings.appSetting.serverPath).then(response => response.json()).then(data => {
            this.authorAndTitle = {
                author: data.author,
                title: data.title,
            }
            this.text = data.text;
            this.line = 0;

            this.localStorage.setText(this.text)
                .then(() => this.localStorage.setLine(this.line))
                .then(() => this.localStorage.setAuthorAndTitle(this.authorAndTitle))
                .then(() => {
                    this.appNormal();
                    this.fillBookText();

                }).catch((err) => {
                console.log(err.message)
                this.appError();
            })

        }).catch((error) => {
            console.log(error.message);
            this.appError();
        });
    }


    initializeData() {
        this.localStorage.config().then(() => {
            return Promise.all([this.localStorage.getAuthorAndTitle(),
                this.localStorage.getText(),
                this.localStorage.getCurrentLine()])
                .then((data) => {
                    this.authorAndTitle = data[0];
                    this.text = data[1];
                    this.line = data[2];
                    this.fillBookText();
                    this.appNormal();
                });
        }).catch((err) => {
            console.log(err.message);
            this.loadDataFromServer();
        });
    }
}


window.addEventListener('load', () => {
    const winnie = new AppWinnieThePooh();
})



