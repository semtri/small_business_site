angular.module('smallBusinessApp', ['ngMaterial'])
.config(function($httpProvider){
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
.controller('navCtrl', function($scope, $http, $mdDialog) {
	$scope.showLogin = function(ev) {
		$mdDialog.show({
			controller: DialogController,
			templateUrl: '/login_dlg/',
			parent: angular.element(document.body),
			targetEvent: ev,
			clickOutsideToClose: true,
			fullscreen: true,
		})
	}
	
	function DialogController($scope, $mdDialog) {
		$scope.cancel = function() {
			$mdDialog.cancel();
		}
	}
});