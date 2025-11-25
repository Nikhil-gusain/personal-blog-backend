
from PortfolioBackend.Utils.ResponseMessages import RESPONSE_MESSAGES
from PortfolioBackend.Utils.ResponseCodes import RESPONSE_CODES
from PortfolioBackend.Utils.ResponseBack import LocalResponse
from .Tasks.portfolioTasks import PORTFOLIO_TASKS
from .Validators.portfolioValidators import PORTFOLIO_VALIDATORS
from PortfolioBackend.Utils.Names import NAMES
from portfolioApi.models import About,ServiceSection,ContactSection

class PORTFOLIO_CONTROLLER:

    @classmethod
    def GetAboutData(self):
        try:
            about = About.objects.first()
            status,aboutData=PORTFOLIO_TASKS.GetAboutData(about)
            if status:
                return LocalResponse(
                    message=RESPONSE_MESSAGES.ABOUT_FETCHED_SUCCESSFULLY,
                    data=aboutData,
                    code=RESPONSE_CODES.SUCCESS
                )
            return LocalResponse(
                message=RESPONSE_MESSAGES.ABOUT_FETCHED_ERROR,
                data=aboutData,
                code=RESPONSE_CODES.ERROR
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.ABOUT_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )
        
    @classmethod
    def GetServiceSection(self):
        try:
            serviceSection = ServiceSection.objects.first()
            servicesData=[]
            for service in serviceSection.services.all():
                status,serviceResp=PORTFOLIO_TASKS.GetServicesData(service)
                if status:
                    servicesData.append(serviceResp)
            sectionData= {
                NAMES.TITLE:serviceSection.title,
                NAMES.SUBTITLE:serviceSection.subtitle,
                NAMES.SERVICES:servicesData
            }
            if status:
                return LocalResponse(
                    message=RESPONSE_MESSAGES.SERVICES_FETCHED_SUCCESSFULLY,
                    data=sectionData,
                    code=RESPONSE_CODES.SUCCESS
                )
            return LocalResponse(
                message=RESPONSE_MESSAGES.SERVICES_FETCHED_ERROR,
                data=servicesData,
                code=RESPONSE_CODES.ERROR
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.SERVICES_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )
    @classmethod
    def GetContactSection(self):
        try:
            contactSection = ContactSection.objects.first()
            status,contactData=PORTFOLIO_TASKS.GetContactData(contactSection)
            if status:
                return LocalResponse(
                    message=RESPONSE_MESSAGES.CONTACT_FETCHED_SUCCESSFULLY,
                    data=contactData,
                    code=RESPONSE_CODES.SUCCESS
                )
            return LocalResponse(
                message=RESPONSE_MESSAGES.CONTACT_FETCHED_ERROR,
                data=contactData,
                code=RESPONSE_CODES.ERROR
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.CONTACT_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )
                            