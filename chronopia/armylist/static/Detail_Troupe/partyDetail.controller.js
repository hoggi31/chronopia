var armyModule = angular.module("armyCreationModule");

// --- WMA rolls metrics JS
var rolls = []; var total= 0;
function recordRoll(s) {
	//console.log(s.innerText);
	rolls.push(s.innerText);
	total+=(parseInt(s.innerText));
	document.getElementById("rollsmetrics").innerText = "Moyenne: "+Math.round(total/rolls.length*10)/10 + " en "+rolls.length+" jets.";
}
// ----------------------					

armyModule.controller("partyDetailController", ["ArmyPartyDisplay", "user", "$routeParams", function(ArmyPartyDisplay, user, $routeParams) {
    var self = this;
    self.partyTroupId = $routeParams.ID;
    var promUser = user.myself();
    showCard: boolean = false ; // hidden by default

    promUser.$promise.then(function(res) {
        var troupsPromise = ArmyPartyDisplay.get({ armyParty: self.partyTroupId, author: res.id });
        console.log(troupsPromise);

        self.idactif = 0;

        troupsPromise.$promise.then(function(res) {
            console.log(res);
            self.troups = res;
	    self.name = res.name;
            self.totalCost = res.totalCost;
      
            self.selectedTroup = self.troups.unitList[0];
        });

    });


    self.setSelectedTroup = function(unit) {
        self.selectedTroup = unit;
        self.showCard=true;
    }

    self.hideCard = function() {
    	self.showCard=false;
    }


    self.isSelect = function(unit) {
        return (unit.id == self.selectedTroup.id);

    }

    self.isUnit = function(element) {
        return (angular.isUndefined(element.unit) || element.unit === null)

    }

    self.removeTroup = function(unit) {
	for (var i = 0 ; i < self.troups.unitList.length;i++) {if (self.troups.unitList[i].unit.id==unit) break;}
	if (i<self.troups.unitList.length) self.troups.unitList.splice(i, 1);
        self.selectedTroup = self.troups.unitList[0];
    }

    self.hasAttackEffect = function(attack) {
        return (attack.Effets != null && attack.Effets != " " && attack.Effets != "");
    }
    
    self.hasMount = function(unit) {
        return (unit.monture.length>0);
    }
    self.hasRangeAttack = function(attack) {
        return (attack.portee != '');
    }
    self.hasFlight = function(unit) {
        return (!angular.isUndefined(unit) && unit.vol> 0);
    }
    self.hasShield = function(unit) {
        return (!angular.isUndefined(unit) && unit.bouclier > 0);
    }
    self.hasPositiveDefense = function(unit) {
        return (!angular.isUndefined(unit) && unit.defence > 0);
    }
    self.IsMago = function(unit) {
        return (unit.magie > 0);
    }
    self.isUser = function() {
        return promUser == self.troups.user;

    }

}]);