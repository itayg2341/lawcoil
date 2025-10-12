from django.utils.translation import get_language


def bidi(request):
    """
    Context processor that provides BiDi (Bidirectional) language information.
    Replacement for the removed bidiutils.context_processors.bidi package.
    """
    language = get_language() or 'he'
    
    # Hebrew is RTL, English is LTR
    is_rtl = language == 'he'
    
    return {
        'LANGUAGE_DIRECTION': 'rtl' if is_rtl else 'ltr',
        'LANGUAGE_START': 'right' if is_rtl else 'left',
        'LANGUAGE_END': 'left' if is_rtl else 'right',
        'LANGUAGE_BIDI': is_rtl,
        'LANGUAGE_MARKER': ' ' if is_rtl else '',  # Used in templates for spacing
    }