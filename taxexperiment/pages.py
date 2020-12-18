from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Encuesta(Page):
    form_model = 'player'
    form_fields = ['edad', 'sexo', 'zona', 'hogares', 'miembros', 'ocupacion', 'escolaridad', 'ingresofamiliar', 'montoanualpredio']
class Consentimientoinformado(Page):
    form_model = 'player'
    form_fields = ['pregconsen', 'acepta1']

class Instrucciones(Page):
    pass

class Preguntadecomprension(Page):
    form_model = 'player'
    form_fields = ['comprension']

class Agradecimientonoacepto(Page):
    def is_displayed(self):
        return self.player.acepta1 == "No"

class Exp1(Page):
    form_model = 'player'
    form_fields = ['pexp1', 'pexp2']

class Exp2(Page):
    form_model = 'player'
    form_fields = ['pexp3']

class Exp3(Page):
    form_model = 'player'
    form_fields = ['pexp4']

class Exp4(Page):
        form_model = 'player'
        form_fields = ['pexp5']


class Comunicymsjtradic(Page):
    form_model = 'player'
    form_fields = ['acepta2']

class Mensajedescriptivo(Page):
    form_model = 'player'
    form_fields = ['acepta3']
    def is_displayed(self):
        return self.player.acepta2 == "No"

class Mensajeprescriptivo(Page):
    form_model = 'player'
    form_fields = ['acepta4']
    def is_displayed(self):
        return self.player.acepta3 == "No"

class Cantidaddemonto(Page):
    form_model = 'player'
    form_fields = ['montototal']
    def is_displayed(self):
        return self.player.acepta3 == "Si" or self.player.acepta2 == "Si" or self.player.acepta4 == "Si"

class Encuestapost(Page):
    form_model = 'player'
    form_fields = ['dificultad', 'conocimientodes', 'conocimientopres', 'causa', 'corrupcion', 'confianza', 'eficiencia', 'comentario']

class Agradecimientofinal(Page):
    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

page_sequence = [Consentimientoinformado, Agradecimientonoacepto, Encuesta, Instrucciones, Preguntadecomprension, Exp1, Exp2, Exp3, Exp4, Comunicymsjtradic, Mensajedescriptivo, Mensajeprescriptivo, Cantidaddemonto, Encuestapost, Agradecimientofinal]
