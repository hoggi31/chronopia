var armyModule = angular.module("armyCreationModule");

armyModule.controller("partyDetailController", ["ArmyPartyDisplay", "user", "$routeParams", function(ArmyPartyDisplay, user, $routeParams) {
    var self = this;
    self.partyTroupId = $routeParams.ID;
    var promUser = user.myself();

    promUser.$promise.then(function(res) {
        var troupsPromise = ArmyPartyDisplay.get({ armyParty: self.partyTroupId, author: res.id });
        console.log(troupsPromise);

        self.idactif = 0;

        troupsPromise.$promise.then(function(res) {
            console.log(res);
            self.troups = res;

            self.selectedTroup = self.troups.unitList[0];
        });

    });



    self.setSelectedTroup = function(unit) {
        self.selectedTroup = unit;

    }



    self.isSelect = function(unit) {
        return (unit.id == self.selectedTroup.id);

    }

    self.isUnit = function(element) {
        return (angular.isUndefined(element.unit) || element.unit === null)

    }

    self.IsMago = function(unit) {
        return (unit.magie > 0);
    }
    self.isUser = function() {
        return promUser == self.troups.user;

    }

}]);