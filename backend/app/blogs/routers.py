from fastapi import APIRouter, status,HTTPException, Query, Depends
from app.auth.dependencies import get_current_user
from sqlmodel import select
from app.dependencies import SessionDep
from app.blogs.model import Blog, BlogCreateSchema, BlogUpdateSchema
from typing import List, Dict, Any
from sqlalchemy import desc, func, asc
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.user.model import User

router = APIRouter(prefix="/api/v1/blogs", tags=["Blogs"])

@router.get("/latest", status_code=status.HTTP_200_OK, response_model=List[Blog])
def get_latest_blogs(session: SessionDep):
	query = select(Blog).order_by(desc(Blog.created_at)).limit(3) # type: ignore
	blogs = session.exec(query).all()
	return blogs

@router.get("/", status_code=status.HTTP_200_OK)
def get_blogs(
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(3, ge=1),
    sort: str = Query(True),
    q: str = Query("newest")
) -> Dict[str, Any]:
    query = select(Blog)
    if q:
        query = query.where(Blog.title.ilike(f"%{q}%"))  # type: ignore
    total = session.exec(select(func.count()).select_from(query.subquery())).one()
    if sort == "newest":
        query = query.order_by(desc(Blog.created_at))  # type: ignore
    else:
        query = query.order_by(asc(Blog.created_at))   # type: ignore
    blogs = session.exec(query.offset(skip).limit(limit)).all()

    return {
        "data": blogs,
        "query_params": {
            "skip": skip,
            "limit": limit,
            "sort": sort,
            "q": q
        },
        "total": total,
    }

@router.post("/", response_model=Blog)
def create_blog(blog_data: BlogCreateSchema, session: SessionDep, current_user: User = Depends(get_current_user)):
	try:
		new_blog = Blog(**blog_data.model_dump())
		session.add(new_blog)
		session.commit()
		session.refresh(new_blog)
		return new_blog
	except IntegrityError as e:
		session.rollback()
		raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Blog creation failed: {e}"
        )
	except SQLAlchemyError:
		session.rollback()
		raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while creating blog"
        )	

@router.get("/{blog_id}", response_model=Blog, status_code=status.HTTP_200_OK)
def get_blog(blog_id: int, session: SessionDep):
	blog = session.get(Blog, blog_id)
	if not blog:
		raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found."
        )
	else:
		return blog

@router.delete("/{blog_id}", status_code=status.HTTP_200_OK)
def delete_blog(blog_id: int, session: SessionDep, current_user: User = Depends(get_current_user)):
	blog = session.get(Blog, blog_id)
	if not blog: 
		raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found."
        )
	session.delete(blog)
	session.commit()
	return {"message": "Blog deleted successfully."}

@router.put("/{blog_id}", status_code=status.HTTP_200_OK)
def update_blog(
    blog_id: int, 
    updated_blog: BlogUpdateSchema, 
    session: SessionDep, 
    current_user: User = Depends(get_current_user)):
    
    blog = session.get(Blog, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    for field, value in updated_blog.model_dump().items():
        setattr(blog, field, value)
    
    try:
        session.add(blog)
        session.commit()
        session.refresh(blog)
        return blog
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
  