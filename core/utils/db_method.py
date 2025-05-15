from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import db_config
from core.utils import constant_variable


from sqlalchemy.future import select
from sqlalchemy import update, delete

getdb = db_config.session_factory()


class DataBaseMethod:
    """This class provides the database methods"""

    def __init__(self, model):
        self.model = model

    async def save(self, validate_data, db: AsyncSession = Depends(getdb)):
        try:
            db.add(validate_data)
            await db.flush()
            await db.commit()## 
            await db.refresh(validate_data)  
            return constant_variable.STATUS_TRUE 
            #return validate_data
        except Exception as err:
            print(err)
            await db.rollback()
            return None  


    async def save_all(self, validate_data: list, db: AsyncSession = Depends(getdb)):
        try:
            db.add_all(validate_data)
            await db.flush()         # Corrected to await
            for data in validate_data:
                await db.refresh(data)  # Corrected to await
            return validate_data
        except Exception as err:
            print(err)
            await db.rollback()     # Corrected to await
            await db.close()        # Corrected to await
            return constant_variable.STATUS_FALSE

    async def bulk_insert_mapping(self, validate_data: dict, db: AsyncSession = Depends(getdb)):
        try:
            await db.bulk_insert_mappings(self.model, validate_data)  # Corrected to await
            return constant_variable.STATUS_TRUE
        except Exception as err:
            print(err)
            await db.rollback()     # Corrected to await
            await db.close()        # Corrected to await
            return constant_variable.STATUS_FALSE

    async def destroy(self, instance: object, db: AsyncSession = Depends(getdb)):
        try:
            await db.delete(instance)  # Corrected to await
            await db.flush()          # Corrected to await
            await db.refresh(instance)  # Corrected to await
            return constant_variable.STATUS_TRUE
        except Exception as e:
            print(e)
            await db.rollback()      # Corrected to await
            return constant_variable.STATUS_FALSE
        
    async def get_all(self, db: AsyncSession):
        """
        Get all records from a table
        """
        query = select(self.model)
        result = await db.execute(query)
        return result.scalars().all()
    
    async def get_by_id(self, db: AsyncSession, id: int):
        """
        Get a record by ID
        """
        query = select(self.model).where(self.model.id == id)
        result = await db.execute(query)
        return result.scalars().first()
    
    async def update(self, db: AsyncSession, id: int, **kwargs):
        """
        Update a record by ID
        """
        stmt = update(self.model).where(self.model.id == id).values(**kwargs)
        await db.execute(stmt)
        await db.commit()
        return await self.get_by_id(db, id)
    
    async def delete(self, db: AsyncSession, id: int):
        """
        Delete a record by ID.
        """
        obj = await self.get_by_id(db, id)
        if not obj:
            return None 

        stmt = delete(self.model).where(self.model.id == id)
        await db.execute(stmt)
        await db.commit()
        
        return obj 

    
    async def filter_by(self, db: AsyncSession, **kwargs):
        """
        Filter records by keyword arguments
        """
        query = select(self.model)
        for key, value in kwargs.items():
            attribute = getattr(self.model, key)
            query = query.where(attribute == value)
        
        result = await db.execute(query)
        return result.scalars().all()    