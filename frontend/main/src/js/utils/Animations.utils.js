import Velocity from 'velocity-animate';

export function scrollTo(elem, time, easing) {
    Velocity(elem, 'scroll', {
        duration: time,
        easing: easing
    });
}

