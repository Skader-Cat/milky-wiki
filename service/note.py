from sqlalchemy import select, insert

from models.tables import User
from models.tables.article import Article
from models.tables.project import Project
from service.base import Manager


class ArticleManager(Manager):
    def __init__(self, db):
        super().__init__(db)
    db = None

    async def get_articles(self, project_id):
        stmt = select(Article).where(Article.project_id == project_id)
        return await self.db.fetch_all(stmt)

    async def get_article(self, article_id):
        stmt = select(Article).where(Article.id == article_id)
        return await self.db.fetch_one(stmt)

    async def create_article(self, article):
        stmt = insert(Article).values(**article.dict())
        return await self.db.execute(stmt)

    async def update_article(self, article_id, article):
        stmt = (
            Article.update()
            .where(Article.id == article_id)
            .values(**article.dict(exclude_unset=True))
        )
        return await self.db.execute(stmt)

    async def delete_article(self, article_id):
        stmt = Article.delete().where(Article.id == article_id)
        return await self.db.execute(stmt)