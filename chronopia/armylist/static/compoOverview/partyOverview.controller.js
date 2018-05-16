var armyModule = angular.module("armyCreationModule");

armyModule.controller("partyOverviewController", ["ArmyParty", "user", "$scope", "$location", "$routeParams", function(ArmyParty, user, $scope, $location, $routeParams) {
    var self = this;
    var promUser = user.myself();
    self.NewParty = new ArmyParty();

    self.path = function(id) {
        return $location.path('/listarmee/' + id).search({});
    };

    self.pathDetail = function(id) {
        return $location.path('/detail/' + id).search({});
    };

    self.create = function() {
        self.NewParty.army = 1; //useless
        self.NewParty.totalCost = 0; // a calculer coté serveur
        console.log("yo");
        self.NewParty.$save(
            function(resp, headers) {
                //success callback
                console.log(resp);
                self.refresh();
            }
        );

    }

    self.refresh = function() {
        promUser.$promise
            .then(function(res) {
                $scope.user = res;
                self.selectedArmy = null;

                var listCompo = ArmyParty.query({ author: $scope.user.id });
                listCompo.$promise.then(function(res) {
                    self.compoList = res;
                });

            });
    };
    self.deleteCompo = function(compo) {
        compo.$delete(function(resp) {
            console.log("deleted");
            self.refresh();
        });
    }

    self.refresh();








}]);