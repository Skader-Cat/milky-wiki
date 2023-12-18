


class ProjectManager():
    db = None

    @classmethod
    async def _execute_query(cls, query):
        async with cls.db as session:
            result = await session.execute(query)
            await session.commit()
            return result