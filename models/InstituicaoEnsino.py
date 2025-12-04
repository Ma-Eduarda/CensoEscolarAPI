from marshmallow import Schema, fields, validate
from flask_restful import fields as flaskFields

instituicao_fields = {
    'id': flaskFields.Integer,
    'nu_ano_censo': flaskFields.Integer,
    'no_entidade': flaskFields.String,
    'co_entidade': flaskFields.Integer,
    'no_uf': flaskFields.String,
    'sg_uf': flaskFields.String,
    'co_uf': flaskFields.Integer,
    'no_municipio': flaskFields.String,
    'co_municipio': flaskFields.Integer,
    'no_mesorregiao': flaskFields.String,
    'co_mesorregiao': flaskFields.Integer,
    'no_microrregiao': flaskFields.String,
    'co_microrregiao': flaskFields.Integer,
    'no_regiao': flaskFields.String,
    'co_regiao': flaskFields.Integer,
    'qt_mat_bas': flaskFields.Integer,
    'qt_mat_prof': flaskFields.Integer,
    'qt_mat_eja': flaskFields.Integer,
    'qt_mat_esp': flaskFields.Integer,
    'qt_mat_fund': flaskFields.Integer,
    'qt_mat_inf': flaskFields.Integer,
    'qt_mat_med': flaskFields.Integer,
    'qt_mat_zr_na': flaskFields.Integer,
    'qt_mat_zr_rur': flaskFields.Integer,
    'qt_mat_zr_urb': flaskFields.Integer,
    'qt_mat_total': flaskFields.Integer,
}

class InstituicaoEnsino():
    def __init__(self, id, nu_ano_censo, no_entidade, co_entidade, no_uf, sg_uf, co_uf,
                no_municipio, co_municipio, no_mesorregiao, co_mesorregiao,
                no_microrregiao, co_microrregiao, no_regiao, co_regiao,
                qt_mat_bas, qt_mat_prof, qt_mat_eja, qt_mat_esp,
                qt_mat_fund, qt_mat_inf, qt_mat_med,
                qt_mat_zr_na, qt_mat_zr_rur, qt_mat_zr_urb, qt_mat_total):

        self.id = id
        self.nu_ano_censo = nu_ano_censo
        self.no_entidade = no_entidade
        self.co_entidade = co_entidade
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_uf = co_uf
        self.no_municipio = no_municipio
        self.co_municipio = co_municipio
        self.no_mesorregiao = no_mesorregiao
        self.co_mesorregiao = co_mesorregiao
        self.no_microrregiao = no_microrregiao
        self.co_microrregiao = co_microrregiao
        self.no_regiao = no_regiao
        self.co_regiao = co_regiao
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_med = qt_mat_med
        self.qt_mat_zr_na = qt_mat_zr_na
        self.qt_mat_zr_rur = qt_mat_zr_rur
        self.qt_mat_zr_urb = qt_mat_zr_urb
        self.qt_mat_total = qt_mat_total


class InstituicaoEnsinoSchema(Schema):
    nu_ano_censo = fields.Integer(required=True)
    no_entidade = fields.String(validate=validate.Length(min=2, max=100),required=True,error_messages={"required": "Nome da Entidade é obrigatório."})
    co_entidade = fields.Integer(required=True, error_messages={"required": "Código da Entidade é obrigatório."})

    no_uf = fields.String(required=True)
    sg_uf = fields.String(validate=validate.Length(equal=2), required=True)
    co_uf = fields.Integer(required=True)

    no_municipio = fields.String(required=True)
    co_municipio = fields.Integer(required=True)

    no_mesorregiao = fields.String(required=True)
    co_mesorregiao = fields.Integer(required=True)

    no_microrregiao = fields.String(required=True)
    co_microrregiao = fields.Integer(required=True)
    
    no_regiao = fields.String(required=True)
    co_regiao = fields.Integer(required=True)

    qt_mat_bas = fields.Integer(required=True)
    qt_mat_prof = fields.Integer(required=True)
    qt_mat_eja = fields.Integer(required=True)
    qt_mat_esp = fields.Integer(required=True)
    qt_mat_fund = fields.Integer(required=True)
    qt_mat_inf = fields.Integer(required=True)
    qt_mat_med = fields.Integer(required=True)
    qt_mat_zr_na = fields.Integer(required=True)
    qt_mat_zr_rur = fields.Integer(required=True)
    qt_mat_zr_urb = fields.Integer(required=True)