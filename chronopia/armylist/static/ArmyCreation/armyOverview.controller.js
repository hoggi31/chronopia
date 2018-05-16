var armyModule = angular.module("armyCreationModule");

armyModule.controller("armyOverviewController",["army","unit",function(army,unit){
	var self =this;
	
	
	self.selectedArmy = null;
	
	var arm =  army.query();
	arm.$promise.then(function(res){
		self.armyList = res;
		console.log(self.selectedArmy.name);
	});	
	
	self.addGobs = function(){
		for (gobs in self.listArmee){
			var unitU = new unit;
			unit.$save(gobs);
		}
		
	}
		
	
	
}]);