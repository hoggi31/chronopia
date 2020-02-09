var armyModule = angular.module("armyCreationModule");

armyModule.controller("partyCreationController", ["army", "user", "ArmyPartyDisplay", "Troups", "unit", "$routeParams", "spells", "spellsf", function(army, user, ArmyPartyDisplay, Troups, unit, $routeParams, spells, spellsf) {
    var self = this;


    var promUser = user.myself();
    var currentUser = null;
    promUser.$promise.then(function(res) {
        currentUser = res;
        self.getArmyParty();

    });

    self.selectedArmy = null;
    self.party = new ArmyPartyDisplay();
    self.totalCost = 0;
    self.totaltir = 0;
    self.totalindep = 0;
    self.counttir = 0;
    self.countinde = 0;
    self.countunit = 0;

    self.IdArmee = $routeParams.ID;
    self.unitList = [];

    self.independant = true;
    self.Unite = true;
    self.Tir = false;
    self.search = "";

    self.oktir = true;
    self.okindep = true;
    
    self.tirratio = 0;

    self.updateFilter = function(aType) {
        self.filter = {};
        self.filter.type = aType;
        self.updateSearch();

        //if (self.Tir){
        //	self.filter.Tir = self.Tir;
        //};
        //if ((self.independant) & (!self.Unite)){

        //};
        //if (!(self.independant) & (self.Unite)){
        //	self.filter.type= 'Unite';	
        //};

    };

    self.filter = {};

    self.updateSearch = function() {
        self.setListUnit();
        self.setListSort();
    }

    self.getArmyParty = function() {
        var partyPromise = ArmyPartyDisplay.get({ armyParty: self.IdArmee, author: currentUser.id });
        partyPromise.$promise.then(function(res) {
            self.party = res;
            self.updateCountUnitList();
        });
        self.getCost();
    }

    self.getCost = function() {
        var partyPromise = ArmyPartyDisplay.totalCost({ armyParty: self.IdArmee });
        partyPromise.$promise.then(function(res) {
            console.log(res.total);
            self.totalCost = res.total;
            self.totaltir = res.totaltir;
            self.totalindep = res.unitIndep;
            self.counttir = res.counttir;
            self.countinde = res.countinde;
            self.countunit = res.countunit;
            self.tirratio = parseInt(self.totaltir / self.totalCost * 100);
            self.oktir = (self.tirratio <= 40)
            self.okindep = ((self.countinde / self.countunit) <= 0.5)

        });
    }

    self.hasRangeAttack = function(attack) {
        return (attack.portee != '');
    }

    self.setList = function() {
        self.setListUnit();
        self.setListSort();
    }

    self.setListUnit = function() {
        var unitpromise = unit.query({
            army: self.selectedArmy.id,
            search: self.search
        });
        unitpromise.$promise.then(function(res) {
            self.unitList = res;
            self.updateCountUnitList();
        })
    }

    self.updateCountUnitList = function() {
        for (var i = 0; i < self.unitList.length; i++) {
            var idx = _.findIndex(self.party.unitList, function(o) { return o.unit.id == self.unitList[i].id; });
            //console.log(idx);
            if (idx == -1) {
                self.unitList[i].count = 0;
            } else {
                self.unitList[i].count = self.party.unitList[idx].count;
            }
        };


    }

    self.updateCountSpellList = function() {
        for (var i = 0; i < self.spellList.length; i++) {
            var idx = _.findIndex(self.party.spellList, function(o) { return o.spell.id == self.spellList[i].id; });
            //console.log(idx);
            if (idx == -1) {
                self.spellList[i].count = 0;
            } else {
                self.spellList[i].count = self.party.spellList[idx].count;
            }
        };
    }

    self.setListSort = function() {
        var spellpromise = spellsf.query({ army: self.selectedArmy.id });
        spellpromise.$promise.then(function(res) {
            self.spellList = res;
            self.updateCountSpellList();
        })
    }

    self.partyTroupes = [];
    var arm = army.query();

    arm.$promise.then(function(res) {
        self.armyList = res;
    });

    self.addSpell = function(spell, num) {
        var idx = -1;
        console.log(self.party.spellList.length);
        for (var i = 0; i < self.party.spellList.length; i++) {
            if (self.party.spellList[i].spell.id == spell.id) {
                idx = i;
            }
        }
        if (idx > -1) {
            var spellPromise = spells.get({ spell: self.party.spellList[idx].id, ArmyParty: self.party.id });
            //console.log(spellPromise);		

            spellPromise.$promise.then(function(res) {
                var spellUpdate = res;
                spellUpdate.count = spellUpdate.count + num;
                if (spellUpdate.count > 0) {
                    spellUpdate.$update(function(resp) {
                        self.getArmyParty();

                    });
                } else {
                    spellUpdate.$delete(function(resp) {
                        console.log("deleted");
                        self.getArmyParty();
                    });
                }

                //self.getArmyParty();
            });
        } else {
            var newSpell = new spells();
            newSpell.count = 1;
            newSpell.spell = spell.id;
            newSpell.armyParty = self.party.id;
            newSpell.$save(function(resp) {
                self.getArmyParty();
            });

        }

    }
    self.removetroupe = function(unit) {
        var troupPromise = Troups.get({ troup: unit.id, ArmyParty: self.party.id });
        troupPromise.$promise.then(function(res) {
            var troupUpdate = res;
            troupUpdate.$delete(function(resp) {
                console.log("deleted");
                self.getArmyParty();
            });
        });

    }
    self.addtroupe = function(unit, num) {
        var idx = -1;
        //console.log(self.party.unitList.length);
        /*for (var i = 0; i < self.party.unitList.length; i++) {
            if (self.party.unitList[i].unit.id == unit.id) {
                idx = i;
            }
        }
        if (idx > -1) {
            var troupPromise = Troups.get({ troup: self.party.unitList[idx].id, ArmyParty: self.party.id });
            //console.log(troupPromise);		

            troupPromise.$promise.then(function(res) {
                var troupUpdate = res;
                troupUpdate.count = troupUpdate.count + num;

                if (troupUpdate.count > 0) {
                    troupUpdate.$update(function(resp) {
                        self.getArmyParty();
                        //self.updateCountUnitList();
                    });
                } else {
                    troupUpdate.$delete(function(resp) {
                        console.log("deleted");
                        self.getArmyParty();
                    });
                }

                //self.getArmyParty();
                //Troups.delete({troup:self.party.unitList[idx].id) TODO
            });*/
        //} else {

        var newTroup = new Troups();
        newTroup.count = 1;
        newTroup.unit = unit.id;
        newTroup.armyParty = self.party.id;
        newTroup.$save(function(resp) {
            self.getArmyParty();

        });

        //}
        //self.updateCountUnitList();
    }
    self.updateTroup = function(unit, currentelement) {

        console.log(unit.count);

        var troupPromise = Troups.get({ troup: unit.id, ArmyParty: self.party.id });

        troupPromise.$promise.then(function(res) {
            var troupUpdate = res;
            troupUpdate.count = unit.count;

            if (troupUpdate.count > 0) {
                troupUpdate.$update(function(resp) {
                    self.getArmyParty();
                    //self.updateCountUnitList();
                });
            } else {
                troupUpdate.$delete(function(resp) {
                    console.log("deleted");
                    self.getArmyParty();
                });
            }

        });


    }


    self.updatepartyname = function() {
        console.log(self.party.name);
        self.party.$update(function(resp) {
            self.getArmyParty();
            //self.updateCountUnitList();
        });
    }
}]);