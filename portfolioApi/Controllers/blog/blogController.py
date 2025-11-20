
from PortfolioBackend.Utils.ResponseMessages import RESPONSE_MESSAGES
from PortfolioBackend.Utils.ResponseCodes import RESPONSE_CODES
from PortfolioBackend.Utils.ResponseBack import LocalResponse
from .Tasks.blogTasks import BLOG_TASKS
from .Validators.blogValidators import BLOG_VALIDATORS
from portfolioApi.models import Blogs

class BLOG_CONTROLLER:

    @classmethod
    def GetBlogsforApi(self):
        try:
            blogs = Blogs.objects.all().order_by('-createdAt')[:6]
            blogdata=[BLOG_TASKS.GetBlogsForShowApi(blog) for blog in blogs]
            return LocalResponse(
                message=RESPONSE_MESSAGES.BLOG_FETCHED_SUCCESSFULLY,
                data=blogdata,
                code=RESPONSE_CODES.SUCCESS
            )
        except Exception as e:
            return LocalResponse(
                message=RESPONSE_MESSAGES.BLOG_FETCHED_ERROR,
                data=str(e),
                code=RESPONSE_CODES.ERROR
            )
    
                            