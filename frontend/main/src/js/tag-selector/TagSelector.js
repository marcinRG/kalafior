export class TagSelector {
    constructor() {
        this.buttons = [];
        this.tagButtonContainer = document.querySelector('.tag-buttons');
        this.projects = getProjects(Array.from(document.querySelectorAll('.project-container')));
        this.uniqueTags = getUniqueTags(document.querySelectorAll('.project-container .project-tags li'));
        this.createButtons();
    }

    createButtons() {
        this.tagButtonContainer.innerHTML = '';
        const showAllButton = createButton('Wszystkie');
        showAllButton.addEventListener('click', () => {
            this.showAllElements();
            this.unselectAllButtons();
            showAllButton.classList.add('selected');
        });

        this.tagButtonContainer.append(showAllButton);
        for (const tag of this.uniqueTags) {
            let button = createButton(tag);
            button.addEventListener('click', () => {
                this.showSelectedElements(tag);
                button.classList.add('selected');
                showAllButton.classList.remove('selected');
            })

            this.buttons.push(button);
            this.tagButtonContainer.append(button);
        }
    }

    showAllElements() {
        for (const project of this.projects) {
            project.element.classList.remove('hide');
        }
    }

    showSelectedElements(selectedTag) {
        for (const project of this.projects) {
            if (!project.tags.includes(selectedTag)) {
                project.element.classList.add('hide');
            }
        }
    }

    unselectAllButtons() {
        for (const button of this.buttons) {
            button.classList.remove('selected');
        }
    }


}

function getUniqueTags(elements) {
    const tags = Array.from(elements).map(el => el.textContent);
    const uniqueTags = [...new Set(tags)];
    return uniqueTags;
}

function getProjects(projects) {
    return projects.map((project) => {
        return {
            element: project,
            tags: getUniqueTags(project.querySelectorAll('.project-tags li'))
        }
    });
}

function createButton(name) {
    const button = document.createElement('button');
    button.classList.add('button')
    button.textContent = name;
    return button;
}
