(function($) {
  "use strict";

  function setDirection() {
    var lang = $('#id_language, #id_lang').val(),
      direction = lang === 'he' ? 'rtl' : 'ltr';

    $('input.vTextField').css('direction', direction);

    if (typeof CKEDITOR === 'undefined') return;

    // make sure we have all ckeditor instances ready, the way the widgets
    // is setup, it's a p followed by script
    if (Object.keys && Object.keys(CKEDITOR.instances).length !== $('.django-ckeditor-widget').length) {
      if (console) {
        console.log('editor instances not ready, delaying');
      }
      setTimeout(setDirection, 1000);
      return;
    }
    $.each(CKEDITOR.instances, function(id, editor) {
      var config = $.extend({}, editor.config);
      if (!config) return;
      config.contentsLangDirection = direction;
      editor.destroy();
      CKEDITOR.replace(id, config);
    });
  }
  $(function() {
    var langEl = $('#id_language, #id_lang');

    if (langEl.length) {
      langEl.on('change', setDirection);
      setTimeout(setDirection, 1000);
    }
  });
})(django.jQuery);
