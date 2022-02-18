import * as localForage from 'localforage';
import {Settings} from '../js/settings/settings';

export class LocalStorage {
    constructor() {

    }

    config() {
        return new Promise((resolve, reject) => {
            try {
                localForage.config(Settings.storage);
                resolve(true);
            } catch (error) {
                reject(error);
            }
        });
    }

    getText() {
        return localForage.getItem('text').then(data => this.hasData(data));
    }

    getCurrentLine() {
        return localForage.getItem('line').then(data => this.hasData(data));
    }

    getAuthorAndTitle() {
        return localForage.getItem('bookDetails').then(data => this.hasData(data));
    }

    setLine(value) {
        return localForage.setItem('line', value);
    }

    setAuthorAndTitle(value) {
        return localForage.setItem('bookDetails', value);
    }

    setText(value) {
        return localForage.setItem('text', value);
    }


    hasData(data) {
        return new Promise((resolve, reject) => {
            if (data !== null || data !== undefined) {
                resolve(data);
            }
            reject(new Error('Brak danych'))
        });
    }


}