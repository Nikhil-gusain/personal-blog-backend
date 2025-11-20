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
                NAMES.DETAILS:json.loads(about.details.replace("'",'"')),
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
                NAMES.AUTHOR:service.author,
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
            contactData={
                NAMES.ID:contact.id,
                NAMES.TITLE:contact.title,
                NAMES.INFO:json.loads(contact.info.replace("'",'"')),
                NAMES.SOCIAL_LINKS:[self.GetSocialData(social) for social in contact.socialLinks.all()]
            }
            return True,contactData
        except Exception as e:
            return None,str(e)