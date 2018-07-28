odoo.define('code_building_block.highlightjs', function (require) {
"use strict";

$(document).ready(function() {
  $('pre code').each(function(i, block) {
    hljs.highlightBlock(block);
  });
});

});



