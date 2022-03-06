export const loadImages = (imageLinks, loadMessage) => {

    let images = [];
    let loadedImages = 0;
    return new Promise((resolve) => {
        imageLinks.forEach((imgLink) => {
            let img = new Image();
            img.onload = () => {
                loadedImages = loadedImages + 1;
                loadMessage.textContent = `Ładowanie... ${(loadedImages / imageLinks.length) * 100}  %`;
                images.push(img);
                if (loadedImages === imageLinks.length) {
                    resolve(images);
                }
            }
            img.src = imgLink.toString();
        });
    });
};
