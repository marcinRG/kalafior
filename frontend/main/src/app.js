import './scss/app.scss';
import {Menu} from './js/menu/Menu';
import {MainSlider} from './js/main-slider/MainSlider';
import {AnimatedLetter} from './js/animated-letter/AnimatedLetter';
import {loadImages} from './js/images/background-images';
import {UpArrows} from './js/UpArrows/UpArrows';

const loadMessage = document.querySelector('.loading-screen .loading-msg');
const loadScreen = document.querySelector('.loading-screen');


let imagesLinks = [];
let slides = [];
const serverPath = 'http://127.0.0.1:5000/'
const imagesPath = 'http://127.0.0.1:5000/app/slider/images';
const dataPath = 'http://127.0.0.1:5000/app/slider/data';

// const serverPath = '/'
// const imagesPath = '/app/slider/images';
// const dataPath = '/app/slider/data';

function getDataFromServer(serverPath) {
    return fetch(serverPath, {
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'}
    }).then(response => response.json()).then(data => {
        return data;

    }).catch((err) => {
        return err;
    });
}


const menu = new Menu();
const upArrows = new UpArrows();

getDataFromServer(imagesPath).then(data => {
    for (const img of data) {
        imagesLinks.push(serverPath + img);
    }
}).then(() => {
    return getDataFromServer(dataPath).then(data => {
        slides = data;
    })
}).then(() => {
    return loadImages(imagesLinks, loadMessage).then((images) => {
        loadScreen.classList.add('hide');
        const mainSlider = new MainSlider(slides, images);
        mainSlider.run();
        const animatedLetter = new AnimatedLetter();
        animatedLetter.run();
    })
}).catch((err) => {
    console.log(err.message);
});
