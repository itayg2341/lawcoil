(function($) {
  'use strict';

  function topicsGetter(e) {
    if (e) {
      e.preventDefault();
    }

    var $this = $(this),
      origContent = $this.html(),
      $parent = $this.parent(),
      topicsParams = $this.data(),

      params = {
        page: topicsParams.topicsPage,
        category: topicsParams.topicsSlug,
        type: topicsParams.topicsType
      };

    $this.html('<i class="fa fa-spinner fa-pulse fa-fw"></i><span class="show-for-sr">Loading...</span>');

    $.get(topicsParams.topicsUrl, params).done(function(result) {
      if (result.rendered_items) {
        $this.html(origContent);
        if (result.category === 'hot-topics') {
          for (var i = 0, l = result.rendered_items.length; i < l; i++) {
            var item = result.rendered_items[i];
            $parent.before(item);
          }
        } else {
          var $topicsColumns = $('.topics-col:visible'),
              totalCols = $topicsColumns.length;

          for (var i = 0, l = result.rendered_items.length; i < l; i++) {
            var item = result.rendered_items[i];
            $($topicsColumns.get(i % totalCols)).append(item);
          }

          var $grandParent = $parent.parent();
          $parent.detach().appendTo($grandParent);
        }
        if (result.next_page) {
          $this.data('topicsPage', result.next_page);
        }
        else {
          $parent.remove();
        }
        new Foundation.Equalizer($('#main-equalizer')).applyHeight();
      }
    });

    if (topicsParams.topicsAlso && e) {
      let itemGetterBound = topicsGetter.bind($(topicsParams.topicsAlso));
      itemGetterBound();
    }

  }

  function showLogin(e) {
    if (e) {
      e.preventDefault();
    }

    var $modal = $('#loginModal');
    $modal.foundation('open');
  }

  function doLogin(ev) {
    ev.preventDefault();
    var $form = $(this);

    $('#login-error').hide();
    $('#submit-id-submit_login').prop('disabled', true);
    $form.find('.form-error').remove();

    $.post($form.attr('action'), $form.serialize())
      .done(function() {
        window.location.reload();
      })
      .fail(function(xhr) {
        var result = xhr.responseJSON;

        if (result.form_errors) {
          for (var key in result.form_errors) {
            if (key === '__all__') {
              $('#login-error span').text(result.form_errors.__all__);
              $('#login-error').show();
            }
            else {
              $('<div class="form-error is-visible""></div>"')
                .text(result.form_errors[key])
                .appendTo($('#div_id_' + key))
            }
          }
        }
      })
      .always(function() {
        $('#submit-id-submit_login').prop('disabled', false);
      });
  }

  function doFollowLink(ev) {
    ev.preventDefault();

    var $this = $(this),
      url = $this.attr('href');

    $.post(url, {})
      .done(function(result) {
        if (result.success) {
          var parent = $this.parent();

          $this.remove();
          parent.append($(result.content))
        }
      });
  }

  function doUnfollowLink(ev) {
    ev.preventDefault();

    var $this = $(this),
      url = $this.attr('href');

    $.post(url, {})
      .done(function(result) {
        if (result.success) {
          $this.parent().parent().fadeOut();
        }
      });
  }

  function doToggleSave(ev) {
    ev.preventDefault();

    var $this = $(this),
      url = $this.attr('href'),
      $icon = $this.find('.fa');

    $this.foundation('hide');
    $.post(url, {})
      .done(function(result) {
        $icon.toggleClass('fa-bookmark-o', !result.is_saved);
        $icon.toggleClass('fa-bookmark', result.is_saved);

        $('#' + $this.data('toggle')).html(result.tooltip);

        var el = $('<div class="callout success"></div>')
          .html(result.message);
        el.appendTo($this.parent().parent());
        setTimeout(function() {
          el.fadeOut(500, function() {el.remove();});
        }, 2000);
      })
      .fail(function(result) {
        if (result.status === 401) {
          showLogin();
        }
      });
  }

  function setupSearchForm() {

    var $searchIn = $('#advanced-search-sections')
    if (!$searchIn.length) {
      return;
    }

    var $radio_buttons = $searchIn.find('[name="search_in"]'),
      $selects = $searchIn.find('select');

    function handleChange() {
      var active = $radio_buttons.filter(':checked').val();
      $selects.each(function() {
        var $this = $(this);
        $this.prop('disabled', $this.attr('id') !== 'id_' + active + '_topic');
      });

    }
    $radio_buttons.on('change', handleChange);
    handleChange();
  }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }

  function addDynamicCsrfToken() {
    var csrftoken = getCookie('csrftoken');
    $('form[method="post"]').each(function() {
      var $form = $(this),
        hasToken = !!($form.find('input[name="csrfmiddlewaretoken"]').length);

      if (hasToken) { return; }

      $('<input type="hidden" name="csrfmiddlewaretoken">').val(csrftoken).prependTo($form);
    });
  }


  function reorderElementsOnMediaChange(newSize, oldSize) {
    if (!newSize && Foundation.MediaQuery.atLeast('large') || (newSize && newSize === oldSize)) {
      return;
    }

    var allItems = $('.listing-item'),
      visibleCols = $('.listing-col:visible'),
      totalCols = visibleCols.length;

    // sort the items in descending order
    allItems.sort(function(a, b) {
      var aDate = $(a).data('date'),
        bDate = $(b).data('date');

      if (aDate < bDate) {
        return 1;
      }
      if (aDate > bDate) {
        return -1;
      }
      // a must be equal to b
      return 0;
    });

    // short circuit for "small", 1 column
    if (totalCols === 1) {
      $(visibleCols.get(0)).append(allItems);
    }
    else {
      var isIndexPage = $('.index-page').length,
        isListingPage = $('.listing-with-images').length,
        col = 0;

      allItems.each(function(index) {
        var imageToAppend = null,
          imageToPrepend = null;;

        // large index page
        if (index === 1 && isIndexPage && totalCols === 3) {
          imageToAppend = '.tall-splash-image.first:visible';
        }
        if (index === 4 && isIndexPage && totalCols === 3) {
          col = 2;
        }

        // large listing page
        if (index === 2 && isListingPage && totalCols === 4) {
          col = 3;
        }
        if (index === 5 && isListingPage && totalCols === 4) {
          imageToPrepend = '.tall-splash-image.first:visible';
        }

        // medium listing page
        if (index === 1 && isListingPage && totalCols === 3) {
          col = 2;
        }
        if (index === 5 && isListingPage && totalCols === 3) {
          col = 1;
        }

        if (index === 2 && isListingPage && totalCols === 3) {
          imageToAppend = '.tall-splash-image.second:visible';
        }

        if (imageToPrepend) {
          $(visibleCols.get(col)).append($(imageToPrepend))
        }
        $(visibleCols.get(col)).append($(this))
        if (imageToAppend) {
          $(visibleCols.get(col)).append($(imageToAppend))
        }
        col = (col + 1) % totalCols;
      });
    }

    $(visibleCols.get(totalCols -1 )).append($('.more-button-container'))
    Foundation.reInit('equalizer');
  }

  function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;

    for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');

      if (sParameterName[0] === sParam) {
        return sParameterName[1] === undefined ? true : sParameterName[1];
      }
    }

    return null;
  };

  $(document).ready(function() {

    $('[data-topics-url]').on('click', topicsGetter);

    $('.main-header-about-link').click(function(e) {
      e.preventDefault();
      $('.main-header-about-slogan').addClass('expanded');
    });

    $('.search-expand').click(function(e) {
      e.preventDefault();
      e.stopPropagation();
      $('.main-header-bottom-nav .top-search').addClass('expanded');

      $('body').off('click').click(function() {
        $('.main-header-bottom-nav .top-search').removeClass('expanded');
      });
    });


    $('.header-logged-in').click(function(e) {
      e.preventDefault();
      $('.main-header-user-dd-menu').addClass('expanded');
    });

    $('.main-header-about-close').click(function(e) {
      e.preventDefault();
      $('.main-header-about-slogan').removeClass('expanded');
    });

    $('.main-header-user-dd-menu-close').click(function(e) {
      e.preventDefault();
      $('.main-header-user-dd-menu').removeClass('expanded');
    });

    $('#toggle-nav, #alt-toggle-nav').click(function(e) {
      e.preventDefault();
      var $sideMenu = $('#side-menu'),
        menuHeight;
      if (Foundation.MediaQuery.atLeast('medium')) {
        menuHeight = $('.main-header-bottom-nav').offset().top;
      }
      else {
        menuHeight = $('.main-content').offset().top;
      }
      $sideMenu.children('.side-menu-top').css('height', menuHeight + 'px');
      $sideMenu.addClass('expanded');
    });

    $('#side-menu-close').click(function(e) {
      e.preventDefault();
      $('#side-menu').removeClass('expanded');
    });

    $('.login-link').on('click', showLogin);
    $('#login-form').on('submit', doLogin);
    $('.follow-link').on('click', doFollowLink);
    $('.unfollow-link').on('click', doUnfollowLink);
    $('.toggle-save').on('click', doToggleSave);

    // toggle arrow on dropdown show/hide
    var prevChevron;

    $('[data-dropdown]').on('show.zf.dropdown', function(ev, $el) {
      var fa = $el.prev().find('.fa'),
        elClass = fa.attr('class');
      if (elClass.indexOf('fa-chevron') > -1) {
        prevChevron = elClass;
        fa.attr('class', 'fa fa-chevron-down');
      }
    });

    $('[data-dropdown]').on('hide.zf.dropdown', function(ev, $el) {
      if (prevChevron) {
        var fa = $el.prev().find('.fa');
        fa.attr('class', prevChevron);
        prevChevron = null;
      }
    });

    $('.alt-header-logged-in a').on('click', function(ev) {
      ev.preventDefault();
    });

    setupSearchForm();

    $('#id_avatar').on('change', function() {
      $('.my-settings-file-description').text($(this).val());
    });

    $('#knowledge-centers-switcher').on('change', function() {
      var $this = $(this);
      if ($this.val()) {
        window.location.href = $this.data('baseUrl') + $this.val() + '/';
      }
    });

    addDynamicCsrfToken();

    var options = {
      modules: {
        speechToText: false
      }
    };

    if (document.dir === 'rtl') {
      options.icon = {
        position: {
          bottom: {size: 50, units: 'px'},
            left: {size: 0, units: 'px'},
            type: 'fixed'
        }
      };
    }

    if (Foundation.MediaQuery.atLeast('large')) {
      // new Accessibility(options);
    }

    if ($(document.body).hasClass('search-page')) {
      var openAdvance = getUrlParameter('adv');
      if (openAdvance) {
        $('.advanced-search-toggle').click();
      }
    }
  });

  reorderElementsOnMediaChange();

  $(window).on('changed.zf.mediaquery', function(event, newSize, oldSize) {
    reorderElementsOnMediaChange(newSize, oldSize);
  });

  $('.advanced-search-link').click(function(e) {
    e.preventDefault();
    var url = $('.top-search').attr('action');
    var params = {q: $('#search').val(), adv: 1};
    window.location.href = url + '?' + $.param(params);
    return false;
  });
})(jQuery);



