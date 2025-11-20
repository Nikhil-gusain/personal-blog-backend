from portfolioApi.models import Skills
from PortfolioBackend.Utils.Names import NAMES
class SKILLS_TASKS:
    
    @classmethod
    def GetSkillsData(self,skill:Skills):
        try:
            skilldata={
                NAMES.ID:skill.id,
                NAMES.NAME:skill.name,
                NAMES.PERCENT:skill.percent
            }
            return True,skilldata
        except Exception as e:
            return None,str(e)
    
                            