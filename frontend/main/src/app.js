import img01 from './images/letter-backgrounds/k1.jpg';
import img02 from './images/letter-backgrounds/k2.jpg';
import img03 from './images/letter-backgrounds/k3.jpg';
import img04 from './images/letter-backgrounds/k4.jpg';
import img05 from './images/letter-backgrounds/k5.jpg';
import img06 from './images/letter-backgrounds/k6.jpg';
import img07 from './images/letter-backgrounds/k7.jpg';
import img08 from './images/letter-backgrounds/k8.jpg';

import './scss/app.scss';
import {loadImages} from './js/images/background-images';

const imageLinks = [img01, img02, img03, img04, img05, img06, img07, img08];
const loadMessage = document.querySelector('.loading-screen .loading-msg');
const loadScreen = document.querySelector('.loading-screen');

loadImages(imageLinks, loadMessage).then((images) => {
    console.log(images);
    loadScreen.classList.add('hide');

}).catch((error) => {
    console.log(error.message);
});

// const bgImages = new BackgroundImages();
// const imgs = bgImages.loadImages();
// const testImage = document.querySelector('.test-image');
// console.log(testImage.src);
// console.log(imgs);