/**
 * jQuery Formset 1.3-pre
 * @author Stanislaus Madueke (stan DOT madueke AT gmail DOT com)
 * @requires jQuery 1.2.6 or later
 *
 * Copyright (c) 2009, Stanislaus Madueke
 * All rights reserved.
 *
 * Licensed under the New BSD License
 * See: http://www.opensource.org/licenses/bsd-license.php
 */
(function($) {
  $.fn.formset = function(opts)
  {
    var options = $.extend({}, $.fn.formset.defaults, opts),
      flatExtraClasses = options.extraClasses.join(' '),
      totalForms = $('#id_' + options.prefix + '-TOTAL_FORMS'),
      maxForms = $('#id_' + options.prefix + '-MAX_NUM_FORMS'),
      minForms = $('#id_' + options.prefix + '-MIN_NUM_FORMS'),
      childElementSelector = 'input,select,textarea,label,div',
      $$ = $(this),

      applyExtraClasses = function(row, ndx) {
        if (options.extraClasses) {
          row.removeClass(flatExtraClasses);
          row.addClass(options.extraClasses[ndx % options.extraClasses.length]);
        }
      },

      updateElementIndex = function(elem, prefix, ndx) {
        var idRegex = new RegExp(prefix + '-(\\d+|__prefix__)-'),
          replacement = prefix + '-' + ndx + '-';
        if (elem.attr("for")) elem.attr("for", elem.attr("for").replace(idRegex, replacement));
        if (elem.attr('id')) elem.attr('id', elem.attr('id').replace(idRegex, replacement));
        if (elem.attr('name')) elem.attr('name', elem.attr('name').replace(idRegex, replacement));
      },

      hasChildElements = function(row) {
        return row.find(childElementSelector).length > 0;
      },

      showAddButton = function() {
        return maxForms.length == 0 ||   // For Django versions pre 1.2
          (maxForms.val() == '' || (maxForms.val() - totalForms.val() > 0));
      },

      /**
       * Indicates whether delete link(s) can be displayed - when total forms > min forms
       */
      showDeleteLinks = function() {
        return minForms.length == 0 ||   // For Django versions pre 1.7
          (minForms.val() == '' || (totalForms.val() - minForms.val() > 0));
      },

      insertDeleteLink = function(row) {
        var delCssSelector = $.trim(options.deleteCssClass).replace(/\s+/g, '.'),
          addCssSelector = $.trim(options.addCssClass).replace(/\s+/g, '.');
        if (row.is('TR')) {
          // If the forms are laid out in table rows, insert
          // the remove button into the last table cell:
          row.children(':last').append('<a class="' + options.deleteCssClass +'" href="javascript:void(0)">' + options.deleteText + '</a>');
        } else if (row.is('UL') || row.is('OL')) {
          // If they're laid out as an ordered/unordered list,
          // insert an <li> after the last list item:
          row.append('<li><a class="' + options.deleteCssClass + '" href="javascript:void(0)">' + options.deleteText +'</a></li>');
        } else {
          // Otherwise, just insert the remove button as the
          // last child element of the form's container:
          row.append('<a class="' + options.deleteCssClass + '" href="javascript:void(0)">' + options.deleteText +'</a>');
        }
        // Check if we're under the minimum number of forms - not to display delete link at rendering
        if (!showDeleteLinks()){
          row.find('a.' + delCssSelector).hide();
        }

        row.find('a.' + delCssSelector).click(function() {
          var row = $(this).parents('.' + options.formCssClass),
            del = row.find('input:hidden[id $= "-DELETE"]'),
            buttonRow = row.siblings("a." + addCssSelector + ', .' + options.formCssClass + '-add'),
            forms;
          if (del.length) {
            // We're dealing with an inline formset.
            // Rather than remove this form from the DOM, we'll mark it as deleted
            // and hide it, then let Django handle the deleting:
            del.val('on');
            row.hide();
            forms = $('.' + options.formCssClass).not(':hidden');
          } else {
            row.remove();
            // Update the TOTAL_FORMS count:
            forms = $('.' + options.formCssClass).not('.formset-custom-template');
            totalForms.val(forms.length);
          }
          for (var i=0, formCount=forms.length; i<formCount; i++) {
            // Apply `extraClasses` to form rows so they're nicely alternating:
            applyExtraClasses(forms.eq(i), i);
            if (!del.length) {
              // Also update names and IDs for all child controls (if this isn't
              // a delete-able inline formset) so they remain in sequence:
              forms.eq(i).find(childElementSelector).each(function() {
                updateElementIndex($(this), options.prefix, i);
              });
            }
          }
          // Check if we've reached the minimum number of forms - hide all delete link(s)
          if (!showDeleteLinks()){
            $('a.' + delCssSelector).each(function(){$(this).hide();});
          }
          // Check if we need to show the add button:
          if (buttonRow.is(':hidden') && showAddButton()) buttonRow.show();
          // If a post-delete callback was provided, call it with the deleted form:
          if (options.removed) options.removed(row);
          return false;
        });
      };

    $$.each(function(i) {
      var row = $(this),
        del = row.find('input:checkbox[id $= "-DELETE"]');
      if (del.length) {
        // If you specify "can_delete = True" when creating an inline formset,
        // Django adds a checkbox to each form in the formset.
        // Replace the default checkbox with a hidden field:
        if (del.is(':checked')) {
          // If an inline formset containing deleted forms fails validation, make sure
          // we keep the forms hidden (thanks for the bug report and suggested fix Mike)
          del.before('<input type="hidden" name="' + del.attr('name') +'" id="' + del.attr('id') +'" value="on" />');
          row.hide();
        } else {
          del.before('<input type="hidden" name="' + del.attr('name') +'" id="' + del.attr('id') +'" />');
        }
        // Hide any labels associated with the DELETE checkbox:
        $('label[for="' + del.attr('id') + '"]').hide();
        del.remove();
      }
      if (hasChildElements(row)) {
        row.addClass(options.formCssClass);
        if (row.is(':visible')) {
          insertDeleteLink(row);
          applyExtraClasses(row, i);
        }
      }
    });

    if ($$.length) {
      var hideAddButton = !showAddButton(),
        addButton, template;
      if (options.formTemplate) {
        // If a form template was specified, we'll clone it to generate new form instances:
        template = (options.formTemplate instanceof $) ? options.formTemplate : $(options.formTemplate);
        template.removeAttr('id').addClass(options.formCssClass + ' formset-custom-template');
        template.find(childElementSelector).each(function() {
          updateElementIndex($(this), options.prefix, '__prefix__');
        });
        insertDeleteLink(template);
      } else {
        // Otherwise, use the last form in the formset; this works much better if you've got
        // extra (>= 1) forms (thnaks to justhamade for pointing this out):
        template = $('.' + options.formCssClass + ':last').clone(true).removeAttr('id');
        template.find('input:hidden[id $= "-DELETE"]').remove();
        // Clear all cloned fields, except those the user wants to keep (thanks to brunogola for the suggestion):
        template.find(childElementSelector).not(options.keepFieldValues).each(function() {
          var elem = $(this);
          // If this is a checkbox or radiobutton, uncheck it.
          // This fixes Issue 1, reported by Wilson.Andrew.J:
          if (elem.is('input:checkbox') || elem.is('input:radio')) {
            elem.attr('checked', false);
          } else {
            elem.val('');
          }
        });
      }
      // FIXME: Perhaps using $.data would be a better idea?
      options.formTemplate = template;

      if ($$.is('TR')) {
        // If forms are laid out as table rows, insert the
        // "add" button in a new table row:
        var numCols = $$.eq(0).children().length,   // This is a bit of an assumption :|
          buttonRow = $('<tr><td colspan="' + numCols + '"><a class="' + options.addCssClass + '" href="javascript:void(0)">' + options.addText + '</a></tr>')
            .addClass(options.formCssClass + '-add');
        $$.parent().append(buttonRow);
        if (hideAddButton) buttonRow.hide();
        addButton = buttonRow.find('a');
      } else {
        // Otherwise, insert it immediately after the last form:
        $$.filter(':last').after('<a class="' + options.addCssClass + '" href="javascript:void(0)">' + options.addText + '</a>');
        addButton = $$.filter(':last').next();
        if (hideAddButton) addButton.hide();
      }
      addButton.click(function() {
        var formCount = parseInt(totalForms.val()),
          row = options.formTemplate.clone(true).removeClass('formset-custom-template'),
          buttonRow = $($(this).parents('tr.' + options.formCssClass + '-add').get(0) || this)
        delCssSelector = $.trim(options.deleteCssClass).replace(/\s+/g, '.');
        applyExtraClasses(row, formCount);
        row.insertBefore(buttonRow).show();
        row.find(childElementSelector).each(function() {
          updateElementIndex($(this), options.prefix, formCount);
        });
        totalForms.val(formCount + 1);
        // Check if we're above the minimum allowed number of forms -> show all delete link(s)
        if (showDeleteLinks()){
          $('a.' + delCssSelector).each(function(){$(this).show();});
        }
        // Check if we've exceeded the maximum allowed number of forms:
        if (!showAddButton()) buttonRow.hide();
        // If a post-add callback was supplied, call it with the added form:
        if (options.added) options.added(row);
        return false;
      });
    }

    return $$;
  };

  /* Setup plugin defaults */
  $.fn.formset.defaults = {
    prefix: 'form',                  // The form prefix for your django formset
    formTemplate: null,              // The jQuery selection cloned to generate new form instances
    addText: 'add another',          // Text for the add link
    deleteText: 'remove',            // Text for the delete link
    addCssClass: 'add-row',          // CSS class applied to the add link
    deleteCssClass: 'delete-row',    // CSS class applied to the delete link
    formCssClass: 'dynamic-form',    // CSS class applied to each form in a formset
    extraClasses: [],                // Additional CSS classes, which will be applied to each form in turn
    keepFieldValues: '',             // jQuery selector for fields whose values should be kept when the form is cloned
    added: null,                     // Function called each time a new form is added
    removed: null                    // Function called each time a form is deleted
  };
})(jQuery);
