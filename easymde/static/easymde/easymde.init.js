var EasyMDE_JQuery = null;

if (typeof jQuery !== 'undefined') {
  EasyMDE_JQuery = jQuery;
} else if (typeof django !== 'undefined') {
  //use jQuery come with django admin
  EasyMDE_JQuery = django.jQuery
} else {
  console.error('Cannot find jQuery. Please make sure jQuery is imported before this script.');
}

if (!!EasyMDE_JQuery) {
  EasyMDE_JQuery(function() {
    EasyMDE_JQuery.each(EasyMDE_JQuery('.easymde-box'), function(i, elem) {
      var options = JSON.parse(EasyMDE_JQuery(elem).attr('data-easymde-options'));
      options['element'] = elem;
      if (elem.EasyMDE === undefined) {
        elem.EasyMDE = new EasyMDE(options);
      }
    });
  });
}
