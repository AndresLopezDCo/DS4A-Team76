/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(document).ready(function() {
  var unique_id = $.gritter.add({
    // (string | mandatory) the heading of the notification
    title: 'Welcome to Dashio!',
    // (string | mandatory) the text inside the notification
    text: 'Hover me to enable the Close Button. You can hide the left sidebar clicking on the button next to the logo.',
    // (string | optional) the image to display on the left
    image: 'usuario.jpg',
    // (bool | optional) if you want it to fade out on its own or just sit there
    sticky: false,
    // (int | optional) the time you want it to be alive for before fading out
    time: 8000,
    // (string | optional) the class name you want to apply to that specific message
    class_name: 'my-sticky-class'
  });

  return false;
});