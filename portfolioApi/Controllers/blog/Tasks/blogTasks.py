from portfolioApi.models import Blogs
from PortfolioBackend.Utils.Names import NAMES
class BLOG_TASKS:
    
    @classmethod
    def GetBlog(self,blog:Blogs):
        try:
            return Blogs.objects.get(id=blog.id)
        except Blogs.DoesNotExist:
            return None
        except Exception as e:
            return None
    
    @classmethod
    def GetBlogsForShowApi(self,blog:Blogs):
        try:
            blogdata={
                NAMES.TITLE:blog.title,
                NAMES.EXCERPT:blog.excerpt,
                NAMES.COVER_IMAGE:blog.coverImage,
                NAMES.CREATED_AT:blog.createdAt,
                NAMES.READ_MIN:blog.readMin,
                NAMES.CATEGORY:blog.category.name
            }
            return True,blogdata
        except Exception as e:
            return None,str(e)