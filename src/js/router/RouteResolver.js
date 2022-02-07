export class RouteResolver {
    constructor(routeSettings) {
        this.routes = routeSettings.routes;
        this.defaultRoute = routeSettings.defaultRoute;
        this.errorRoute = routeSettings.errorRoute;
        this.regEx = /(\/\S*?)+(?:\/?$)/;
    }

    isPathValid(path) {
        if (path && !path.includes('//')) {
            return this.regEx.test(path);
        }
        return false;
    }

    isRouteValid(route) {
        if (this.routes && this.routes.length > 0) {
            return (this.routes.indexOf(route) >= 0);
        }
        return false;
    }

    getRouteAndParameters(path) {
        let route = this.errorRoute;
        let params = {};
        if (this.isPathValid(path)) {
            route = this.defaultRoute;
            if (path !== '/') {
                const paramsArray = getRouteAndParametersArray(path);
                route = getRoute(paramsArray);
                params = getParameters(paramsArray);
            }
        }
        return {
            route,
            parameters: params
        };
    }
}

function removeFirstAndLastSlash(str) {
    if ((str) && (str.length > 0)) {
        if (str.charAt(0) === '/') {
            str = str.substring(1, str.length);
        }
        if (str.charAt(str.length - 1) === '/') {
            str = str.substring(0, str.length - 1);
        }
    }
    return str;
}

function getRouteAndParametersArray(str) {
    let paramsArray = [];
    str = removeFirstAndLastSlash(str);
    if (str && str.length > 0) {
        paramsArray = str.split('/');
    }
    return paramsArray;
}

function getRoute(paramsArray) {
    if (paramsArray && paramsArray.length > 0) {
        return paramsArray[0];
    }
    return null;
}

function getParameters(paramsArray) {
    let params = {};
    if (paramsArray && paramsArray.length > 2) {
        for (let i = 1; i < paramsArray.length - 1; i = i + 2) {
            params[paramsArray[i]] = paramsArray[i + 1];
        }
    }
    return params;
}
