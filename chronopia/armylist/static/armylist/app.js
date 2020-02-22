var app = angular.module("chronopiaApp", ["ngRoute", "ngAnimate", "ngCookies","data","armyCreationModule"]);

app.config(["$resourceProvider", function($resourceProvider) {
	
	// ngResource configuration
	$resourceProvider.defaults.stripTrailingSlashes = false;
	var actions = $resourceProvider.defaults.actions;
    actions.patch  = {method: 'PATCH'};

    // REST Framework mapping
    // http://www.django-rest-framework.org/api-guide/viewsets/
    // https://docs.angularjs.org/api/ngResource/service/$resource
    actions.list     = {method: 'GET', isArray:true};
    actions.create   = {method: 'POST'};
    actions.retrieve = {method: 'GET'};
    actions.update   = {method: 'PUT'};
    actions.partial  = {method: 'PATCH'};
    actions.destroy  = {method: 'DELETE'};

}]);

app.config(["$routeProvider","$locationProvider", function($routeProvider,$locationProvider){
	$locationProvider.html5Mode(true);
		// Routes configuration
	$routeProvider
	//.when('/', { redirectTo : '/home' })
	.when('/armees', { controller : 'armyOverviewController', controllerAs : 'armyCtrl', templateUrl : '/static/ArmyCreation/Overview.html' })
	.when('/listarmee/:ID', { controller : 'partyCreationController', controllerAs : 'partyCtrl', templateUrl : '/static/compoCreation/partycreation.html' })
	.when('/compoOverView', { controller : 'partyOverviewController', controllerAs : 'partyOverCtrl', templateUrl : '/static/compoOverview/partyOverview.html' })
	.when('/detail/:ID', { controller : 'partyDetailController', controllerAs : 'partyDetailCtrl', templateUrl : '/static/Detail_Troupe/partyDetail.html' })
	.when('/rules/', { controller : 'partyDetailController', controllerAs : 'partyDetailCtrl', templateUrl : '/static/rules/index.html' })
	.when('/rules/images/', { controller : 'partyDetailController', controllerAs : 'partyDetailCtrl', templateUrl : '/static/rules/images/' })

	.otherwise({ redirectTo : '/compoOverView' });
}]);

//Update xsrf $http headers to align with Django's defaults
app.run(['$http', function ($http) {
	$http.defaults.xsrfHeaderName = 'X-CSRFToken';
	$http.defaults.xsrfCookieName = 'csrftoken';
}]);

