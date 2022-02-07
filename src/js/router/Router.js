export class Router {
    constructor(routeResolver) {
        this.routeResolver = routeResolver;
        this.errorHandler = null;
        this.routeAndParams = [];
    }

    run() {
        this.setFirstRun();
        window.addEventListener('popstate', () => {
            let reqParams = this.getReqParams();
            this.handleRequest(reqParams);
        });
    }

    setFirstRun() {
        let reqParams = this.getReqParams();
        if (!(reqParams.route && this.routeResolver.isRouteValid(reqParams.route))) {
            reqParams = {
                route: this.routeResolver.defaultRoute,
                parameters: {}
            };
        }
        this.handleRequest(reqParams);
    }

    getReqParams() {
        const path = document.location.hash.slice(1);
        return this.routeResolver.getRouteAndParameters(path);
    }

    handleError(reqParams) {
        if (this.errorHandler) {
            this.errorHandler(reqParams);
        }
    }

    addRouteHandler(route, handler) {
        this.routeAndParams.push({
            route,
            handler,
        });
    }

    addErrorHandler(handler) {
        if (handler) {
            this.errorHandler = handler;
        }
    }

    handleRequest(reqParams) {
        const index = this.hasHandler(reqParams.route);
        if (reqParams.route === this.routeResolver.errorRoute) {
            this.handleError(reqParams);
        }
        if (index >= 0) {
            this.routeAndParams[index].handler(reqParams);
        }
    }

    hasHandler(route) {
        return this.routeAndParams.findIndex((elem) => {
            return ((elem) && (elem.route === route));
        });
    }
}