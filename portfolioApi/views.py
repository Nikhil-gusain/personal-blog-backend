from django.shortcuts import render
from .Controllers.portfolio.portfolioController import PORTFOLIO_CONTROLLER
from .Controllers.blog.blogController import BLOG_CONTROLLER
from .Controllers.skills.skillsController import SKILLS_CONTROLLER
from rest_framework.decorators import api_view

from PortfolioBackend.Utils.ResponseBack import ServerResponse
from PortfolioBackend.Utils.ResponseCodes import RESPONSE_CODES
from PortfolioBackend.Utils.ResponseMessages import RESPONSE_MESSAGES


@api_view(['GET'])
def GetServiceSectionView(request)->ServerResponse:
    try:
        serviceResp= PORTFOLIO_CONTROLLER.GetServiceSection()
        return ServerResponse(
            message=serviceResp.message,
            data=serviceResp.data,
            code=serviceResp.code
        )
    except Exception as e:
        return ServerResponse(
            message=RESPONSE_MESSAGES.SERVICES_FETCHED_ERROR,
            data=str(e),
            code=RESPONSE_CODES.ERROR
        )
    

@api_view(['GET'])
def GetAboutSectionView(request)->ServerResponse:
    try:
        aboutResp= PORTFOLIO_CONTROLLER.GetAboutData()
        return ServerResponse(
            message=aboutResp.message,
            data=aboutResp.data,
            code=aboutResp.code
        )
    except Exception as e:
        return ServerResponse(
            message=RESPONSE_MESSAGES.ABOUT_FETCHED_ERROR,
            data=str(e),
            code=RESPONSE_CODES.ERROR
        )


@api_view(['GET'])
def GetSkillSectionView(request)->ServerResponse:
    try:
        skillResp= SKILLS_CONTROLLER.GetSkillSection()
        return ServerResponse(
            message=skillResp.message,
            data=skillResp.data,
            code=skillResp.code
        )
    except Exception as e:
        return ServerResponse(
            message=RESPONSE_MESSAGES.SKILLS_FETCHED_ERROR,
            data=str(e),
            code=RESPONSE_CODES.ERROR
        )


@api_view(['GET'])
def GetContactSectionView(request)->ServerResponse:
    try:
        contactResp= PORTFOLIO_CONTROLLER.GetContactSection()
        return ServerResponse(
            message=contactResp.message,
            data=contactResp.data,
            code=contactResp.code
        )
    except Exception as e:
        return ServerResponse(
            message=RESPONSE_MESSAGES.CONTACT_FETCHED_ERROR,
            data=str(e),
            code=RESPONSE_CODES.ERROR
        )


@api_view(['GET'])
def GetBlogsforApiView(request)->ServerResponse:
    try:
        blogResp= BLOG_CONTROLLER.GetBlogsforApi()
        return ServerResponse(
            message=blogResp.message,
            data=blogResp.data,
            code=blogResp.code
        )
    except Exception as e:
        return ServerResponse(
            message=RESPONSE_MESSAGES.BLOG_FETCHED_ERROR,
            data=str(e),
            code=RESPONSE_CODES.ERROR
        )