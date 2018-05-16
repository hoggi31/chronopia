angular.module('data')
  .factory('army', ['$resource',
    function($resource){
      return $resource('/api/v1/Army/:Id/', {armyId:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}});
    }]
  )
  .factory('unit', ['$resource',
    function($resource){
	  return $resource('/api/v1/Unit/:Id/', {unitId:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}, populate_xls:{methode:'POST'}});
    }]
  )
  .factory('ArmyParty', ['$resource',
    function($resource){
	  return $resource('/api/v1/ArmyParty/:armyParty/', {armyParty:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}, get: {method: 'GET'}});
    }]
  )
  .factory('ArmyPartyDisplay', ['$resource',
    function($resource){
	  return $resource('/api/v1/ArmyPartyDisplay/:armyParty/:verb', {armyParty:'@id'}, {update: { method:'PUT' }, save: {method:'POST'},totalCost:{method: 'GET',params:{verb:'totalCost'} }  });
    }]
  )
  
  .factory('Troups', ['$resource',
    function($resource){
	  return $resource('/api/v1/troupes/:troup/', {troup:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}});
    }]
  )
  .factory('spells', ['$resource',
    function($resource){
	  return $resource('/api/v1/spells/:spell/', {spell:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}});
    }]
  )  
  .factory('spellsf', ['$resource',
    function($resource){
	  return $resource('/api/v1/spellsf/:spell/', {spell:'@id'}, {update: { method:'PUT' }, save: {method:'POST'}});
    }]
  )  