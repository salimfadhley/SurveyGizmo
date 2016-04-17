
from surveygizmo.api import base


class SurveyOption(base.Resource):
    resource_fmt_str = 'survey/%(survey_id)s/surveyquestion/%(question_id)s/surveyoption/%(option_id)s'
    resource_id_keys = ['survey_id', 'quesiton_id']

    def list(self, survey_id, question_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
        })
        return super(SurveyOption, self).list(**kwargs)

    def get(self, survey_id, question_id, option_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
            'option_id': option_id,
        })
        return super(SurveyOption, self).get(**kwargs)

    def create(self, survey_id, question_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
        })
        return super(SurveyOption, self).create(**kwargs)

    def update(self, survey_id, question_id, option_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
            'option_id': option_id,
        })
        return super(SurveyOption, self).update(**kwargs)

    def copy(self, **kwargs):
        raise NotImplementedError()

    def delete(self, survey_id, question_id, option_id, **kwargs):
        kwargs.update({
            'survey_id': survey_id,
            'question_id': question_id,
            'option_id': option_id,
        })
        return super(SurveyOption, self).delete(**kwargs)
