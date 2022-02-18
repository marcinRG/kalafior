import './scss/app.scss';
import {ScrollButtons} from './js/scrollButtons/scrollButtons';
import {LocalStorage} from './localStorage/localStorage';
import {Settings} from './js/settings/settings';

class AppWinnieThePooh {
    constructor() {
        this.appState = Settings.appStates.LOADING;
        this.titleScreen = document.querySelector('.screen.title');
        this.displayScreen = document.querySelector('.screen.book-display');
        this.loadingScreen = document.querySelector('.screen.loading');
        this.errorScreen = document.querySelector('.screen.error');
        this.errorButton = document.querySelector('.btn.error');
        this.nextParagraphsButton = document.querySelector('.btn.next');
        this.previousParagraphsButton = document.querySelector('.btn.previous');
        this.randomParagraphsButton = document.querySelector('.btn.random');

        this.errorButton.addEventListener('click', () => {
            this.initializeData()
        });

        this.scrollButtons = new ScrollButtons();
        this.localStorage = new LocalStorage();
        this.authorAndTitle = {};
        this.text = [];
        this.line = 0;
        this.appLoading();
        this.initializeData();
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

    fillBookParagraphs(lineNumber) {
        const ps = document.querySelectorAll('div.book-paragraphs > p');
        ps.forEach((p, i) => {
            p.textContent = (lineNumber + i) + ': ' + this.text[lineNumber + i]
        })
    }

    loadDataFromServer() {
        fetch('http://127.0.0.1:5000/kubus_puchatek/data').then(response => response.json()).then(data => {
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
                    this.fillBookParagraphs(this.line);
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
                    this.fillBookParagraphs(this.line);
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



