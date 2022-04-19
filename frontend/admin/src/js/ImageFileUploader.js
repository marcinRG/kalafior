export class ImageFileUploader {
    constructor() {
        this.fileInput = document.querySelector('.image-uploader .input-file');
        this.fileName = document.querySelector('.image-uploader .file-name');
        this.uploadButton = document.querySelector('.image-uploader .small-button');
        this.thumbnailImage = document.querySelector('.image-uploader .uploaded-image');
        this.fileName.value = '';
        this.fileInput.value = '';
        this.addFileUploadHandler();
        this.addButtonHandler();
    }

    loadImage() {
        if (this.thumbnailImage) {
            this.thumbnailImage.classList.add('hide');
        }
        const file = this.fileInput.files[0];
        const fileReader = new FileReader();
        const img = new Image();

        fileReader.addEventListener('load', () => {
            img.src = fileReader.result;
            img.addEventListener('load', () => {
                if (this.thumbnailImage) {
                    this.thumbnailImage.src = img.src;
                    this.thumbnailImage.classList.remove('hide');
                }
                if (this.fileName) {
                    this.fileName.value = file.name;
                }
            });
        });
        fileReader.readAsDataURL(file);
    }

    addButtonHandler() {
        if (this.uploadButton && this.fileInput) {
            this.uploadButton.addEventListener('click', () => {
                this.fileInput.click();
            })
        }
    }

    addFileUploadHandler() {
        if (this.fileInput) {
            this.fileInput.addEventListener('change', () => {
                this.loadImage();
            });
        }
    }


}