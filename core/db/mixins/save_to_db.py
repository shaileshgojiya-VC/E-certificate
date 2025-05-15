from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

async def save_object(db: AsyncSession, obj: Any) -> Any:
    
    """
    Generic method to save any SQLAlchemy model object to the database
    
    Args:
        db: AsyncSession - The database session
        obj: Any - The model object to save
        
    Returns:
        The saved object with refreshed data
    """
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj