(function (ng) {
    'use strict';
    
    var kgraphGraphDirectives = ng.module('kgraphGraphDirectives', []);
    var baseTplUrl = '/static/js/graph/partials/';
    
    kgraphGraphDirectives.directive('graphMainSvg', function () {

        function ctrl() {
            this.height = '300px',
            this.width = '300px';
        }
        return {
            restrict: 'E',
            templateUrl: baseTplUrl + 'graphMainSVG.html',
            replace: true,
            scope: {},
            controller: ctrl,
            controllerAs: 'graphMainSvgCtrl',
            bindToController: true
        };

    });

})(angular);
