angular.module('data')
  .factory('user', ['$resource',
    function($resource){
      return $resource('/api/v1/users/:dd/:verb/', {id:'@id'}, {myself: {method:'GET', params:{verb:'myself'}}});
    }]
  )
