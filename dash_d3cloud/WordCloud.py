# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WordCloud(Component):
    """A WordCloud component.


Keyword arguments:
- id (string; optional)
- words (list; optional)
- options (optional): . options has the following type: dict containing keys 'fontStyle', 'fontSizes', 'colors', 'enableTooltip', 'deterministic', 'fontFamily', 'fontWeight', 'rotations', 'rotationAngles', 'padding', 'scale', 'spiral', 'transitionDuration'.
Those keys have the following types:
  - fontStyle (string; optional)
  - fontSizes (list; optional)
  - colors (list; optional)
  - enableTooltip (boolean; optional)
  - deterministic (boolean; optional)
  - fontFamily (string; optional)
  - fontWeight (string; optional)
  - rotations (number; optional)
  - rotationAngles (list; optional)
  - padding (number; optional)
  - scale (string; optional)
  - spiral (string; optional)
  - transitionDuration (number; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, words=Component.UNDEFINED, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'words', 'options']
        self._type = 'WordCloud'
        self._namespace = 'dash_d3cloud'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'words', 'options']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WordCloud, self).__init__(**args)
