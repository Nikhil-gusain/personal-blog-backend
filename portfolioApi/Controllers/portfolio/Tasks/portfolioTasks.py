from portfolioApi.models import About,Services,SocialLinks,ContactSection
from PortfolioBackend.Utils.Names import NAMES
import json
class PORTFOLIO_TASKS:
    
    @classmethod
    def GetAboutData(self,about:About):
        try:
            aboutData={
                NAMES.ID:about.id,
                NAMES.TITLE:about.sectionTitle,
                NAMES.NAME:about.name,
                NAMES.DESIGNATION:about.designation,
                NAMES.BIO:about.bio,
                NAMES.PROFILE_IMAGE:about.profileImage,
                NAMES.DETAILS:about.details,
                NAMES.CV_LINK:about.cvLink
            }
            return True,aboutData
        except Exception as e:
            return None,str(e)
    
    @classmethod
    def GetServicesData(self,service:Services):
        try:
            serviceData={
                NAMES.ID:service.id,
                NAMES.TITLE:service.title,
                NAMES.DESCRIPTION:service.description,
                NAMES.ICON:service.icon,
                NAMES.AUTHOR:service.author.username,
                NAMES.CREATED_AT:service.createdAt
            }
            return True,serviceData
        except Exception as e:
            return None,str(e)
    
    @classmethod
    def GetSocialData(self,social:SocialLinks):
        try:
            socialData={
                NAMES.ID:social.id,
                NAMES.ICON:social.icon,
                NAMES.URL:social.url
            }
            return True,socialData
        except Exception as e:
            return None,str(e)

    @classmethod
    def GetContactData(self,contact:ContactSection):
        try:
            socialData:list = []
            for social in contact.socialLinks.all():
                status,socialresp=self.GetSocialData(social)
                if status:
                    socialData.append(socialresp)
            contactData={
                NAMES.ID:contact.id,
                NAMES.TITLE:contact.title,
                NAMES.INFO:contact.info,
                NAMES.SOCIAL_LINKS:socialData
            }
            return True,contactData
        except Exception as e:
            return None,str(e)