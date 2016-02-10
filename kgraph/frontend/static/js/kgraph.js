(function (ng) {
    'use strict';

    var kgraphApp = ng.module('kgraphApp', [
    'ngRoute',
    'kgraphGraphModule' 
    ]);

    kgraphApp.config(['$routeProvider', function ($rp) {
        $rp.
        when('/', {
            templateUrl: 'static/js/main/main.html',
        }).
        when('/graph/:deptid', {
            templateUrl: 'static/js/graph/graph.html'
        }).
        otherwise({
            redirectTo: '/'
        });
    }]);
})(angular);