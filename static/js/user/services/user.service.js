/**
* User
* @namespace crowdsource.user.services
*/
(function () {
  'use strict';

  angular
    .module('crowdsource.user.services')
    .factory('User', User);

  User.$inject = ['$cookies', '$http', '$q', '$location', 'HttpService'];

  /**
  * @namespace User
  * @returns {Factory}
  */

  function User($cookies, $http, $q, $location, HttpService) {
    var User = {
      getProfile : getProfile,
      updateProfile: updateProfile
    };
    return User;

    function getProfile(username) {
      var settings = {
        url: '/api/profile/' + username + '/',
        method: 'GET'
      };
      return HttpService.doRequest(settings);
    }
    function updateProfile(username, address, birthday, country){
      var settings = {
        url: '/api/profile/' + username + '/update_profile/',
        data: {
          address: 'New Delhi',
          birthday: '10/07/1992',
          city: 'New Delhi',
          street:'Batukji Apartments',
          gender:'Male',
          country: 'Indian'   //no need to transfer this but for now required
        },
        method: 'POST'
      };
      return HttpService.doRequest(settings);
    }

  } 

})();