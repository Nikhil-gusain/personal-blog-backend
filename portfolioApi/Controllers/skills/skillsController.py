
from PortfolioBackend.Utils.ResponseMessages import RESPONSE_MESSAGES
from PortfolioBackend.Utils.ResponseCodes import RESPONSE_CODES
from PortfolioBackend.Utils.ResponseBack import LocalResponse
from PortfolioBackend.Utils.Names import NAMES
from .Tasks.skillsTasks import SKILLS_TASKS
from .Validators.skillsValidators import SKILLS_VALIDATORS

from portfolioApi.models import Skills,SkillSection

class SKILLS_CONTROLLER:
    
    @classmethod
    def GetAllSkillsData(self):
        try:
            skills = Skills.objects.all()
            skilldata=[SKILLS_TASKS.GetSkillsData(skill) for skill in skills]
            return LocalResponse(
                message=RESPONSE_MESSAGES.SKILLS_FETCHED_SUCCESSFULLY,
                data=skilldata,
                code=RESPONSE_CODES.SUCCESS
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.SKILLS_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )

    @classmethod
    def GetSkillSection(self):
        try:
            skillsection = SkillSection.objects.first()
            skillsData=[SKILLS_TASKS.GetSkillsData(skill) for skill in skillsection.skills.all()]
            sectionData= {
                NAMES.TITLE:skillsection.sectionTitle,
                NAMES.INTRO:skillsection.intro,
                NAMES.SKILLS:skillsData
            }
            return LocalResponse(
                message=RESPONSE_MESSAGES.SKILLS_FETCHED_SUCCESSFULLY,
                data=sectionData,
                code=RESPONSE_CODES.SUCCESS
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.SKILLS_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )       