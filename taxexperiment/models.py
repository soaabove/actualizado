from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import itertools
import random

class Constants(BaseConstants):
    name_in_url = 'taxexperiment'
    players_per_group = None
    num_rounds = 1
    turno = [1, 2]


class Subsession(BaseSubsession):
    def creating_session(self):
        turnos = Constants.turno.copy()
        random.shuffle(turnos)
        turnojugador = itertools.cycle(turnos)
        for p in self.get_players():
            p.turnodeljugador = next(turnojugador)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    turnodeljugador = models.IntegerField()

    pregconsen = models.IntegerField(
        choices=[[1, 'Sí acepto'], [2, 'No acepto']],
        label= '¿Acepto que se comuniquen conmigo?',
        widget=widgets.RadioSelectHorizontal,
    )

    edad = models.IntegerField(label='1. ¿Cuál es tu edad?', min=18, max=100,
    )

    sexo = models.IntegerField(
        choices=[[0, 'Mujer'], [1, 'Hombre']],
        label='2. ¿Cuál es tu sexo?',
        widget=widgets.RadioSelect,
    )

    zona = models.IntegerField(
        choices=[[1, 'José Carlos Mariátegui'], [2, 'Cercado'], [3, 'Inca Pachacútec'], [4, 'Nueva Esperanza'], [5, 'Tablada de Lurín'], [6, 'José Gálvez'], [7, 'Nuevo Milenio']],
        label='3. ¿Zona de residencia?',

    )

    hogares = models.IntegerField(
        choices=[[0, 'Solo mi hogar'], [1, '1 hogar más'], [2, '2 hogares más'], [3, '3 hogares a más']],
        label='4. ¿Cuántos hogares (familias) se encuentran en su predio (vivienda)?',
        widget=widgets.RadioSelect,
    )

    miembros = models.IntegerField(label='5. Generalmente, ¿cuántos miembros se encuentran en su hogar?', min=1, max=50)

    ocupacion = models.IntegerField(
        choices=[[1, 'Empleador o patrono'], [2, 'Trabajador independiente'], [3, 'Empleado'], [4, 'Obrero'], [5, 'Trabajador familiar no remunerado'], [6, 'Trabajador del hogar'], [7, 'Otro']],
        label='5. ¿Usted se desempeña en su ocupación principal o negocio como?',
    )

    escolaridad = models.IntegerField(
        choices=[[1, 'Sin nivel'], [2, 'Educación inicial'], [3, 'Primaria incompleta'], [4, 'Primaria completa'], [5, 'Secundaria incompleta'], [6, 'Secundaria completa'], [7, 'Superior no universitaria incompleta'], [8, 'Superior no universitaria completa'], [9, 'Superior universitaria incompleta'], [10, 'Superior universitaria completa'], [11, 'Maestría/Doctorado']],
        label='6. ¿Cuál es el último año o grado de estudio cursado?',
    )
    ingresofamiliar = models.IntegerField(label='7. En general, ¿cuánto dinero en total recibe (en S/.) de los miembros del hogar para el pago del concepto de autovalúo (impuesto predial?', min=0, max=10000)

    montoanualpredio = models.IntegerField(label= '8. Generalmente en el predio que reside, ¿cuánto paga "anualmente" por el concepto de autovalúo (impuesto predial)?', min=50, max=2000)

    comprension = models.IntegerField(min=2, max=2,
        choices=[[1, 'Responder preguntas sobre mi personalidad y mi vida diaria'], [2, 'Responder acerca de mis decisiones diarias ante situaciones económicas con S/.50.00.'], [3, 'Responder sobre situaciones económicas de mi vida diaria con S/. 30.00.']],
        label= 'Marque la opción correcta',
        widget=widgets.RadioSelect,
    )

    dificultad = models.IntegerField(
        choices=[[1, 'Sencilla'], [2, 'Normal'], [3, 'Dificil']],
        label= '1. ¿Considera a la plataforma como?',
        widget=widgets.RadioSelectHorizontal
    )
    comentario = models.LongStringField(blank=True,
         label= '8. ¿Tiene algún comentario? (Responder es opcional)')

    conocimientodes = models.IntegerField(
        choices=[[1, 'Sí'], [2, 'Tal vez'], [3, 'No']],
        label= '2. ¿Usted consideraba que el 70% de vecinos participante de su distrito cumplió con el pago de la contribución?',
        widget=widgets.RadioSelectHorizontal
    )

    conocimientopres = models.IntegerField(
        choices=[[1, 'Sí'], [2, 'Tal vez'], [3, 'No']],
        label='3. ¿Usted creía que pagar una contribución es un deber cívico y la organización ha iniciado procesos coactivos en el 68% de participantes incumplidores?',
        widget=widgets.RadioSelectHorizontal
    )

    causa = models.IntegerField(
        choices=[[1, 'Falta de dinero'], [2, 'Olvido'], [3, 'Lejanía del local de pago'],
                 [4, 'Desconocimiento en cómo pagar'], [5, 'Ninguna, siempre pago']],
        label='4. ¿A qué se debe el incumplimiento del pago del impuesto predial?',
        widget=widgets.RadioSelect
    )

    corrupcion = models.IntegerField(
        choices=[[1, 'Totalmente en desacuerdo'], [2, 'En desacuerdo'], [3, 'Ni en desacuerdo/Ni en acuerdo'], [4, 'En acuerdo'], [5, 'Totalmente de acuerdo']],
        label= '5. Con respecto a la corrupción, ¿usted considera al gobierno peruano como un país corrupto?',
        widget=widgets.RadioSelectHorizontal
    )

    confianza = models.IntegerField(
        choices=[[1, 'Nada'], [2, 'Poco'], [3, 'Suficiente'], [4, 'Bastante'], [5, 'No sé']],
        label= '6. Actualmente, ¿tiene usted confianza en su institución "Municipalidad distrital de V. M. T"?',
        widget=widgets.RadioSelectHorizontal
    )

    eficiencia = models.IntegerField(
        choices=[[1, 'Muy malo'], [2, 'Malo'], [3, 'No sé'], [4, 'Bueno'], [5, 'Muy bueno']],
        label='7. En su opinión, la gestión de la "Municipalidad distrital de V. M. T" es:',
        widget=widgets.RadioSelectHorizontal
    )

    acepta1 = models.StringField(
        choices=['No', 'Si'], widget=widgets.RadioSelectHorizontal, )

    acepta2 = models.StringField(
        choices=['No', 'Si'], widget=widgets.RadioSelectHorizontal, )

    acepta3 = models.StringField(
        choices=['No', 'Si'], widget=widgets.RadioSelectHorizontal, )

    acepta4 = models.StringField(
        choices=['No', 'Si'], widget=widgets.RadioSelectHorizontal, )

    pexp1 = models.IntegerField(
        choices=[[1, 'Si'], [2, 'No'], [3, 'No sé']],
        label='1. En los últimos 6 meses, ¿suele gastar más de lo planificado en actividades recreativas como paseo familiar, ir al cine, ir de compras, entre otros?',
        widget=widgets.RadioSelectHorizontal
    )

    pexp2 = models.IntegerField(
        choices=[[1, 'Nada'], [2, 'Poca'], [3, 'No sé'], [4, 'Suficiente'], [5, 'Bastante']],
        label='2. ¿Cuánto confía en su anterior respuesta dada?',
        widget=widgets.RadioSelectHorizontal
    )

    pexp3 = models.IntegerField(
        choices=[[1, 'Nada'], [2, 'Poco'], [3, 'No sé'], [4, 'Suficiente'], [5, 'Bastante']],
        label='3. Usted al poseer el recibo de luz, agua u otro recibo, ¿suele leer los detalles escritos además del monto mensual del pago?',
        widget=widgets.RadioSelectHorizontal
    )

    pexp4 = models.IntegerField(
        choices=[[1, 'Nada'], [2, 'Poco'], [3, 'No sé'], [4, 'Suficiente'], [5, 'Bastante']],
        label='4. Usted al poseer el recibo de luz, agua u otro recibo, ¿suele ver los gráficos además del monto mensual del pago?',
        widget=widgets.RadioSelectHorizontal
    )

    pexp5 = models.IntegerField(
        choices=[[1, 'Sí'], [2, 'No'], [3, 'No sé']],
        label='5. ¿Se identifica con la frase “Más vale guardar pan para mayo"?',
        widget=widgets.RadioSelectHorizontal
    )


    montototal = models.FloatField(
        label='Monto que desea contribuir:',
        min=2, max=6,
    )