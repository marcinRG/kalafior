import * as localForage from 'localforage';

export const Settings = {
    storage: {
        driver: localForage.INDEXEDDB,
        name: 'Puchatek',
        version: 1.0,
        size: 4980736,
        storeName: 'WinnieDB',
        description: 'baza lokalna do apki Winnie the Pooh',
    },
    appStates: {
        LOADING: 'loading',
        WORKING: 'working',
        ERROR: 'error'
    },
    appSetting: {
        serverPath: '/kubus_puchatek/data',
        lines: 5
    }
}