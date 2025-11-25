
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
            skilldata:list=[]
            for skill in skills:
                status,skillresp=SKILLS_TASKS.GetSkillsData(skill)
                if status:
                    skilldata.append(skillresp)
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
            skillResp = self.GetAllSkillsData()
            skillsData=skillResp.data
            sectionData= {
                NAMES.TITLE:skillsection.sectionTitle,
                NAMES.INTRO:skillsection.intro,
                NAMES.SKILLS:skillsData if skillResp.code==RESPONSE_CODES.SUCCESS else [] 
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