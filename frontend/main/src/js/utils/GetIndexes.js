export function getIndexes(i, max) {
    let previous = i - 1;
    let current = i;
    let next = i + 1;

    if (i === 0) {
        previous = max;
    }
    if (i === max) {
        next = 0;
    }

    return {
        previous,
        current,
        next
    }
}